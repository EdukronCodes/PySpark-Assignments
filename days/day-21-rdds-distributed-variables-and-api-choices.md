# Day 21: RDDs, distributed variables, and API choices

Suggested date: 2026-10-26. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

RDD; map; flatMap; reduceByKey; partitions; broadcast variables; accumulators; pandas API; Connect.

## Before you begin

Complete Day 20; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Convert a tiny line subset to RDD and compute category quantities with reduceByKey.
2. Compare RDD and DataFrame plans and results.
3. Broadcast a tiny lookup dictionary and use it in an RDD map.
4. Use an accumulator for diagnostics and explain retry overcount risk.
5. Compare DataFrame, pandas API on Spark, and Spark Connect architecture in a short decision note.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
pairs = clean_lines.select("product_id", "quantity").rdd.map(lambda r: (r.product_id, r.quantity))
totals = pairs.reduceByKey(lambda a, b: a + b)
```

## More examples to solve

1. Word count over product names. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. groupByKey versus reduceByKey. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Explain why Python has no typed JVM Dataset API. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is an RDD?
2. How does an RDD differ from a DataFrame?
3. What does RDD map return?
4. How does flatMap differ from map?
5. What is a key-value pair RDD?
6. What does reduceByKey compute?
7. What is a broadcast variable used for?
8. What is an accumulator used for?
9. Why is the DataFrame API usually preferred for structured retail data?
10. Why is the JVM typed Dataset API not a Python DataFrame feature?

### Hands-on questions (11-20)

11. Convert a tiny product-quantity DataFrame to a pair RDD.
12. Sum quantities by product using reduceByKey.
13. Compute the same totals with DataFrame groupBy.
14. Compare RDD and DataFrame totals after deterministic sorting.
15. Build a word count over product names using flatMap.
16. Broadcast a tiny product-category dictionary for an RDD lookup.
17. Use mapPartitions for a partition-level diagnostic.
18. Add an accumulator for a nonfinancial diagnostic counter.
19. Inspect RDD partition counts and lineage.
20. Write a short comparison of DataFrames, pandas API on Spark, and Spark Connect.

### Advanced challenges (21-30)

21. Compare groupByKey and reduceByKey shuffle behavior for summation.
22. Explain the associativity and commutativity assumptions of distributed reductions.
23. Show why floating-point reductions can vary with reduction order.
24. Explain how task retries or repeated actions can make accumulator totals unsuitable for revenue.
25. Distinguish a Spark broadcast variable from a SQL broadcast join hint.
26. Explain serialization risks when an RDD closure captures a large Python object.
27. Compare partition-wise initialization with per-row initialization of a lookup resource.
28. Explain why Spark Connect does not expose every classic RDD/SparkContext workflow.
29. Design a decision rule for choosing DataFrame expressions over custom RDD logic.
30. Produce a small equivalent RDD/DataFrame implementation with correctness and API tradeoffs.


## Completion checks

RDD and DataFrame totals agree; accumulators are never used as authoritative financial totals.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-21/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-21/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day21/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-21/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
