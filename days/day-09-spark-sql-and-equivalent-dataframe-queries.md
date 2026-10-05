# Day 09: Spark SQL and equivalent DataFrame queries

Suggested date: 2026-10-14. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

temporary views; SQL expressions; CTEs; subqueries; explain.

## Before you begin

Complete Day 08; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Register clean facts and dimensions as temporary views.
2. Write revenue by category in SQL and DataFrame API.
3. Use a CTE for completed order totals and filter above-average orders.
4. Use CASE for basket bands.
5. Compare query plans and explain why SQL and DataFrame results match.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
clean_lines.createOrReplaceTempView("clean_lines")
spark.sql("SELECT order_id, COUNT(*) AS lines FROM clean_lines GROUP BY order_id").show()
```

## More examples to solve

1. Find customers ordering from two cities. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Use EXISTS or a semi join for repeat shoppers. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Compare SQL NULL behavior with Python None. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a temporary view, and how long does it exist?
2. How do you register a DataFrame as a SQL view?
3. What is a SQL common table expression?
4. How does WHERE differ from HAVING?
5. What does CASE WHEN represent?
6. How does SQL treat comparisons with NULL?
7. Why should SQL reports select explicit columns?
8. What does ORDER BY guarantee about displayed results?
9. How do DataFrame and SQL operations use Spark's query engine?
10. What is the difference between an aggregate query and a row filter?

### Hands-on questions (11-20)

11. Write category revenue SQL over enriched completed lines.
12. Write its equivalent DataFrame transformation.
13. Use a CTE to compute order totals.
14. Find orders whose value exceeds the average completed-order value.
15. Use CASE WHEN to create basket bands.
16. Use HAVING to retain categories with revenue above a chosen threshold.
17. Find repeat customers using SQL distinct order counts.
18. Find products never sold using NOT EXISTS or an anti join.
19. Query cancelled-order rates by channel with an explicit denominator.
20. Compare ordered SQL and DataFrame results on a fixture.

### Advanced challenges (21-30)

21. Show how NOT IN with a null-containing subquery can produce surprising output.
22. Replace an unsafe NOT IN query with a correctly defined NOT EXISTS query.
23. Use EXPLAIN to compare SQL and DataFrame physical plans.
24. Explain why equivalent SQL strings may have different logical plans before optimization.
25. Create a correlated-subquery example and verify support in the pinned Spark version.
26. Avoid double-counting order totals when SQL joins order and line grains.
27. Demonstrate SQL three-valued logic with true, false, and null predicates.
28. Parameterize a date filter without inserting untrusted text into SQL expressions.
29. Design equality checks that handle nulls, decimals, and duplicate rows.
30. Write a SQL report with three CTEs and document each intermediate grain.


## Completion checks

Both APIs yield equal rows and schemas after deterministic ordering.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-09/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-09/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day09/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-09/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
