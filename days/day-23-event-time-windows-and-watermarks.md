# Day 23: Event time, windows, and watermarks

Suggested date: 2026-10-28. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

event time vs processing time; tumbling/sliding windows; state cleanup; output modes.

## Before you begin

Complete Day 22; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Aggregate purchase-event counts into five-minute event-time windows.
2. Set a ten-minute watermark and use append output.
3. Publish batches in numeric order and inspect eventTime watermark and state metrics.
4. Compare append and update console output on a separate checkpoint.
5. Explain why final windows may need newer events and a later micro-batch to emit.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
counts = stream.withWatermark("event_time", "10 minutes").groupBy(F.window("event_time", "5 minutes")).count()
```

## More examples to solve

1. An event arrives six minutes late. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. An event arrives thirty minutes late. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Compare 5-minute tumbling with 10-minute windows sliding every 5 minutes. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is event time?
2. What is processing time?
3. What is a tumbling event-time window?
4. What is a sliding window?
5. What does withWatermark declare?
6. Why must event_time be parsed as a timestamp?
7. What state does a windowed count retain?
8. How do append and update modes differ for aggregations?
9. Why might a finalized window not appear immediately?
10. Why is a watermark not a fixed wall-clock lateness cutoff?

### Hands-on questions (11-20)

11. Count purchase events in five-minute event-time windows.
12. Add a ten-minute event-time watermark before aggregation.
13. Publish batches in order, waiting for each to finish.
14. Save eventTime watermark values from query progress.
15. Compare a controlled on-time and six-minute-late event.
16. Publish a much older event after advancing event time.
17. Compare five-minute tumbling windows with ten-minute windows sliding every five minutes.
18. Test events exactly at 10:00, 10:04:59, and 10:05 window boundaries.
19. Run separate append and update experiments with separate checkpoints.
20. Inspect retained-state and dropped-by-watermark metrics where available.

### Advanced challenges (21-30)

21. Explain why newer data and a subsequent micro-batch can be needed for final output.
22. Predict windows receiving one event in a sliding-window query.
23. Explain why summing sliding-window counts double-counts events across overlapping windows.
24. Test a future-dated outlier and discuss its effect on watermark advancement.
25. Explain the guarantee for within-delay data versus possible dropping beyond the delay.
26. Compare watermark placement before and after aggregation and verify supported usage.
27. Define a business policy for events arriving after finalization.
28. Estimate state size as a function of keys, windows, and delay threshold.
29. Design controlled late-data tests independent of real wall-clock waiting.
30. Publish a lateness report with event timestamps, arrival batches, watermarks, and observed outputs.


## Completion checks

A tiny controlled fixture proves window boundaries; explain that data beyond the watermark may be dropped, while data within the delay is protected.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-23/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-23/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day23/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-23/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
