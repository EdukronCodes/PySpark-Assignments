# Day 03: Filtering, expressions, and retail amounts

Suggested date: 2026-10-08. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

select; filter; withColumn; when; cast; DecimalType; null semantics.

## Before you begin

Complete Day 02; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Build line_gross = quantity * unit_price and line_net = line_gross * (1 - discount_pct).
2. Use decimal arithmetic and round each line to two places.
3. Select positive-quantity lines with a discount between zero and one.
4. Classify line_net below 500 as low, 500 through 1999.99 as medium, otherwise high.
5. Compare isNull() with equality to None.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
lines = spark.read.option("header", True).csv("data/raw/order_items.csv")
lines = lines.withColumn("quantity", F.col("quantity").cast("int"))
# Cast both monetary columns to suitable decimals before computing amounts.
```

## More examples to solve

1. Find lines with net amount above 2000. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Apply a 10% discount to a synthetic 2 x 500 line. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Show how negative quantity affects revenue. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. How does select differ from withColumn?
2. How do you refer to a column using functions.col?
3. What does cast change about a column?
4. Why must CSV quantity be typed before arithmetic?
5. How do filter and where relate?
6. How do you combine column conditions using & and |?
7. Why are parentheses needed around combined comparisons?
8. What does when(...).otherwise(...) express?
9. How does isNull differ from comparing a column to None?
10. How are line gross and line net defined in this course?

### Hands-on questions (11-20)

11. Calculate net value for quantity 2, price 500, and discount 0.10.
12. Create decimal quantity-price-discount calculations for all line items.
13. Round line net to two decimal places using the course rounding rule.
14. Filter positive quantities with discount_pct between zero and one inclusive.
15. Classify amounts below 500, below 2000, and all remaining amounts.
16. Find lines with net amount greater than 2000.
17. Select only line_id and computed amounts without modifying raw columns.
18. Create fixtures for discounts 0, 1, -0.1, and 1.1.
19. Compare filtering null quantities with isNull and a numeric comparison.
20. Create a named reusable expression for net line amount.

### Advanced challenges (21-30)

21. Compare rounding each line before aggregation with rounding only the final total.
22. Demonstrate half-up rounding and explain how bround differs on a tie.
23. Create an overflow fixture and document behavior with ANSI mode enabled and disabled.
24. Explain the precision and scale of intermediate decimal multiplication.
25. Handle null price and discount explicitly without silently treating them as zero.
26. Test classification at 499.99, 500.00, 1999.99, and 2000.00.
27. Explain why a negative quantity must not become a negative sale in this dataset.
28. Compare built-in column expressions with a Python loop over collected rows.
29. Inspect whether chained projections are simplified in the optimized plan.
30. Write a calculation function and expected-output checks for all boundary cases.


## Completion checks

A 2 x 500 line with discount 0.10 has net amount 900.00; invalid discounts are excluded.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-03/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-03/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day03/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-03/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
