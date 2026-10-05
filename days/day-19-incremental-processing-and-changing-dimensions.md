# Day 19: Incremental processing and changing dimensions

Suggested date: 2026-10-24. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

watermarks for batch ingestion; business updates; SCD1; SCD2; idempotence; lakehouse concepts.

## Before you begin

Complete Day 18; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Split orders into two arrival batches and preserve ingest metadata.
2. Create an updated customer row and implement SCD1 with latest update time.
3. Build SCD2 valid_from, valid_to, and is_current on a tiny fixture.
4. Join historical orders to the dimension version valid at order time.
5. Design an idempotent batch manifest and discuss transactional Delta/Iceberg/Hudi alternatives.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Use half-open validity: order_ts >= valid_from and order_ts < valid_to.
# Plain Parquet has no native MERGE; use a full snapshot for this small exercise.
```

## More examples to solve

1. Customer moves cities between two orders. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. A late order arrives with an old business date. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Retry an already committed input batch. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is incremental batch ingestion?
2. How does ingestion time differ from business event time?
3. What is an ingestion high-water mark?
4. How is a batch high-water mark different from a streaming event-time watermark?
5. What does SCD Type 1 retain?
6. What does SCD Type 2 retain?
7. What do valid_from and valid_to represent?
8. Why use half-open validity intervals?
9. What makes an incremental load idempotent?
10. Why does plain Parquet not provide a native transactional MERGE?

### Hands-on questions (11-20)

11. Split orders into two input arrival batches.
12. Add batch_id and ingested_at metadata.
13. Create a customer city update with a newer update timestamp.
14. Build a latest-row SCD1 customer snapshot.
15. Build two SCD2 versions for a changing customer.
16. Join an order to the customer version valid at order time.
17. Detect overlapping validity intervals for the same customer.
18. Create a committed-input manifest for processed batch IDs.
19. Retry the same input batch and verify no duplicate business rows.
20. Publish a small complete snapshot after validation rather than assuming Parquet upserts.

### Advanced challenges (21-30)

21. Handle a late order whose business date precedes the latest ingestion timestamp.
22. Explain why filtering solely on max(order_ts) can miss late-arriving records.
23. Create an out-of-order dimension update and rebuild valid intervals correctly.
24. Handle two customer updates with the same timestamp using a documented policy.
25. Model a customer deletion or inactive status without deleting historical facts.
26. Design recovery when output is staged but the batch manifest is not committed.
27. Compare SCD2 business history with system ingestion history.
28. Explain the transaction guarantees that Delta, Iceberg, or Hudi can add.
29. Define a backfill strategy that updates historical partitions safely.
30. Write an incremental-load design with retry, late-data, and concurrent-writer assumptions.


## Completion checks

SCD2 intervals do not overlap per customer and retries do not double output.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-19/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-19/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day19/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-19/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
