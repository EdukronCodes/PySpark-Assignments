# Day 12: Nested JSON and complex types

Suggested date: 2026-10-17. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

arrays; structs; maps; explode_outer; from_json; higher-order functions.

## Before you begin

Complete Day 11; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Read events with the supplied explicit nested schema.
2. Explode items while retaining event_id and event_time.
3. Extract device metadata and map attributes.
4. Sum basket quantities using higher-order functions.
5. Compare explode and explode_outer for empty and null arrays.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
events = spark.read.schema(event_schema).json("data/events_archive/batch_001.json")
flat = events.select("event_id", "event_time", F.explode_outer("items").alias("item"))
```

## More examples to solve

1. An event has two products: expect two flattened rows. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Purchase event has no items: quarantine it. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Access campaign from an attribute map with a default. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a struct column?
2. What is an array column?
3. What is a map column?
4. How do you access a nested struct field?
5. How do you retrieve a value from a map?
6. What does explode do to row count?
7. How does explode_outer treat empty or null arrays?
8. What does from_json require besides a JSON string?
9. Why preserve event_id when flattening items?
10. How is an empty purchase basket different from a valid view event?

### Hands-on questions (11-20)

11. Read batch_001.json using the explicit nested schema.
12. Select event_id and device.os without flattening other fields.
13. Extract campaign from the attributes map.
14. Explode purchase items into one row per event item.
15. Calculate item amount from nested quantity and price.
16. Count items per event before and after flattening.
17. Use a higher-order function to calculate basket quantities.
18. Create empty-array and null-array fixtures and compare explode variants.
19. Reconstruct an items array from flattened rows using a documented ordering key.
20. Identify malformed or empty purchase events for quarantine.

### Advanced challenges (21-30)

21. Show why exploding two independent arrays can create a Cartesian multiplication.
22. Use arrays_zip for paired arrays and define behavior for unequal lengths.
23. Preserve item position with posexplode when order matters.
24. Compare higher-order expressions with a Python UDF for array calculations.
25. Parse JSON missing a nested field and record the resulting null behavior.
26. Handle an unknown map key without replacing valid values.
27. Validate each item rather than only checking that the basket array exists.
28. Create one basket containing both valid and invalid items and define rejection policy.
29. Compare event-level and item-level counts to avoid inflated purchase metrics.
30. Write a flattening function with fixtures for null, empty, and multiple-item baskets.


## Completion checks

Flattening counts match sum of item lengths; empty-item handling is explicitly documented.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-12/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-12/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day12/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-12/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
