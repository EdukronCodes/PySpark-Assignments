# Day 07: Project 1 - Retail sales report

Suggested date: 2026-10-12. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

batch integration; quality report; reproducibility; business explanation.

## Before you begin

Complete Day 06; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Package Days 2-6 into a repeatable sales-report script.
2. Produce store and channel KPIs plus top ten products by booked revenue.
3. Add counts for raw, rejected, duplicated, and accepted rows.
4. Write Parquet reports and a small Markdown executive summary.
5. Rerun from raw files and compare outputs by business key.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Build a main() function with input and output path arguments.
# Use the Day 6 order-level table for AOV, not the line-level table.
```

## More examples to solve

1. Explain why top products by units differ from top products by revenue. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Add a zero-revenue store. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Investigate one quarantined line end to end. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. Who is the intended consumer of the sales report?
2. Which raw tables are required to compute booked revenue?
3. What is the output grain of the store report?
4. What is the output grain of the product report?
5. Why must cancelled orders be excluded from booked revenue?
6. What cleaning evidence should accompany a sales report?
7. Why should an input path be configurable?
8. What makes a report rerun reproducible?
9. Why keep monetary outputs in Parquet rather than only screenshots?
10. What business assumption must the report disclose about tax and shipping?

### Hands-on questions (11-20)

11. Assemble ingestion, cleaning, deduplication, and aggregation into one script.
12. Publish revenue and AOV by store.
13. Publish revenue and revenue share by channel.
14. Publish the top ten products by booked revenue.
15. Publish raw, quarantined, removed-duplicate, and accepted counts.
16. Verify booked revenue equals the manifest's expected amount.
17. Write a short explanation of the best-performing store.
18. Compare top products by units against top products by revenue.
19. Rerun the script with the same inputs and compare business rows.
20. Trace one BAD line from raw input to its quarantine reason.

### Advanced challenges (21-30)

21. Add a store with no sales without excluding it from the store report.
22. Test that an injected cancelled high-value order never increases booked revenue.
23. Test that an identical duplicate line never increases booked revenue.
24. Design behavior when every input line is rejected.
25. Demonstrate a failure caused by a missing product dimension key.
26. Make ranking deterministic when two products have equal revenue.
27. Explain whether two Parquet directories must be byte-identical to represent equal reports.
28. Design a report-level contract covering schema, grain, and totals.
29. Estimate what changes are needed to run the report over a year of large data.
30. Prepare a five-minute walkthrough with reproducible commands and reconciliation evidence.


## Completion checks

A second run produces identical business rows; no cancelled order contributes to booked revenue.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-07/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-07/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day07/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-07/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
