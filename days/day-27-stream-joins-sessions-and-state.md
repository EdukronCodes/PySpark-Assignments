# Day 27: Stream joins, sessions, and state

Suggested date: 2026-11-01. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

stream-stream joins; time bounds; multiple watermarks; session_window; state growth.

## Before you begin

Complete Day 26; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Read purchase events and payment events as two independent streams.
2. Watermark both and join by order_id with payment time between purchase time and 15 minutes later.
3. Use append mode and inspect bounded state across newer batches.
4. Build a separate session-window query over customer activity with a ten-minute gap.
5. Discuss custom state APIs, RocksDB state store, and timeout requirements as advanced extensions.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Use aliases p and pay, equality on order_id, and explicit timestamp range.
# Separate checkpoint paths for the join and session-window queries.
```

## More examples to solve

1. Payment arrives before purchase in processing time. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Payment timestamp is outside the time bound. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Unmatched purchase in a left outer join: explain delayed null emission. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a stream-stream join?
2. How does a stream-stream join differ from a stream-static join?
3. Why do streaming joins retain state?
4. What is a time-bounded join condition?
5. Why watermark both inputs in the bounded join lab?
6. What is a session window?
7. What does a ten-minute session gap mean?
8. Why can unmatched outer-join rows be delayed?
9. How does processing-order arrival differ from event-time matching?
10. What is the purpose of a state store?

### Hands-on questions (11-20)

11. Read purchase and payment events from independent input directories.
12. Parse and validate both event-time columns.
13. Join purchases and payments by order_id with the required fifteen-minute time bound.
14. Publish a matching purchase and payment fixture.
15. Publish a payment outside the matching event-time range.
16. Publish a payment before its purchase in processing order.
17. Inspect join state rows after successive batches.
18. Advance event time on both inputs and inspect cleanup behavior.
19. Build a separate customer session-window aggregation.
20. Test activity separated by gaps smaller and larger than ten minutes.

### Advanced challenges (21-30)

21. Explain how Spark's multiple-watermark policy affects a slow input.
22. Compare minimum and maximum watermark policies and their late-data tradeoffs.
23. Design a left outer join fixture demonstrating delayed unmatched output.
24. Explain why equality on order_id alone can allow unbounded state.
25. Predict a many-to-many output when an order has several payment events.
26. Design payment deduplication before joining without unsupported stateful chaining assumptions.
27. Explain session merging when a late event bridges two previously separate sessions.
28. Discuss RocksDB state-store benefits and deployment-specific memory considerations.
29. Sketch a custom per-customer state machine with a timeout and bounded-state policy.
30. Deliver independent join and session experiments with checkpoint paths and state-growth evidence.


## Completion checks

A synthetic matched/unmatched fixture proves join results; state cleanup requires advancing event time on both inputs.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-27/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-27/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day27/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-27/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
