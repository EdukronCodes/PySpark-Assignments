# Day 01: Setup and your first retail DataFrame

Suggested date: 2026-10-06. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

SparkSession; driver and executors; lazy evaluation; transformations and actions; schemas.

## Before you begin

Complete SETUP.md and read DATA_DICTIONARY.md.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Create an environment and run the dataset generator.
2. Start local[2] with UTC timestamps and four shuffle partitions.
3. Read orders.csv and print its schema, count, and ten rows.
4. Select order_id, customer_id, status and explain what triggers execution.
5. Create a five-row DataFrame manually with an explicit schema.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
orders = spark.read.option("header", True).csv("data/raw/orders.csv")
orders.printSchema()
orders.show(10, truncate=False)
```

## More examples to solve

1. Filter orders for store S01. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Count orders by channel. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Compare show(), take(3), and collect() on a tiny subset. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What problem does PySpark solve when retail data outgrows one computer?
2. What is a SparkSession, and how do you create one?
3. What does local[2] mean in the supplied setup?
4. What is the driver's role in a Spark application?
5. What work is performed by executors?
6. What is a DataFrame, and what does its schema describe?
7. How do transformations differ from actions?
8. Why does constructing a filter not immediately read every row?
9. How do you display five orders without collecting the whole table?
10. How do you stop a SparkSession after an assignment?

### Hands-on questions (11-20)

11. Read orders.csv and verify its row count against the manifest.
12. Print the order schema and identify columns read as strings.
13. Select order_id, customer_id, and status and display ten rows.
14. Filter orders from S01 and display only their IDs.
15. Count completed and cancelled orders separately without using Python loops.
16. Create a five-row customer DataFrame with an explicit string schema.
17. Rename status to order_status without altering the source DataFrame.
18. Find the distinct channel values and explain why the result is small.
19. Compare show(3), take(3), and collect() on a five-row fixture.
20. Set the session timezone to UTC and verify the configuration value.

### Advanced challenges (21-30)

21. Predict how many actions run when the same filtered DataFrame is counted twice.
22. Explain why reading 300 rows locally does not demonstrate cluster scalability.
23. Reproduce an unresolved-column error and explain its message.
24. Explain why DataFrame rows have no guaranteed order unless explicitly sorted.
25. Show that withColumn returns a new DataFrame rather than mutating the original.
26. Design a safe inspection strategy for a billion-row orders table.
27. Compare where SparkSession objects and distributed row data live.
28. Identify driver-side Python code and distributed work in your solution.
29. Predict when a missing input path fails: during read construction or an action; verify.
30. Write a reusable session factory and a five-row smoke-check script.


## Completion checks

The raw orders count equals data/manifest.json; explain why collect() is unsafe for large data.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-01/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-01/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day01/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-01/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
