# Day 17: Performance, skew, and caching

Suggested date: 2026-10-22. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

broadcast joins; AQE; repartition; coalesce; persist; skew; benchmark discipline.

## Before you begin

Complete Day 16; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Generate at least 100000 synthetic lines with unique IDs for performance practice.
2. Compare broadcast and non-broadcast product joins.
3. Benchmark uncached and cached repeated aggregations and unpersist afterward.
4. Create a hot product key and inspect partition imbalance.
5. Try salting a skewed aggregation and compare totals; record AQE settings.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
joined = large_lines.join(F.broadcast(products), "product_id")
# Use repeatable inputs and the same actions in each timing run.
```

## More examples to solve

1. Broadcast a tiny product dimension. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Too many partitions for a tiny dataset. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Cache once but never reuse: explain wasted cost. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a broadcast join?
2. When is broadcasting a dimension reasonable?
3. What is Adaptive Query Execution?
4. What is data skew?
5. What does persist retain for reuse?
6. Why call unpersist after repeated work?
7. Why can too many shuffle partitions hurt tiny workloads?
8. How does coalesce differ from a full repartition shuffle?
9. Why should benchmark results include input size?
10. Why do local timings not directly predict cluster performance?

### Hands-on questions (11-20)

11. Generate at least 100000 synthetic lines with unique IDs.
12. Join a small product dimension using an explicit broadcast hint.
13. Compare its plan with a non-broadcast join plan.
14. Benchmark repeated aggregations without caching.
15. Cache the reused input, materialize it, and repeat the benchmark.
16. Unpersist cached input and verify your cleanup code runs.
17. Create a hot product key holding most rows.
18. Measure row counts per partition for the skewed dataset.
19. Compare three shuffle partition settings on identical inputs.
20. Record median action-based runtimes over three measured runs.

### Advanced challenges (21-30)

21. Salt a skewed aggregation and recombine partial totals correctly.
22. Explain why salting a join requires careful duplication or mapping of the other side.
23. Test that optimization preserves exact revenue and business keys.
24. Inspect AQE settings and compare initial versus final join choices.
25. Explain broadcast memory costs on the driver and executors.
26. Compare cache benefits when an input is reused once versus five times.
27. Prevent a benchmark action from pruning the computation being measured.
28. Diagnose whether long tasks indicate skew, spill, or expensive per-row logic.
29. Design a larger benchmark that separates read time from transformation time.
30. Produce a performance report with correctness checks, settings, and limitations.


## Completion checks

Optimizations preserve results; report median of three action-based runs and avoid claiming local timings predict cluster speed.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-17/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-17/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day17/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-17/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
