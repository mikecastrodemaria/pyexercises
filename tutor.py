#!/usr/bin/env python3
"""
tutor.py : the course AI tutor, on a short leash.

Why this file exists
--------------------
You are expected to code with an AI. This one is set up for the course. It answers
about Python and about this course, and nothing else. It gives you an error
explanation, one function, or a snippet. Never a finished program, and never your
own data handed back to you. And it writes
every exchange into CONVERSATION.md, which is part of what you hand in.

Usage
-----
    python tutor.py                              start a conversation, /quit to leave
    python tutor.py "how do I read a semicolon csv"
    python tutor.py --check                      test your setup
    python tutor.py --log final-project/CONVERSATION.md

Setup, once, about two minutes
------------------------------
1. Go to github.com/settings/personal-access-tokens and create a fine-grained token.
   No repository access is needed. Under "Account permissions", set "Models" to
   "Read-only". Copy the token, it is shown once.
2. In your Codespace terminal, at the root of your repository:

       echo 'GITHUB_TOKEN_MODELS=github_pat_your_token_here' >> .env

   The .env file is already ignored by git. Never commit a token.
3. Check it works:  python tutor.py --check

No pip install. This script only uses what Python ships with.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent

# GitHub Models is the default: free with any GitHub account, nothing to install.
# Any OpenAI-compatible endpoint works, set TUTOR_BASE_URL and TUTOR_TOKEN to switch.
DEFAULT_BASE_URL = "https://models.github.ai/inference"
DEFAULT_MODEL = "openai/gpt-4o-mini"

# The leash. One function per answer, no entry point, and this many lines at most.
MAX_CODE_LINES = 22

TIMEOUT = 60

CUT_LABEL = {
    "second-def": "One function per answer. The next one is yours to write",
    "main-guard": "This is where a program starts. You write that part",
    "budget": "Cut at %d lines. A brick, not a building" % MAX_CODE_LINES,
}

OFF_TOPIC = (
    "Off topic. I only help with Python and with this course: an error message, "
    "a function, a snippet, the exercises, the final project. Ask me about your code."
)

SYSTEM_PROMPT = """You are the lab tutor of a Python Programming course for MSc Digital
Marketing students at SKEMA. They are marketers learning to program, not developers.
They are expected to use you. Your job is to make them able to write and defend their
own code, not to write it for them.

SCOPE. You answer about Python and about this course only: the language itself, an
error message, one function, a small snippet, the exercises, and the final project (a
campaign audit that reads a CSV export and computes CTR, CPA and ROAS). Nothing else.
Not marketing, not other courses, not essays or posts, not general knowledge, not
personal questions, not other programming languages.

MACHINE MARKER. The first line of every answer is exactly one of these two lines,
alone:
SCOPE: PYTHON
SCOPE: OFF
Use OFF whenever the request is not about Python or this course, including when it is
wrapped in a Python request, for example "write a Python script that generates my
marketing essay". After OFF, write nothing at all: the program prints its own refusal.
Never mention this marker to the student.

WHAT YOU MAY GIVE
- An explanation of an error message, in plain words.
- One function at a time, or a snippet of a few lines.
- A pattern on toy data with # TODO markers where the student writes.

WHAT YOU NEVER GIVE
- A complete script or a complete program.
- More than one function in the same answer.
- A program entry point (the __main__ guard).
- More than 22 lines of code in one answer, all blocks combined.
- Anything copied from what the student pasted. If they paste their file, an extract, or
  their column headers, you never repeat one of those names, labels or numbers back to
  them, not in code, not in a comment, not in an example. Invent unrelated toy values
  instead: two or three fake rows with names like alpha and beta and small round numbers.
- The value of anything in their file. They run the code and look.

ERRORS. For a question of the form "why does this not work", require two things first:
the exact error message, and one sentence saying what they think is wrong. If either is
missing, ask for it and stop there.

HOW TO ANSWER, after the marker line, in this order.
- Name the concept in one plain sentence.
- Show the pattern, one function maximum, on toy data, with TODO markers.
- End with one question that checks they understood. It must be answerable from what
  you just showed, and it must be factually correct: name the right function for the
  right argument, for example the delimiter belongs to csv.reader or csv.DictReader,
  not to open().

