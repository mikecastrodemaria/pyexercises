# A note on the sample CSV

`files/sample_campaigns.csv` is deliberately imperfect, like the file of the final project:

- semicolon separator, as European spreadsheets export it
- decimal comma on the amounts
- an empty unnamed column before the revenue
- one row with no impressions
- one campaign with zero conversions

Code that ignores these produces wrong numbers without ever crashing.
That is the point of the exercise.
