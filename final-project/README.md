# Final project: Campaign Audit Quiz

**Session TP4. Submitted by commit on your repository, within 7 days.**

---

## The situation

You receive the quarterly advertising export of a company. Your job: write a Python program that reads this data, computes the performance indicators, and quizzes the player on what the numbers actually say.

The file `campaigns_X.csv` assigned to you is a raw export, exactly as it comes out of a real tool. It is not clean. That is the point of the exercise.

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

## How to work: the four steps

You will use ChatGPT, Copilot or Gemini. This is expected, encouraged, and graded. What is graded is not the code the AI writes, it is your ability to steer it. Apply these four steps to every function you write.

**1. Ask.** Describe to the AI what the function must do, what goes in, what comes out. A vague request produces vague code.

**2. Read.** Before running anything, add above each block a comment, in your own words, explaining what the block does. If you cannot write that comment, you have not understood the code: ask the AI to explain it again.

**3. Adapt.** The AI does not know your file. It will invent column names, assume a separator, ignore the edge cases. Connecting its code to your real data is your job.

**4. Check.** Take one case where you know the answer by hand, and compare. A program that runs without an error is not the same thing as a program that is right.

---

## Deliverables

In your repository, at root level:

| File | Content |
|---|---|
| `campaign_audit.py` | Your program, commented in your own words |
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
| The comments are yours | 4 | They explain intent, not syntax. A wrong or empty comment costs more than a missing one |
| The AI conversation is documented | 3 | It shows the errors you hit and how you solved them |

Two students submitting the same code with different datasets get different results. A result that does not match your own file is the signal of code reused without being understood.

---

## Optional extras

- Handle the case where the player types an answer in an unexpected format
- Add a sixth question of your own
- Keep the score history from one game to the next
- Display a ranking of campaigns by ROAS, highest first
