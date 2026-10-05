# Day 04: Cleaning and quarantine

Suggested date: 2026-10-09. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

trim; lower; coalesce; null handling; rule-based validation; audit reasons.

## Before you begin

Complete Day 03; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Normalize city and email casing without changing IDs.
2. Reject nonpositive quantity, missing IDs, negative price, and discounts outside [0,1].
3. Flag unknown product IDs by anti join.
4. Add an array of all rejection reasons per row.
5. Write clean and quarantine Parquet outputs and a rule-count report.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
invalid_qty = F.col("quantity").isNull() | (F.col("quantity") <= 0)
# Combine rules explicitly; null comparisons alone do not reject null values.
```

## More examples to solve

1. Compare filling a missing email with rejecting a missing ID. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. A row fails two rules: retain both reasons. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Distinguish blank strings from null. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a quarantine dataset used for?
2. How does a parse error differ from an invalid business value?
3. Why normalize email and city values?
4. What do trim and lower do?
5. What does coalesce return when several columns are null?
6. Why is a missing email allowed but a missing line_id rejected?
7. What is a referential-integrity violation?
8. Why retain more than one rejection reason per row?
9. What is the accepted-row grain before deduplication?
10. Why preserve original values alongside cleaned values?

### Hands-on questions (11-20)

11. Normalize customer email and city without changing IDs.
12. Flag null and blank line_id values using a tiny fixture.
13. Reject nonpositive quantities and negative prices.
14. Reject missing discounts and values outside the inclusive valid range.
15. Find unknown product IDs with a left anti join.
16. Find unknown order IDs independently of product validation.
17. Build an array containing every applicable rejection reason.
18. Write accepted and quarantined rows to separate Parquet paths.
19. Produce rejected-row counts for each rule.
20. Verify that raw rows equal accepted-before-dedup plus quarantined rows.

### Advanced challenges (21-30)

21. Create a row violating quantity, price, and product rules simultaneously.
22. Explain why summing per-rule rejection counts can exceed the quarantine row count.
23. Design mutually exclusive severity categories without losing detailed reasons.
24. Detect text that failed numeric casting rather than confusing it with original null.
25. Explain how SQL three-valued logic can accidentally admit invalid rows.
26. Test all-valid, all-invalid, and empty input DataFrames.
27. Preserve source-file metadata so a quarantined line can be traced to its origin.
28. Define a maximum rejection threshold and a pipeline failure policy.
29. Design a correction-and-reprocessing workflow that preserves the original audit.
30. Implement a reusable validator returning accepted rows, quarantine rows, and metrics.


## Completion checks

Every raw line is assigned to exactly one clean or quarantine output before duplicate removal.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-04/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-04/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day04/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-04/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
