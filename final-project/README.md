# Final project: Campaign Audit Quiz

**Session TP4. Submitted by commit on your repository, within 7 days.**

---

## The situation

You receive the quarterly advertising export of a company. Your job: write a Python program that reads this data, computes the performance indicators, and quizzes the player on what the numbers actually say.

Your repository already contains three datasets in `final-project/`: `campaigns_A.csv`, `campaigns_B.csv` and `campaigns_C.csv`. **Your teacher tells you which one is yours. Use only that one.** They hold different numbers and give different answers, so working from a neighbour's file gives you the wrong result.

The file is a raw export, exactly as it comes out of a real tool. It is not clean. That is the point of the exercise.

---

## What the program must do

1. Read the file `campaigns_X.csv`
2. Compute, for each campaign: CTR, CPA and ROAS
3. Ask the player 5 questions whose answers must be computed from the data
4. Check each answer and keep the score
5. Display the final score
6. Write a file `result.csv` with the player name, the score and the date

---

## The 5 questions

1. Which campaign has the best CTR?
2. Which campaign has the highest CPA?
3. How many campaigns have a ROAS above 3?
4. Which channel generated the most conversions in total?
5. What is the average CTR across all campaigns, rounded to two decimals?

The correct answers are written nowhere. Your program must compute them.

---

## The formulas

| Indicator | Formula | Meaning |
|---|---|---|
| CTR | clicks / impressions | Share of people who saw the ad and clicked |
| CPA | cost / conversions | How much one conversion costs |
| ROAS | revenue / cost | How much one euro spent brings back |

---

## Data rules

These three rules are part of the assignment. A program that ignores them returns wrong numbers.

- **Incomplete row**: a campaign with an empty impressions cell is excluded from every calculation.
- **Zero conversions**: a campaign with no conversion has no CPA. Exclude it from the CPA calculation, keep it in the others. Your program must not crash on it.
- **Number format**: amounts use the European decimal comma. `11088,60` means eleven thousand and eighty-eight euros and sixty cents.

---

## Answer these before you ask an AI anything

Write your answers as comments at the top of `campaign_audit.py`. They are graded, and
they are what makes the difference between building a program and pasting one.

1. **What goes in?** Open your dataset and describe it: how many rows, which columns,
   what separator, how the amounts are written. Do not guess, look.
2. **What happens to it?** List the steps, in order, in plain English. One line each.
3. **What comes out?** Describe both outputs: what the player sees on screen, and what
   ends up in `result.csv`.
4. **What could go wrong?** Read your file again and list every row that is not like the
   others. There are at least three. Say what your program will do with each.

## What an AI assistant cannot know

Paste this brief into ChatGPT, Copilot, Claude, Gemini, Mistral or DeepSeek and it will
happily write you a program. That program will not work, and it is worth understanding
why before you start.

- **It has not seen your file.** It does not know the separator, the column names, the
  way the amounts are written, or which variant you were given. It will invent all of it,
  confidently.
- **It does not know which rows are broken.** Two campaigns have no conversions, one row
  is incomplete. It cannot know that unless you tell it.
- **It cannot check the result.** Only you can compute one value by hand and compare.

So the work is not writing the program. It is describing the situation precisely enough
that a program can be written, then verifying that it was. That is the same work you will
do the day you brief a developer, or an agency.

## How to work: the four steps

You will use ChatGPT, GitHub Copilot, Claude, Gemini, Mistral or DeepSeek, Claude, Gemini, Mistral or DeepSeek. This is expected, encouraged, and graded. What is graded is not the code the AI writes, it is your ability to steer it. Apply these four steps to every function you write.

**1. Ask.** Describe to the AI what the function must do, what goes in, what comes out. A vague request produces vague code.

**2. Read.** Before running anything, add above each block a comment, in your own words, explaining what the block does. If you cannot write that comment, you have not understood the code: ask the AI to explain it again.

**3. Adapt.** The AI does not know your file. It will invent column names, assume a separator, ignore the edge cases. Connecting its code to your real data is your job.

**4. Check.** Take one case where you know the answer by hand, and compare. A program that runs without an error is not the same thing as a program that is right.

---

## Deliverables

In the `final-project/` folder of your repository, next to the datasets:

| File | Content |
|---|---|
| `campaign_audit.py` | Your program, commented in your own words, with the four answers above at the top |
| `campaigns_X.csv` | The dataset assigned to you |
| `result.csv` | One example of the output your program produces |
| `CONVERSATION.md` | Your exchanges with the AI: what you asked, what it answered, what you had to fix |

---

## Grading, 20 points

| Criterion | Points | What we look at |
|---|---|---|
| The program runs | 3 | It goes from start to end without crashing |
| The numbers are correct | 4 | The five answers match the dataset |
| Edge cases are handled | 3 | Incomplete row, zero conversions, decimal comma |
| The code is split into functions | 3 | One function per task, names that say what they do |
| The comments are yours | 4 | The four answers at the top, plus one comment per block explaining intent, not syntax. A wrong or empty comment costs more than a missing one |
| The AI conversation is documented | 3 | It shows the errors you hit and how you solved them |

Two students submitting the same code with different datasets get different results. A result that does not match your own file is the signal of code reused without being understood.

---

## Submission

**You hand in at the end of session 8, on Teams. Not one extra minute.**

Upload the four files above to the Teams assignment. The deadline is the end of the session, and it does not move: last year the delay was used to pass copies around, so there is no longer a delay.

Every submission goes through a code check. A program you cannot explain line by line is a program you did not write, whatever the AI told you.

The Gradio bonus is the only thing accepted afterwards: the link to your published Space goes in the same Teams assignment, up to seven days after the session.

---

## Bonus, up to 2 points on top of the 20

Optional. Nobody is penalised for skipping it, and it never compensates a program that does not run.

Your program already has an IN box, a PROCESS box and an OUT box. The bonus only changes the last one: instead of printing in a terminal, the same code answers on a web page anyone can open.

| Criterion | Points | What we look at |
|---|---|---|
| A working Gradio interface | 1 | The user uploads a campaign export and reads the answers on the page. Your existing functions are reused, not rewritten |
| A published link | 1 | The Space runs, the link is in your repository README, and we can click it without asking you for anything |

How: wrap your existing audit function in `gr.Interface(...)`, then publish it on a free Hugging Face Space (CPU Basic, no card, no cost). Covered in online session 4.

Two things that cost the bonus: a page that works only on your machine, and an interface built around code that crashes on the incomplete row.

---

## Optional extras

- Handle the case where the player types an answer in an unexpected format
- Add a sixth question of your own
- Keep the score history from one game to the next
- Display a ranking of campaigns by ROAS, highest first
