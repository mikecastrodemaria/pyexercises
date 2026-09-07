# pyexercises — Python Programming, SKEMA 2026

The working environment and the examples for the Python Programming course.
No installation required.

> **Where your exercise files are:** on **K2**, the course page. Not here.
> This repository gives you the environment, the examples and the tutor. The
> exercise briefs and the final project datasets are handed out on K2.

---

## Start here

You do this in your **first on-site lab**, with your teacher in the room. The four
online sessions are demonstration and explanation: nothing is asked of you during them.

1. Open **github.com/mikecastrodemaria/pyexercises** and click the green **Use this template** button, then **Create a new repository**
2. Give it a name, keep it **Public**, create it
3. In *your* new repository, click **Code**, then the **Codespaces** tab, then **Create codespace on main**
4. Wait about a minute. A full editor opens in your browser, with Python already installed

That is it. You now have your own copy of the course and a working environment.

> Do not work in this repository. Work in the copy you just created. If you are
> not sure which one you are in, look at the name at the top of the page.

**Before your first lab:** create a GitHub account with your **skema.edu** address and
apply for [GitHub Education verification](https://education.github.com/discount_requests/application).
It takes a few days, so do not leave it to the night before.

---

## What is inside

| Folder | What you find there |
|---|---|
| `examples/` | Working code on every topic of the course, with comments. Run it, change it, run it again |
| `bonus/` | Optional material. Not covered in class, not graded |
| `tutor.py` | The course AI tutor. Gives you bricks, never the building, and logs every exchange |

Slides point to files using this structure. When a slide says
`pyexercises / examples/lists/indexing.py`, open that file in your Codespace.

Every example file ends with a short **What to remember** block. If you read
nothing else, read those.

## Working during the labs

- Write your code, save the file, then click **Run** at the top right
- The terminal at the bottom is where Python answers you
- To install a library: `pip install <name>` in the terminal
- At the end of every session: **Source Control** panel, write a short message, **Commit**, then **Sync**

Your commit history is how your teacher sees the work you did. One single commit
the night before the deadline tells its own story.

---

## How we work with AI

You will use ChatGPT, GitHub Copilot, Claude, Gemini, Mistral or DeepSeek. This is
expected, and it is graded. What is graded is not the code the AI writes, it is your
ability to steer it. Four steps, on every function you write:

1. **Ask** — describe what the code must do, what goes in, what comes out
2. **Read** — write your own comment above each block. If you cannot, you have not understood it
3. **Adapt** — the AI does not know your files. Connect its code to your data
4. **Check** — test one case where you already know the answer

A program that runs is not the same thing as a program that is right.

### The course tutor

This repository ships with its own AI tutor, `tutor.py`. It is the same kind of model
you would use elsewhere, with two differences that matter for you.

- It never hands over a finished program. One function per answer, 22 lines of code at
  most, and no program entry point. The script itself cuts anything longer before you
  see it. It also refuses to give you back your own file: it answers on invented toy data.
- Every exchange is written into `CONVERSATION.md`, which is a graded deliverable.
  You no longer have to rebuild it from memory the night before the deadline.

```
python tutor.py --check                       test your setup
python tutor.py                               start a conversation
python tutor.py "how do I read a semicolon csv"
python tutor.py --log CONVERSATION.md         write the log where you want it
```

Setup takes two minutes and is explained at the top of `tutor.py`. You create a
GitHub token with the Models permission, you paste it into `.env`, and that is all.
It costs nothing and needs no account beyond the GitHub one you already have.

Copilot Chat, inside your Codespace, follows the same rules: they are written in
`.github/copilot-instructions.md` and applied automatically.

You are free to use any other AI. Nobody is checking your browser tabs. But the
program you hand in has to be one you can explain line by line, and a tutor that
refuses to do the work for you is the fastest way to get there.

---

## If Codespaces does not work

Say so during the session, do not stay stuck. Fallbacks:

- Run your code in [Google Colab](https://colab.research.google.com)
- Upload your files through the GitHub web interface, using **Add file**, then **Upload files**
- Install Python and VS Code on your own machine

Free Codespaces quota is 120 hours per month. This course needs about ten.

---

## Course outline

| Session | What you do |
|---|---|
| Online 1 | How software works, where Python sits, how to use AI to write code |
| Online 2 | Environment and method, demonstrated: this repository, Codespaces, a first script, a commit |
| Online 3 | Writing a program: comments, variables, text, numbers, conditions |
| Online 4 | Repeating and storing: lists, dictionaries, loops |
| Lab 1 | Your environment, then comments, variables, strings, asking the user, conditions |
| Lab 2 | Lists, dictionaries, loops |
| Lab 3 | Functions, reading and writing files |
| Lab 4 | Final project: the Campaign Audit Quiz. Graded, handed in on Teams |

---

Mike Castro Demaria — mike.castrodemaria-ext@skema.edu
