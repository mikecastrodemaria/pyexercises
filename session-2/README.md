# Session 2 — Your working environment

Online session 2. Ninety minutes. At the end of it you own a working Python
environment, in your browser, and your first script is saved on GitHub.

Nothing to install. Nothing to pay. If something fails, say so in the chat
straight away instead of staying stuck, there is a fallback at the bottom of
this page.

---

## What you must have done before the session

From session 1, slide 69:

1. A **GitHub account**, created with your **skema.edu** address
2. The **GitHub Education** verification requested (github.com/education, "Get student benefits")

Verification can take a few days. It is a bonus, not a blocker: a free account
is enough for the whole course. Arrive signed in.

> A Microsoft Education account gives you nothing on GitHub. There is no single
> sign-on between the two. Your skema.edu address is only an identifier and a
> proof of eligibility.

---

## What you do during the session

Tick them as you go. The whole session is these eight steps.

| # | Step | How you know it worked |
|---|---|---|
| 1 | Sign in to github.com | Your avatar appears top right |
| 2 | Open **github.com/mikecastrodemaria/pyexercises**, click **Use this template**, then **Create a new repository**. Keep it **Public** | The repository name at the top is *yours*, not `mikecastrodemaria` |
| 3 | Post the URL of your repository in the chat | The teacher can open it |
| 4 | In your repository: **Code**, tab **Codespaces**, **Create codespace on main** | An editor opens in your browser after about a minute |
| 5 | Find the four parts of the editor: file explorer, editor, terminal, source control | You can name them without looking |
| 6 | Create `hello.py` at the root of the repository, print a message, run it | Your message appears in the terminal |
| 7 | In the terminal, install a library: `pip install qrcode` | The last lines say `Successfully installed` |
| 8 | **Source Control**, write a message, **Commit**, then **Sync**. Reload github.com | `hello.py` is visible on the website |

---

## Checking your own work

Once step 7 is done, run this in the terminal:

```
python session-2/check_setup.py
```

It checks eight things and tells you, line by line, what is in place and what is
not. Green light on all eight, you are done for the session.

Run it again at the very end, after your commit and sync, to confirm step 8.

---

## The two mistakes that cost the most time

**Working in the teacher's repository.** If the name at the top of the page is
`mikecastrodemaria/pyexercises`, you are in the wrong place. You cannot save
anything there. Go back to step 2. The check script detects this.

**Waiting in silence.** A Codespace that will not start, a button that is not
where the slide says: it happens, and it is not your fault. Say it in the chat.
Ten seconds of asking beats forty minutes of watching.

---

## Quotas, so you know

A free GitHub account gives you 120 core-hours of Codespaces per month, which is
60 hours of coding on a 2-core machine. This course needs about ten over the whole
semester. Verified Education accounts get 180.

Stop your Codespace when you are done: **Codespaces** menu, **Stop current
codespace**. It also restarts faster next time.

---

## If Codespaces will not work for you

Fallback, in this order:

1. Open `session-2/colab_fallback.ipynb` in [Google Colab](https://colab.research.google.com) and do steps 6 and 7 there
2. Upload your files to your repository through the website: **Add file**, then **Upload files**
3. Install Python and VS Code on your own machine, with help, outside session time

The fallback covers the session. It does not replace the environment: get your
Codespace working before lab 1.
