# Day 30: Project 5 - Batch and streaming retail capstone

Suggested date: 2026-11-04. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

architecture; reconciliation; deployment; security; observability; design tradeoffs.

## Before you begin

Complete Day 29; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Integrate the sales mart, customer mart, returns, stream monitoring, and one ML experiment.
2. Map streaming purchase order_ids to batch orders and classify unmatched orders without assuming all events reconcile.
3. Produce an architecture diagram, data contract, deployment command, and recovery runbook.
4. Demonstrate initial load, two event batches, duplicate replay, late event, and restart.
5. Review partitioning, privacy of synthetic customer fields, dependency versions, cluster sizing, and access control.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Use spark-submit with configuration and explicit input/output paths.
# Refer to PROJECTS.md for the final scoring rubric.
```

## More examples to solve

1. Compare daily finalized batch reports with provisional streaming metrics. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Backfill an old day without corrupting current output. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Explain cost, correctness, and latency tradeoffs for a 1-million-event/day retailer. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What are the main layers of your final retail platform?
2. Which datasets are sources of truth for batch financial reports?
3. Which outputs serve customer analytics?
4. Which outputs serve live operational monitoring?
5. What does a data contract specify?
6. What is a recovery runbook?
7. Why separate finalized daily results from provisional streaming metrics?
8. What does spark-submit provide?
9. Why should runtime credentials remain outside source code?
10. Which limitations of the synthetic fixtures must the final project disclose?

### Hands-on questions (11-20)

11. Integrate the sales report, customer mart, return adjustments, and live monitor.
12. Create an architecture diagram with sources, transformations, state, and sinks.
13. Document every output grain and business key.
14. Publish exact batch revenue and return reconciliation evidence.
15. Map streamed purchase order_ids to batch orders and classify unmatched records.
16. Include the demand-model comparison with its chronological split and baseline.
17. Write reproducible initial-load and stream-start commands.
18. Demonstrate two arrival batches, a duplicate, a late event, and a restart.
19. Package meaningful tests and saved progress evidence.
20. Prepare a ten-minute walkthrough of the complete platform.

### Advanced challenges (21-30)

21. Design a historical backfill that does not corrupt current stream state or output.
22. Explain reconciliation differences caused by status, contents, timing, and returns.
23. Propose partition and file layouts for one million daily events.
24. Estimate bottlenecks from measured workload characteristics rather than guessing executor counts.
25. Define freshness, correctness, and recovery objectives for each output.
26. Design failure handling for source loss, corrupted checkpoint, and partial sink commits.
27. Compare a local Parquet publication design with a transactional production sink.
28. Define access controls and retention for customer fields and audit records.
29. Explain tradeoffs between latency, state size, replayability, and reporting finality.
30. Perform a final design review with test evidence, operational risks, and a prioritized improvement plan.


## Completion checks

Deliver reproducible code, tests, screenshots or saved progress, reconciliation report, and a ten-minute walkthrough; explain every known limitation.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-30/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-30/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day30/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-30/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
