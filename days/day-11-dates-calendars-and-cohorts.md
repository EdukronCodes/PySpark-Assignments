# Day 11: Dates, calendars, and cohorts

Suggested date: 2026-10-16. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

to_timestamp; date_trunc; datediff; calendar joins; cohort retention.

## Before you begin

Complete Day 10; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Parse order_ts in UTC and derive date, week, and month.
2. Create a complete calendar covering the supplied data.
3. Fill missing store dates with zero revenue.
4. Define first completed purchase month as cohort.
5. Calculate month-0 and month-1 customer retention using distinct customers.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
orders = orders.withColumn("order_ts", F.to_timestamp("order_ts"))
orders = orders.withColumn("order_date", F.to_date("order_ts"))
```

## More examples to solve

1. Order at 23:59 UTC viewed in Asia/Kolkata. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Missing sales date versus missing input file. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Customer signs up but never orders: exclude from purchase cohorts. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. Why distinguish a timestamp from a date?
2. What does the session timezone affect?
3. How does to_timestamp differ from to_date?
4. What does date_trunc return for a month?
5. How does datediff calculate elapsed days?
6. What is a calendar dimension?
7. Why can missing dates distort rolling averages?
8. What is a customer purchase cohort?
9. What is the denominator of cohort retention?
10. Why exclude customers without purchases from purchase cohorts?

### Hands-on questions (11-20)

11. Parse order_ts and derive order_date in UTC.
12. Calculate daily and monthly completed-order revenue.
13. Generate a date calendar covering the full sales period.
14. Build store-date combinations and fill missing sales with zero.
15. Find each customer's first completed purchase month.
16. Calculate month-0 cohort customer counts.
17. Calculate month-1 retained customer counts.
18. Calculate retention percentages with distinct customers.
19. Convert a 23:59 UTC fixture to Asia/Kolkata and compare dates.
20. Verify that month-0 retention is 100% for every nonempty cohort.

### Advanced challenges (21-30)

21. Calculate month offsets across a December-to-January boundary.
22. Explain why months_between can be inappropriate for integer cohort offsets.
23. Distinguish a true zero-sales day from a day whose ingestion failed.
24. Handle incomplete recent cohorts without interpreting unobserved months as churn.
25. Test leap-day and month-end date calculations on synthetic fixtures.
26. Compare week definitions at year boundaries and state the chosen convention.
27. Calculate a seven-calendar-day rolling revenue after calendar densification.
28. Define retention when a customer buys multiple times in the same month.
29. Build an as-of-date parameter so cohort outputs remain reproducible.
30. Publish a cohort matrix with observed-versus-unobserved cells distinguished.


## Completion checks

Month-0 retention is 100% for nonempty cohorts; missing calendar dates are represented.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-11/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-11/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day11/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-11/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
