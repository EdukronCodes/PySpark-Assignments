# Day 02: Explicit schemas and file ingestion

Suggested date: 2026-10-07. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

StructType; nullable; CSV options; JSON; corrupt records; inference costs.

## Before you begin

Complete Day 01; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Define schemas for all six batch tables.
2. Read prices and discounts as decimal values, IDs as strings, and timestamps explicitly.
3. Compare inferred and explicit schemas.
4. Create a three-line malformed CSV fixture and compare PERMISSIVE, DROPMALFORMED, and FAILFAST.
5. Record file path and ingestion time as audit columns.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([StructField("customer_id", StringType()), StructField("city", StringType())])
# Extend the schema to match the complete customers file before reading it.
```

## More examples to solve

1. Read an empty file with an explicit schema. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Read JSON events using the supplied schema. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Handle a quoted comma in a CSV value. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. Why can schema inference be risky for customer and product identifiers?
2. What do StructType and StructField represent?
3. What does nullable mean in a Spark schema?
4. Which type should represent quantity, and why?
5. Why use a decimal type for retail prices?
6. How do DateType and TimestampType differ?
7. What does the CSV header option control?
8. What is the difference between a blank field and a quoted empty string?
9. What does PERMISSIVE parsing attempt to preserve?
10. Why do file streams normally require an explicit schema?

### Hands-on questions (11-20)

11. Define and use a complete schema for customers.csv.
12. Define a complete order_items schema with decimal prices and discounts.
13. Read orders with order_ts parsed as a timestamp in UTC.
14. Compare inferred and explicit schemas for the same CSV file.
15. Read a CSV fixture containing a quoted comma in a customer name.
16. Read a header-only CSV with an explicit schema and verify zero rows.
17. Create a malformed numeric fixture and inspect PERMISSIVE output.
18. Compare DROPMALFORMED and FAILFAST on that fixture using an action.
19. Add source filename and ingestion timestamp audit columns.
20. Read one event archive file using the supplied nested event_schema.

### Advanced challenges (21-30)

21. Preserve malformed CSV evidence using a configured corrupt-record column.
22. Explain why fewer or extra CSV tokens are not always classified as corrupt records.
23. Demonstrate how column pruning can affect CSV corruption detection.
24. Compare missing columns, reordered columns, and incompatible types during ingestion.
25. Design a contract that distinguishes parsing failures from business-rule failures.
26. Explain why nullable=False is not a complete data-quality enforcement strategy.
27. Preserve an identifier with leading zeros through read and write.
28. Create a decimal-overflow fixture and record parsing behavior under your configuration.
29. Design ingestion that retains raw text for rows that cannot be typed safely.
30. Write a reusable reader with schema, format, audit columns, and parse-mode arguments.


## Completion checks

A malformed row is visible in your audit output; every table has a documented schema.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-02/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-02/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day02/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-02/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
