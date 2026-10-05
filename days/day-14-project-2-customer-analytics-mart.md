# Day 14: Project 2 - Customer analytics mart

Suggested date: 2026-10-19. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

RFM; star schema; cohorts; reusable transformations; reconciliation.

## Before you begin

Complete Day 13; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Build fact_order and fact_line with customer, product, and store dimensions.
2. Calculate recency as of 2026-10-01, completed-order frequency, and booked monetary value.
3. Create documented RFM bands and customer segments.
4. Publish cohort retention and category preferences.
5. Reconcile all mart revenue with Project 1 and explain differences if any.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# Keep customer-level RFM separate from line-level category preferences.
# Use a fixed as-of date to make results reproducible.
```

## More examples to solve

1. Compare a recent low-spend buyer with a dormant high-spend buyer. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Customer has only cancelled orders. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Verify adding product attributes does not multiply revenue. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is the grain of fact_order?
2. What is the grain of fact_line?
3. What does a dimension table add to a fact table?
4. What do recency, frequency, and monetary represent?
5. Why fix an as-of date for RFM analysis?
6. Why should frequency count distinct orders?
7. Which statuses are included in customer monetary value?
8. How should customers without completed purchases appear?
9. What is the grain of a cohort retention result?
10. Why keep category preferences separate from customer-level RFM?

### Hands-on questions (11-20)

11. Build a unique fact_order table with completed-order totals.
12. Build a unique fact_line table with product and order keys.
13. Validate all dimension keys before mart joins.
14. Calculate recency as of 2026-10-01.
15. Calculate completed-order frequency and booked monetary value.
16. Define transparent RFM bands using documented thresholds.
17. Create customer segments from those bands.
18. Calculate each customer's highest-revenue category.
19. Publish month-0 and month-1 retention from purchase cohorts.
20. Reconcile mart monetary totals with Project 1 revenue.

### Advanced challenges (21-30)

21. Test a customer with only cancelled orders.
22. Test a customer with three lines in one completed order.
23. Resolve category-preference ties with a deterministic rule.
24. Compare fixed bands with quantile-based RFM bands and explain small-sample limitations.
25. Explain why customer-level monetary values inflate when joined repeatedly to line facts.
26. Add a dimension attribute and prove it does not change facts or totals.
27. Design separate semantics for return-adjusted monetary value.
28. Create a customer-segment change report across two as-of dates.
29. Design a mart contract covering key uniqueness and time definitions.
30. Prepare a customer-analysis walkthrough with fixtures and exact reconciliation.


## Completion checks

Fact grains are unique, RFM frequency counts orders, and revenue reconciles exactly.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-14/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-14/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day14/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-14/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
