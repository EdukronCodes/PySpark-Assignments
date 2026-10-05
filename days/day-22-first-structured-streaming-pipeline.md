# Day 22: First Structured Streaming pipeline

Suggested date: 2026-10-27. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

readStream; explicit schema; micro-batches; append sink; checkpoints; triggers.

## Before you begin

Complete Day 21; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Start examples/stream_ingest.py with an empty data/stream_input directory.
2. Publish one archive batch with scripts/publish_events.py.
3. Inspect new Parquet output and query progress.
4. Publish a second batch while the stream is running.
5. Stop and restart with the same checkpoint and compare event counts.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
stream = spark.readStream.schema(event_schema).option("maxFilesPerTrigger", 1).json("data/stream_input")
# See the runnable example for sink and checkpoint configuration.
```

## More examples to solve

1. Compare batch and streaming DataFrames. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Why inference is disabled for this file stream. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Publish a file atomically so Spark never reads a partial file. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What makes a DataFrame streaming rather than bounded?
2. What is a micro-batch?
3. How does readStream differ from read?
4. What is a streaming source?
5. What is a streaming sink?
6. What is a checkpoint directory used for?
7. What does append output mode mean for a stateless query?
8. What does maxFilesPerTrigger control?
9. Why must arriving files be complete and immutable?
10. What does a processingTime trigger configure?

### Hands-on questions (11-20)

11. Start the supplied stream with an empty input directory.
12. Publish batch_001.json atomically with the publisher script.
13. Read the generated Parquet sink and inspect its events.
14. Publish batch_002.json while the query is running.
15. Inspect isStreaming on the input DataFrame.
16. Save query.lastProgress after a processed batch.
17. Stop and restart the same query with its existing checkpoint.
18. Verify committed source files are not processed again after restart.
19. Run an availableNow query on a separate set of paths.
20. Compare batch and stream ingestion schemas for identical JSON.

### Advanced challenges (21-30)

21. Explain why committed-file recovery does not remove duplicate business event IDs.
22. Publish a new filename containing an already-seen event and observe the duplicate.
23. Explain why modifying an already-discovered file is an invalid replay strategy.
24. Distinguish processingTime trigger intervals from guaranteed processing latency.
25. Explain why availableNow is different from a continuous listener.
26. Design isolated input, output, and checkpoint paths for repeatable tests.
27. Compare restarting with a retained checkpoint versus starting a fresh query.
28. Explain what Spark and the sink each contribute to recovery guarantees.
29. Create an ingestion runbook for empty input, malformed input, and interrupted processing.
30. Build a controlled two-batch smoke test with saved counts and progress evidence.


## Completion checks

Restart with the same checkpoint does not reread committed source files; business duplicates still exist until Day 24.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-22/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-22/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day22/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-22/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
