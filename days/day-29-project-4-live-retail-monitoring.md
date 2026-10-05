# Day 29: Project 4 - Live retail monitoring

Suggested date: 2026-11-03. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

end-to-end streaming; alerts; metrics; replay testing; service objectives.

## Before you begin

Complete Day 28; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Build purchase-event ingestion, validation, bounded deduplication, and product enrichment.
2. Produce five-minute counts and revenue with a documented lateness policy.
3. Build a separate alert query for event basket amounts above 10000.
4. Persist output and track inputRowsPerSecond, processedRowsPerSecond, watermark, and state rows.
5. Test duplicate events, malformed events, delayed events, and restart recovery with a runbook.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Use separate queries/checkpoints for aggregated metrics and event alerts.
# Define alert ID from event_id and rule version.
```

## More examples to solve

1. An alert batch is replayed: avoid duplicate notification records. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. One hot customer overwhelms a partition. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. No incoming events: distinguish silence from query failure. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. Which components are needed for a live retail monitor?
2. What makes a streaming metric provisional?
3. Why validate events before computing business metrics?
4. Why deduplicate purchase events before calculating revenue?
5. What is an alert rule?
6. Why should alerts have a stable identity?
7. What does inputRowsPerSecond describe?
8. What does processedRowsPerSecond describe?
9. Why monitor watermark and state-row counts?
10. Why does absence of incoming events not automatically mean failure?

### Hands-on questions (11-20)

11. Build event ingestion with explicit schema and audit metadata.
12. Quarantine invalid timestamps and empty purchase baskets.
13. Deduplicate valid events within the defined delay horizon.
14. Enrich valid purchase items with a unique static dimension.
15. Produce five-minute purchase counts and event revenue.
16. Create a separate high-value-basket alert query.
17. Generate a basket above 10000 to test the alert path.
18. Save local alert records using event_id and rule version as identity.
19. Collect progress snapshots and input-to-output reconciliation counts.
20. Demonstrate stop-and-restart recovery with retained checkpoints.

### Advanced challenges (21-30)

21. Replay an alert-producing event and verify your defined duplicate behavior.
22. Compare provisional window output with finalized append output.
23. Create a delayed event and explain whether the metric or alert should change.
24. Design monitoring thresholds for lag, failures, state growth, and source silence.
25. Identify hot-key bottlenecks without changing monetary correctness.
26. Define alert sink idempotence independently from query checkpoint recovery.
27. Design a raw-event replay path for events excluded by the online lateness policy.
28. Document why batch booked revenue cannot be directly equated to simulated event revenue.
29. Separate metrics and alerts into compatible query plans with independent checkpoints.
30. Deliver a live-monitor runbook covering bad input, duplicates, late data, sink failure, and recovery.


## Completion checks

Alert records are saved locally rather than sent; demonstrate replay behavior and bounded state on a controlled fixture.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-29/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-29/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day29/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-29/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
