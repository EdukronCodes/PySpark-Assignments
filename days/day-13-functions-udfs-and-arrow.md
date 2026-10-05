# Day 13: Functions, UDFs, and Arrow

Suggested date: 2026-10-18. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

built-in expressions; Python UDF; pandas UDF; serialization; benchmarking.

## Before you begin

Complete Day 12; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Build a reusable expression for basket bands.
2. Implement equivalent Python UDF and compare results on boundary and null values.
3. Benchmark both on a scaled dataset with a forced action.
4. Optionally implement a pandas UDF in a separately compatible Arrow environment.
5. Explain serialization and why built-ins are the default.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
def basket_band(c):
    return F.when(c.isNull(), "unknown").when(c < 500, "low").when(c < 2000, "medium").otherwise("high")
```

## More examples to solve

1. Band for exactly 500 and 2000. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Normalize email with built-ins. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. A UDF throws on null: reproduce and repair. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a built-in Spark column expression?
2. What is a Python UDF?
3. What must a Python UDF declare about its output?
4. Why can Python serialization affect UDF performance?
5. What is a pandas UDF intended to process?
6. What role does Arrow play in data transfer?
7. Why prefer built-ins for common string and numeric operations?
8. How should basket bands handle null amounts?
9. Why must benchmarks include an action?
10. Why are compatible pandas and Arrow versions important?

### Hands-on questions (11-20)

11. Implement basket bands using when expressions.
12. Implement an equivalent ordinary Python UDF.
13. Check bands for 499.99, 500, 1999.99, and 2000.
14. Check null amounts in both implementations.
15. Normalize emails with built-ins and compare with a Python implementation.
16. Inspect plans for built-in and Python UDF versions.
17. Benchmark both implementations on the same scaled input.
18. Repeat timings three times after an initial warm-up.
19. Optionally implement a pandas UDF in a compatible separate environment.
20. Document dependency versions and action results for every benchmark.

### Advanced challenges (21-30)

21. Explain why a count action may prune a computed UDF column from execution.
22. Choose an action that forces evaluation of the benchmarked output column.
23. Reproduce a null-handling UDF error and repair it.
24. Explain why nondeterministic UDFs need explicit care in repeated computations.
25. Compare row-at-a-time Python UDFs with vectorized pandas UDFs.
26. Explain why vectorization does not remove every serialization or memory cost.
27. Avoid external network calls inside a per-row UDF; propose a join-based alternative.
28. Test return-type mismatches and document observed behavior.
29. Design a UDF review checklist covering types, nulls, determinism, and dependency distribution.
30. Replace a complex UDF with composable built-ins and compare correctness and plans.


## Completion checks

Results match on all boundary fixtures; timing includes an action and environment details.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-13/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-13/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day13/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-13/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