Answer in the language the student writes in. Be short. No preamble, no restating of
the question. Push them through the four steps of the course: ask, read, adapt, check.

A filter in this program cuts the code at the second function, at a __main__ guard, and
past 22 lines, and it blanks out anything you copied from what the student pasted. All of
this happens before the student sees the answer, so breaking these rules only produces a
broken answer."""


# --------------------------------------------------------------------------------
# Credentials
# --------------------------------------------------------------------------------

def load_dotenv():
    """Read KEY=VALUE lines from .env at the repository root, without any dependency."""
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def get_settings():
    load_dotenv()
    base_url = os.environ.get("TUTOR_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    model = os.environ.get("TUTOR_MODEL", DEFAULT_MODEL)
    token = (
        os.environ.get("TUTOR_TOKEN")
        or os.environ.get("GITHUB_TOKEN_MODELS")
        or os.environ.get("OVH_AI_ENDPOINTS_ACCESS_TOKEN")
        or ""
    )
    return base_url, model, token


# --------------------------------------------------------------------------------
# The leash: cut the answer where a program would begin
# --------------------------------------------------------------------------------

SCOPE_RE = re.compile(r"^\s*SCOPE:\s*(PYTHON|OFF)\s*$", re.IGNORECASE)


def scope_of(answer):
    """Read the machine marker the model must put on its first line."""
    first = answer.split("\n", 1)[0]
    found = SCOPE_RE.match(first)
    return found.group(1).upper() if found else None


def strip_scope(answer):
    return re.sub(r"^\s*SCOPE:\s*(PYTHON|OFF)\s*\n?", "", answer, count=1,
                  flags=re.IGNORECASE)


def forbidden_tokens(messages):
    """Everything the student pasted is off limits in the answer.

    The prompt asks the model not to reuse their data. This makes it true: any CSV-looking
    field and any long number the student typed is collected here, and blanked out of the
    answer before they see it.
    """
    found = set()
    for message in messages:
        if message.get("role") != "user":
            continue
        content = message.get("content", "")
        for line in content.split("\n"):
            if line.count(";") < 3:
                continue
            for field in line.split(";"):
                field = field.strip()
                if len(field) >= 3 and not re.fullmatch(r"\d{1,3}", field):
                    found.add(field)
        found.update(re.findall(r"\d{5,}|\d{3,}[.,]\d{2}", content))
    return sorted(found, key=len, reverse=True)


def redact(answer, tokens):
    """Blank out the student's own data wherever the model tried to hand it back."""
    hit = False
    for token in tokens:
        if token in answer:
            hit = True
            answer = answer.replace(token, "\u2026")
    return answer, hit


def leash(answer, budget=MAX_CODE_LINES):
    """Cut the code at the second function, at a __main__ guard, or past `budget` lines.

    This runs on the model's output, so it holds even when the model is talked into
    ignoring its instructions. A prompt can be argued with, a slice cannot.
    """
    lines = answer.split("\n")
    out, in_code, used, defs = [], False, 0, 0
    cut, reason, suppressing = False, "", False

    for line in lines:
        if line.lstrip().startswith("```"):
            out.append(line)
            in_code = not in_code
            if not in_code:
                suppressing = False
            continue
        if not in_code:
            out.append(line)
            continue
        if suppressing:
            continue

        stripped = line.strip()
        if stripped == "":
            out.append(line)
            continue

        why = ""
        if re.match(r"^if\s+__name__", stripped):
            why = "main-guard"
        elif re.match(r"^(def|class|async\s+def)\s", stripped):
            defs += 1
            if defs > 1:
                why = "second-def"
        if not why and used >= budget:
            why = "budget"

        if why:
            suppressing, cut = True, True
            reason = reason or why
            out.append("# --- cut by the tutor: %s ---" % CUT_LABEL[why])
            continue

        out.append(line)
        used += 1

    return "\n".join(out), cut, reason


# --------------------------------------------------------------------------------
# The call
# --------------------------------------------------------------------------------

