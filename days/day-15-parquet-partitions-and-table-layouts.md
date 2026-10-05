# Day 15: Parquet, partitions, and table layouts

Suggested date: 2026-10-20. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

columnar storage; partition pruning; compression; small files; catalogs.

## Before you begin

Complete Day 14; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Write facts as Parquet partitioned by order_date.
2. Read one date with a filter and inspect PartitionFilters.
3. Compare CSV and Parquet sizes and schemas.
4. Create a temporary SQL view over Parquet and query it.
5. Discuss managed versus external tables and choose suitable partition columns.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
facts.write.mode("overwrite").partitionBy("order_date").parquet("outputs/day15/facts")
```

## More examples to solve

1. Why customer_id is usually a poor partition column. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. A one-day overwrite accidentally removes other dates: demonstrate on scratch data. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Compare coalesce(1) with multiple output files. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is columnar storage?
2. How does Parquet differ from CSV?
3. What does directory partitioning encode?
4. What is partition pruning?
5. Why can high-cardinality partition keys cause problems?
6. What is a small-file problem?
7. How do repartition and coalesce differ?
8. What does overwrite mode do at an output path?
9. What is the difference between a managed and an external table?
10. Why is order_date a plausible retail partition column?

### Hands-on questions (11-20)

11. Write clean facts as Parquet partitioned by order_date.
12. Read one date and verify its rows against a full-data filter.
13. Inspect PartitionFilters in an explain plan.
14. Compare CSV and Parquet schema preservation.
15. Compare output sizes and file counts for both formats.
16. Create a SQL view over a Parquet path.
17. Write a scratch dataset with coalesce(1) and inspect file count.
18. Compare compression settings on the same scratch dataset.
19. List how many files were written per date partition.
20. Demonstrate overwrite behavior only on disposable scratch data.

### Advanced challenges (21-30)

21. Explain why partitioning by customer_id can produce too many directories.
22. Distinguish partition pruning from Parquet predicate pushdown.
23. Compare selecting two columns with reading every column in the plan.
24. Design a compaction strategy for many tiny daily files.
25. Explain why coalesce(1) can bottleneck a large output.
26. Compare static and dynamic partition overwrite on an isolated fixture.
27. Document how appending incompatible schemas should be prevented.
28. Design retention and backfill boundaries for a partitioned fact table.
29. Compare directory partitions with runtime execution partitions.
30. Propose a file layout for one year of retail data with daily reporting needs.


## Completion checks

Pruned reads return the same rows as filtered full reads; file counts and sizes are recorded.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-15/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-15/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day15/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-15/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
