# Day 20: Project 3 - Reliable batch pipeline

Suggested date: 2026-10-25. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Intermediate.

## Goal and concepts

bronze/silver/gold; configuration; logs; incremental loads; operational runbook.

## Before you begin

Complete Day 19; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Create a CLI pipeline with --input, --output, and --run-id.
2. Keep raw bronze, validated silver, and business gold datasets.
3. Log counts, elapsed time, schema, and rejected reasons.
4. Add return-adjusted revenue without joining raw returns directly to raw lines.
5. Run initial, incremental, retry, and failed-validation scenarios with a runbook.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
# For the local lab, stage a complete snapshot then publish only after checks pass.
# Document that local folder publication is not a distributed transaction.
```

## More examples to solve

1. Partial output exists after a crash: recover with a new staging directory. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Return references an unknown line. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Return quantity exceeds purchased quantity. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What belongs in bronze, silver, and gold layers?
2. Why retain raw bronze records?
3. What is the purpose of a run_id?
4. Which quality metrics should a batch run log?
5. Why aggregate return events before joining sales lines?
6. Why deduplicate return_id before summing returned quantities?
7. Which returns are valid under the course business rules?
8. Why should staging outputs be validated before publication?
9. What information belongs in a recovery runbook?
10. Why is local folder publication not a distributed transaction?

### Hands-on questions (11-20)

11. Build a CLI accepting input, output, and run-id arguments.
12. Write separate bronze, validated silver, and reporting gold outputs.
13. Record raw, rejected, duplicate, and accepted line counts.
14. Aggregate accepted return units by line_id.
15. Calculate return deductions and return-adjusted revenue.
16. Reconcile return-adjusted revenue with the manifest.
17. Reject a return referencing an unknown line.
18. Reject return quantities exceeding the line's purchased units.
19. Run the same input twice and compare unique business rows.
20. Document a complete initial-load command and expected outputs.

### Advanced challenges (21-30)

21. Inject a failure after staging and demonstrate a safe recovery run.
22. Inject failure after publication but before run-status recording and discuss retry handling.
23. Test multiple partial returns against one sale without revenue multiplication.
24. Define how invalid return records affect pipeline status and reporting.
25. Design atomic publication assumptions for local storage versus object storage.
26. Define a policy for two runs trying to publish the same output concurrently.
27. Separate financial metric failures from noncritical missing-email warnings.
28. Design partition-specific backfills with unaffected dates preserved.
29. Package transformation functions and meaningful integration checks.
30. Deliver an operations walkthrough covering success, validation failure, crash, and retry.


## Completion checks

Accepted valid return units are aggregated by line before subtraction; reruns preserve unique output and all layers reconcile.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-20/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-20/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day20/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-20/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