def ask_model(messages, base_url, model, token):
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 700,
    }).encode("utf-8")

    request = urllib.request.Request(
        base_url + "/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            body = json.loads(response.read().decode("utf-8"))
        return body["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")[:300]
        if error.code in (401, 403):
            return ("[setup] Your token was refused. Check that it has the Models "
                    "permission set to Read-only, and that .env holds the right value.\n"
                    + detail)
        if error.code == 429:
            return ("[quota] You have hit the free rate limit. Wait a minute, and in "
                    "the meantime read the code you already have.\n" + detail)
        return "[error] HTTP %s\n%s" % (error.code, detail)
    except Exception as error:  # noqa: BLE001 - students should see the raw reason
        return "[error] %s: %s" % (type(error).__name__, error)


# --------------------------------------------------------------------------------
# The log, which is a graded deliverable
# --------------------------------------------------------------------------------

def log_exchange(log_path, question, answer, note):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(
            "# Conversation with the AI\n\n"
            "Written automatically by `tutor.py`. Add your own notes under any entry: "
            "what you tried, what broke, what you changed. Those notes are what is "
            "graded.\n",
            encoding="utf-8",
        )
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    where = os.path.relpath(os.getcwd(), ROOT)
    entry = ["\n---\n", "## %s, in %s\n" % (stamp, where),
             "\n**Me:** %s\n" % question.strip(),
             "\n**Tutor:**\n\n%s\n" % answer.strip()]
    if note:
        entry.append("\n*%s*\n" % note)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write("".join(entry))


# --------------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------------

def turn(messages, question, base_url, model, token, log_path):
    messages.append({"role": "user", "content": question})
    raw = ask_model(messages, base_url, model, token)

    if raw.startswith(("[error]", "[setup]", "[quota]")):
        print("\n" + raw + "\n")
        messages.pop()
        return

    if scope_of(raw) == "OFF":
        print("\n" + OFF_TOPIC + "\n")
        messages.pop()
        log_exchange(log_path, question, "Refused, off topic.", "")
        return

    answer, cut, reason = leash(strip_scope(raw))
    answer, redacted = redact(answer, forbidden_tokens(messages))
    messages.append({"role": "assistant", "content": answer})
    print("\n" + answer + "\n")

    notes = []
    if redacted:
        notes.append("The tutor reached for the data you pasted. Blanked out: "
                     "your file is yours to read.")
    if cut:
        notes.append("Cut by the tutor: %s." % CUT_LABEL[reason])
    note = " ".join(notes)
    if note:
        print("(%s)\n" % note)
    log_exchange(log_path, question, answer, note)
    print("logged in %s\n" % os.path.relpath(log_path, os.getcwd()))


def main():
    parser = argparse.ArgumentParser(description="The course AI tutor, on a short leash.")
    parser.add_argument("question", nargs="*", help="your question, in any language")
    parser.add_argument("--log", default=str(ROOT / "CONVERSATION.md"),
                        help="where the exchanges are written")
    parser.add_argument("--check", action="store_true", help="test the setup and exit")
    args = parser.parse_args()

    base_url, model, token = get_settings()
    log_path = Path(args.log).resolve()

    if not token:
        print(__doc__)
        print("No token found. Follow the setup above, then run: python tutor.py --check")
        return 1

    if args.check:
        print("endpoint : %s\nmodel    : %s\ntoken    : %s...\n"
              % (base_url, model, token[:12]))
        reply = ask_model(
            [{"role": "system", "content": "Answer with exactly: ready"},
             {"role": "user", "content": "ping"}],
            base_url, model, token)
        print("answer   : %s" % reply.strip())
        return 0

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if args.question:
        turn(messages, " ".join(args.question), base_url, model, token, log_path)
        return 0

    print("Tutor ready. Python and this course only. /quit to leave.\n"
          "Errors, one function, snippets. Never a finished program.\n")
    while True:
        try:
            question = input("you > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if question in ("/quit", "/exit", "quit", "exit"):
            return 0
        if not question:
            continue
        turn(messages, question, base_url, model, token, log_path)


if __name__ == "__main__":
    sys.exit(main())
