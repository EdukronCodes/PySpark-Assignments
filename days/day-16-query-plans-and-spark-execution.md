# Day 16: Query plans and Spark execution

Suggested date: 2026-10-21. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

Catalyst; physical plans; stages; jobs; shuffle; narrow and wide transformations.

## Before you begin

Complete Day 15; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Use explain("formatted") for filter, join, and aggregation queries.
2. Identify exchanges and scan filters.
3. Inspect local Spark UI after running an action.
4. Compare projection before and after a join.
5. Explain driver memory risks, task execution, and lazy recomputation.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
enriched.groupBy("category").agg(F.sum("line_net")).explain("formatted")
```

## More examples to solve

1. Filter then groupBy: identify shuffle boundary. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Sort globally versus sortWithinPartitions. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Use count after repartition: identify stages. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a logical query plan?
2. What is a physical query plan?
3. What does Catalyst optimize?
4. What is a Spark job?
5. What is a Spark stage?
6. What is a task?
7. What is a shuffle?
8. How do narrow and wide transformations differ?
9. Why does an action trigger distributed execution?
10. What information does the Spark UI provide?

### Hands-on questions (11-20)

11. Save explain('formatted') output for a filtered scan.
12. Save a physical plan for a grouped revenue query.
13. Identify exchange operators in an aggregation plan.
14. Inspect a join plan and identify its join operator.
15. Compare plans before and after selecting only required columns.
16. Run an action and inspect its jobs and stages in the UI.
17. Compare global orderBy with sortWithinPartitions.
18. Inspect the number of partitions before and after repartition.
19. Identify scan filters and projected columns in a Parquet plan.
20. Annotate a plan with scan, filter, exchange, join, and aggregation nodes.

### Advanced challenges (21-30)

21. Explain how partial aggregation reduces shuffle data volume.
22. Distinguish the initial and final adaptive execution plans.
23. Explain why a single action can create several jobs.
24. Trace why repeated uncached actions can recompute the same transformations.
25. Compare a broadcast exchange with a shuffle exchange.
26. Identify a potential single-partition bottleneck in a window query.
27. Explain driver-memory risk in collecting a large aggregation result.
28. Predict which operations in a multi-step pipeline cause shuffles and verify.
29. Diagnose a slow stage using task duration, input size, and spill metrics.
30. Write a plan-based optimization note with evidence rather than guessed speedups.


## Completion checks

A saved plan is annotated with scan, exchange, join, and aggregate nodes.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-16/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-16/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day16/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-16/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
