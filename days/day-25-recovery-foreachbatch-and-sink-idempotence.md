# Day 25: Recovery, foreachBatch, and sink idempotence

Suggested date: 2026-10-30. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

query progress; batch_id; replay; at-least-once callbacks; checkpoint compatibility.

## Before you begin

Complete Day 24; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Write a foreachBatch callback that publishes a Parquet snapshot per batch_id.
2. Use a committed batch directory as the local completion record.
3. Inject a failure before publication and verify safe retry.
4. Restart without changing source, schema, or stateful logic.
5. Explain why arbitrary external side effects require idempotent sink writes and why checkpoint deletion changes recovery.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
def write_batch(df, batch_id):
    df.write.mode("overwrite").parquet(f"outputs/day25/batch_{batch_id}")
# Lab-only stable batch folders; replace with transactional publication in a real sink.
```

## More examples to solve

1. Fail after write but before recording success. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Print batch_id and source offsets. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Try a changed state schema using a new lab checkpoint. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What does foreachBatch pass to its callback?
2. What does batch_id identify?
3. Why can a foreachBatch callback execute again for a retried batch?
4. What makes a sink write idempotent?
5. Why are checkpoints necessary but insufficient for arbitrary external side effects?
6. What should a committed-batch record mean?
7. Why isolate query checkpoint directories?
8. Why can changing stateful query logic make recovery incompatible?
9. What is the difference between a source replay and a sink duplicate?
10. Why should a callback not collect a large batch to the driver?

### Hands-on questions (11-20)

11. Write each batch to a stable batch_id-specific Parquet path.
12. Log batch_id, row count, and output location.
13. Create a local committed-batch marker after successful publication.
14. Inject failure before the output is committed.
15. Restart and verify that retry produces one logical output batch.
16. Run two actions inside the callback and discuss temporary caching.
17. Record query progress before and after restart.
18. Verify an empty batch does not crash your callback.
19. Keep stateful logic unchanged during a checkpoint-recovery experiment.
20. Document the local-filesystem assumptions of your callback implementation.

### Advanced challenges (21-30)

21. Inject failure after writing but before recording success and analyze the duplicate risk.
22. Explain why check-then-write is insufficient with concurrent writers.
23. Design a transactional sink protocol that combines data publication and commit recording.
24. Explain why batch_id alone is not globally unique across unrelated queries.
25. Define a query identity plus batch_id key for sink commits.
26. Compare overwrite-per-batch lab outputs with append-only external side effects.
27. Design safe recovery after checkpoint loss without assuming source events remain retained.
28. Explain which query changes require a deliberate new checkpoint and replay plan.
29. Ensure a stateful foreachBatch consumer fully consumes the batch as required by the query.
30. Deliver a failure-matrix test covering pre-write, post-write, pre-commit, and restart behavior.


## Completion checks

A replay of the same batch_id produces one committed logical batch; document local filesystem assumptions.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-25/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-25/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day25/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-25/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
