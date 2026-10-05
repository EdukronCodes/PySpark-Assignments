# Day 24: Streaming deduplication and enrichment

Suggested date: 2026-10-29. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

dropDuplicatesWithinWatermark; bounded state; stream-static joins; dimension freshness.

## Before you begin

Complete Day 23; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Deduplicate event_id with a ten-minute event-time watermark.
2. Explode purchase items and join to a static unique product dimension.
3. Compute per-event basket amount with the supplied price fields.
4. Count the repeated E0001 event once within the watermark horizon.
5. Change a product attribute and document when the static snapshot becomes visible.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
unique_events = stream.withWatermark("event_time", "10 minutes").dropDuplicatesWithinWatermark(["event_id"])
# Introduced in Spark 3.5; keep this curriculum on its pinned version.
```

## More examples to solve

1. Same ID appears with a different timestamp within the delay. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Duplicate arrives after state eviction. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Unknown product in a purchase event. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. Why can a streaming source contain duplicate business events?
2. What is the event deduplication key?
3. What does dropDuplicatesWithinWatermark provide?
4. Why does bounded deduplication need event-time information?
5. How is bounded deduplication different from permanent uniqueness?
6. What is a stream-static join?
7. Why must the static product key be unique?
8. Why retain event_id after exploding purchase items?
9. How does purchase-event revenue differ from batch booked revenue?
10. What is dimension freshness in a streaming application?

### Hands-on questions (11-20)

11. Deduplicate event_id using the supplied ten-minute watermark.
12. Publish the repeated E0001 event within the tested delay horizon.
13. Verify the controlled duplicate is counted once.
14. Explode valid purchase items and enrich them with static product attributes.
15. Compute item amounts from event-supplied prices rather than current catalog prices.
16. Preserve unmatched product keys in an audit output.
17. Test static dimension duplication and its effect on streamed amounts.
18. Create an event with a known product and an unknown product.
19. Document the product snapshot loaded by the query.
20. Verify event-level purchase counts are not replaced by item counts.

### Advanced challenges (21-30)

21. Send the same event_id with a slightly different timestamp inside the horizon.
22. Advance event time, then test an old duplicate after state eviction.
23. Explain why deduplicating only event_id without a bound can grow state indefinitely.
24. Compare duplicate business events with duplicated file publication.
25. Define whether to reject or preserve conflicting payloads sharing an event_id.
26. Test invalid timestamps before stateful deduplication.
27. Design per-event basket calculations using higher-order functions without an unbounded event-id aggregation.
28. Change a static dimension and document whether the running query observes the change.
29. Propose a historical-price enrichment strategy for changing catalog data.
30. Write a deduplication contract stating horizon, key, conflict policy, and replay limitations.


## Completion checks

Controlled in-horizon duplicates are removed; explain why bounded deduplication is not permanent uniqueness.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-24/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-24/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day24/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-24/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
