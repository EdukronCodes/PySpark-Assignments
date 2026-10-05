# Day 05: Deduplication and deterministic records

Suggested date: 2026-10-10. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Beginner.

## Goal and concepts

distinct; dropDuplicates; composite keys; window ordering; data grain.

## Before you begin

Complete Day 04; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Declare grains for orders, lines, customers, products, stores, and returns.
2. Identify duplicated line_id values and compare entire-row duplicates.
3. Keep one line per line_id using source ordering or a documented stable tie-break.
4. Create a changed duplicate and explain why arbitrary dropDuplicates is insufficient.
5. Publish deduplicated lines for later days.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
w = Window.partitionBy("line_id").orderBy(F.col("order_id"), F.col("product_id"))
# This tie-break is adequate only for identical duplicates in the supplied data.
```

## More examples to solve

1. Two different lines share order_id: keep both. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Same customer has updated email: choose latest update. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. A duplicate has equal timestamps: define a tie-break. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is the difference between a business key and an entire-row duplicate?
2. Why is order_id not unique in order_items?
3. What is the business key of an order line?
4. How does distinct differ from dropDuplicates on selected columns?
5. Why must cleaning happen before canonical line deduplication?
6. What makes a deduplication rule deterministic?
7. What does row_number assign within a window partition?
8. Why does a timestamp alone sometimes fail as a tie-break?
9. Why preserve removed duplicate rows?
10. When might two rows with one line_id represent a correction rather than an exact duplicate?

### Hands-on questions (11-20)

11. Count exact duplicate raw line rows.
12. Find line_id values appearing more than once.
13. Verify that supplied valid duplicate additions total eight rows.
14. Keep one accepted row per line_id and verify uniqueness.
15. Compare distinct with dropDuplicates(['order_id']) and explain the lost lines.
16. Build a fixture with two different lines belonging to one order.
17. Create a changed duplicate with a newer updated_at value.
18. Choose the newest correction using a window and stable tie-break.
19. Save discarded rows with the winning line_id for audit.
20. Check raw = quarantine + removed duplicates + clean unique lines.

### Advanced challenges (21-30)

21. Create equal-timestamp corrections and define a business-approved tie-break.
22. Explain why arbitrary dropDuplicates cannot guarantee the latest record.
23. Compare row-number winners after repartitioning the same fixture.
24. Design a duplicate policy when no trustworthy ordering metadata exists.
25. Distinguish missing-key rejection from deduplicating several null keys together.
26. Test idempotence: deduplicating an already deduplicated table changes nothing.
27. Explain why line_id and order_id+product_id are not interchangeable keys.
28. Design an audit that separates exact duplicates from conflicting corrections.
29. Compare batch permanent uniqueness with bounded streaming deduplication conceptually.
30. Write a configurable deduplication function and conflicting-record tests.


## Completion checks

Clean line_id values are unique and a duplicate audit preserves removed rows.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-05/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-05/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day05/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-05/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
