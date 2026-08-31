"""Session 2 - environment check.

Run this from the terminal of your Codespace, from the root of your repository:

    python session-2/check_setup.py

It checks eight things and tells you what is in place and what is not.
It changes nothing, it only looks.
"""

import os
import subprocess
import sys

TEACHER_REPO = "mikecastrodemaria/pyexercises"

results = []


def record(ok, title, detail):
    """Store one check: passed or not, what it was, what to do about it."""
    results.append((ok, title, detail))


def git(*args):
    """Run a git command and return its output, or None if it fails."""
    try:
        out = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if out.returncode != 0:
            return None
        return out.stdout.strip()
    except Exception:
        return None


def repo_root():
    """The top folder of the repository, or None if we are not in one."""
    return git("rev-parse", "--show-toplevel")


# 1. Python is running and recent enough
version = sys.version_info
record(
    version >= (3, 8),
    "Python is running",
    "Version {}.{}.{}".format(version.major, version.minor, version.micro),
)

# 2. We are inside a git repository
root = repo_root()
record(
    root is not None,
    "You are inside a git repository",
    root if root else "No repository here. Open your Codespace from YOUR repository.",
)

# 3. The repository is yours, not the teacher's
remote = git("remote", "get-url", "origin")
if remote is None:
    record(False, "The repository is yours", "No remote found.")
elif TEACHER_REPO in remote:
    record(
        False,
        "The repository is yours",
        "This is the teacher's repository. Nothing you write here can be saved.\n"
        "        Go back to github.com/" + TEACHER_REPO + " and click Use this template.",
    )
else:
    record(True, "The repository is yours", remote)

# 4. Git knows who you are
name = git("config", "user.name")
email = git("config", "user.email")
record(
    bool(name and email),
    "Git knows who you are",
    "{} <{}>".format(name, email) if name and email else
    "Not set. In the terminal:\n"
    '        git config --global user.name "Your Name"\n'
    '        git config --global user.email "you@skema.edu"',
)

# 5. hello.py exists somewhere in the repository
hello = None
if root:
    for folder, _dirs, files in os.walk(root):
        if ".git" in folder:
            continue
        if "hello.py" in files:
            hello = os.path.join(folder, "hello.py")
            break
record(
    hello is not None,
    "hello.py exists",
    hello if hello else "Not found. Create hello.py and print something in it.",
)

# 6. hello.py actually prints something
if hello:
    with open(hello, "r", encoding="utf-8") as f:
        content = f.read()
    has_print = "print(" in content
    record(
        has_print,
        "hello.py prints something",
        "Found a print() call" if has_print else
        "No print() in the file. A program that displays nothing proves nothing.",
    )
else:
    record(False, "hello.py prints something", "No file to look at yet.")

# 7. pip installed a library outside the standard set
try:
    import qrcode  # noqa: F401
    record(True, "pip installed a library", "qrcode is available")
except ImportError:
    record(
        False,
        "pip installed a library",
        "qrcode not found. In the terminal: pip install qrcode",
    )

# 8. Your work is committed and pushed
commits = git("rev-list", "--count", "HEAD") if root else None
status = git("--no-optional-locks", "status", "--porcelain") if root else None
ahead = git("rev-list", "--count", "@{u}..HEAD") if root else None

if commits is None:
    record(False, "Your work is committed and pushed", "No commit history readable.")
elif status:
    n = len(status.splitlines())
    record(
        False,
        "Your work is committed and pushed",
        "{} file(s) changed but not committed. Source Control, write a message, "
        "Commit, then Sync.".format(n),
    )
elif ahead and ahead != "0":
    record(
        False,
        "Your work is committed and pushed",
        "{} commit(s) not sent to GitHub yet. Click Sync.".format(ahead),
    )
else:
    record(True, "Your work is committed and pushed", "{} commit(s), nothing pending".format(commits))


# Report
print()
print("SESSION 2 - ENVIRONMENT CHECK")
print("=" * 60)

passed = 0
for i, (ok, title, detail) in enumerate(results, start=1):
    mark = "OK  " if ok else "TODO"
    print("{} {}. {}".format(mark, i, title))
    print("        {}".format(detail))
    if ok:
        passed += 1

print("=" * 60)
print("{} of {} checks passed.".format(passed, len(results)))

if passed == len(results):
    print("Your environment is ready. Nothing else to do for session 2.")
else:
    print("Read the TODO lines above, fix them, run this script again.")
    print("Still stuck after two tries: say so in the chat, do not wait.")
print()
