# Day 08: Joins and referential integrity

Suggested date: 2026-10-13. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

inner; left; full; semi; anti; aliases; join cardinality.

## Before you begin

Complete Day 07; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Join clean lines to products and orders with explicit column selection.
2. Join orders to customers and stores.
3. Find unknown keys using left_anti.
4. Use left_semi to find customers with completed purchases.
5. Demonstrate many-to-many inflation by deliberately duplicating a dimension key.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
unknown = lines.join(products.select("product_id"), "product_id", "left_anti")
```

## More examples to solve

1. Find customers without any order. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Compare inner and left joins for unknown product P999. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Find products never sold. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a join key in the retail dataset?
2. How does an inner join differ from a left join?
3. When would you use a full outer join?
4. What does a left semi join return?
5. What does a left anti join return?
6. Why use aliases when column names overlap?
7. What is a many-to-one join?
8. What is join cardinality, and why does it affect revenue?
9. How do ordinary equality joins treat null keys?
10. Why check dimension-key uniqueness before enrichment?

### Hands-on questions (11-20)

11. Join clean lines to product attributes.
12. Join lines to order status and timestamp.
13. Join orders to customers and stores with explicit output columns.
14. Find unknown product references with a left anti join.
15. Find customers with completed orders using a left semi join.
16. Find customers without orders using a left anti join.
17. Find products never referenced by accepted lines.
18. Compare inner and left join results for a P999 fixture.
19. Verify that dimension enrichment preserves clean line count.
20. Select unambiguous column names after joining customers and stores.

### Advanced challenges (21-30)

21. Duplicate one product-dimension key and quantify revenue inflation.
22. Create a many-to-many fixture and predict its output row count.
23. Compare joining on a list of key names with an explicit equality condition.
24. Demonstrate null-safe equality on a tiny nullable-key fixture.
25. Explain why filtering the right-side column after a left join can remove unmatched rows.
26. Compare filtering right-side rows before a join with filtering joined output.
27. Design a strategy for unmatched keys: reject, preserve, or map to an unknown dimension.
28. Inspect physical join operators and identify a potential shuffle.
29. Test that revenue and row count are preserved after every intended many-to-one join.
30. Write an enrichment function that fails when a dimension key is duplicated.


## Completion checks

Dimension keys are unique before joins; enrichment preserves clean line count.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-08/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-08/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day08/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-08/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
