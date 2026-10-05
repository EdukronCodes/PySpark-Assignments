# Day 18: Testing and data contracts

Suggested date: 2026-10-23. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

assertDataFrameEqual; schemas; fixtures; quality thresholds; negative tests.

## Before you begin

Complete Day 17; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Create five-row fixtures for amount calculations and null rules.
2. Test join cardinality and unique business keys.
3. Test deterministic deduplication and duplicate updates.
4. Test empty input and all-invalid input.
5. Define required columns, types, allowed statuses, and failure policy in a data contract.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
from pyspark.testing.utils import assertDataFrameEqual
# Build small expected DataFrames with the same types as actual output.
```

## More examples to solve

1. Inject missing order_id and expect quarantine. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Swap an integer field for text. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Revenue 900.00 must not become 899.99. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a data contract?
2. What is the purpose of a small deterministic fixture?
3. How does a unit test differ from an integration test?
4. Why is equal row count insufficient to prove equal output?
5. What should a schema assertion check?
6. Why test null inputs explicitly?
7. What is a negative test?
8. Why should tests avoid relying on unspecified row order?
9. What does assertDataFrameEqual help compare?
10. What is a quality threshold used for?

### Hands-on questions (11-20)

11. Test the 900.00 net amount calculation using explicit decimal types.
12. Test every basket-band boundary.
13. Test null and blank key rejection.
14. Test discount values below zero and above one.
15. Test unknown product and order references.
16. Test that dimension enrichment preserves line count.
17. Test that line business keys are unique after deduplication.
18. Test that cancelled orders do not increase booked revenue.
19. Test empty input and all-invalid input.
20. Create a contract for required columns, types, keys, and statuses.

### Advanced challenges (21-30)

21. Introduce a faulty rounding implementation and show that a test detects it.
22. Introduce an extra dimension row and detect join inflation.
23. Test changed duplicates with equal timestamps and deterministic tie-breaks.
24. Compare schema checks with value-level business validation.
25. Design property checks for revenue additivity across disjoint partitions.
26. Test transformation idempotence where business semantics require it.
27. Explain when approximate floating equality is appropriate and when decimals are required.
28. Keep tests isolated so temporary views and output paths do not interfere.
29. Design a small integration test covering raw-to-gold reconciliation.
30. Create a test report showing each deliberately broken implementation was caught.


## Completion checks

Tests catch deliberately introduced errors and compare row content, not only counts.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-18/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-18/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day18/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-18/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
