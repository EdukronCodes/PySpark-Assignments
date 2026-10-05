# Day 06: Aggregations and business metrics

Suggested date: 2026-10-11. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

groupBy; agg; countDistinct; conditional aggregation; denominator definitions.

## Before you begin

Complete Day 05; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Aggregate net line amounts to one row per order.
2. Join order status and include only completed orders in booked revenue.
3. Compute revenue, distinct orders, and average order value by store.
4. Calculate cancellation rate using all orders as denominator.
5. Compute channel revenue shares and verify they sum to one.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
order_totals = clean_lines.groupBy("order_id").agg(F.sum("line_net").alias("order_net"))
```

## More examples to solve

1. Compare count(*) and count(customer_id). Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Store with no completed orders: define AOV as null. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Compare average line value with average order value. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What does groupBy define about an aggregation's output grain?
2. How do count and countDistinct differ?
3. How does count(column) treat null values?
4. Why should AOV use orders rather than lines as its denominator?
5. Which order status contributes to booked revenue?
6. What is cancellation rate's denominator?
7. What does sum do when all values are null?
8. Why can revenue share be different from order-count share?
9. When should an undefined ratio be null rather than zero?
10. Why aggregate lines to order grain before calculating order averages?

### Hands-on questions (11-20)

11. Sum clean line_net by order_id.
12. Calculate booked revenue for completed orders only.
13. Compute store revenue and distinct completed-order counts.
14. Calculate store AOV from revenue and completed-order count.
15. Calculate cancellation rate at order grain.
16. Compute channel revenue shares and verify their total.
17. Count orders containing more than three accepted lines.
18. Find the highest-revenue product by units and by money.
19. Use conditional aggregation for completed and cancelled order counts.
20. Reconcile summed store revenue with global booked revenue.

### Advanced challenges (21-30)

21. Create a store with no completed orders and define its output metrics.
22. Explain why averaging store AOV values does not produce global AOV.
23. Reconstruct global AOV using correctly weighted store metrics.
24. Compare count(*) and count(customer_id) on a null-containing fixture.
25. Show how joining order totals back to lines can duplicate order-level revenue.
26. Define how an order with all lines rejected affects AOV and quality metrics.
27. Compare approximate distinct counting with exact counts for financial reporting.
28. Design a revenue reconciliation with decimal precision rather than floating tolerance.
29. Inspect the shuffle introduced by grouping and explain its key distribution.
30. Write a metric-definition document and independent fixture checks.


## Completion checks

Global booked revenue equals the sum of store revenue; AOV equals revenue divided by distinct completed orders.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-06/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-06/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day06/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-06/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
