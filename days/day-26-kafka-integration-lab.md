# Day 26: Kafka integration lab

Suggested date: 2026-10-31. Dates are optional; shift the entire schedule if starting later.
Time: 4-6 hours including all 30 questions (milestone projects may take 6-8 hours). Difficulty: Advanced.

## Goal and concepts

Kafka source/sink; keys; offsets; JSON parsing; connector packages; retention; consumer semantics.

## Before you begin

Complete Day 25; retain its validated outputs. Read DATA_DICTIONARY.md for table grains.
Run all commands from the course root. Start batch exercises with the imports and session in SETUP.md. `clean_lines` means the Day 5 accepted, deduplicated lines with Day 3 monetary columns. `facts`, `enriched`, and `category_sales` are tables you build in preceding exercises, not preloaded variables. Streaming exercises use `event_schema` from `examples/schemas.py`.

## Study and practice schedule

1. 20 minutes: read the related official guide linked in REFERENCES.md and summarize the concepts in your own words.
2. 20 minutes: reproduce the starter pattern on a five-row fixture.
3. 70-100 minutes: complete the assignments below.
4. 90-150 minutes: solve the 30-question bank from foundation through advanced; reuse your assignment outputs where appropriate.
5. 30 minutes: check extra examples, save evidence, and answer the review questions. Split the day into two sessions when needed.

## Assignments

1. Complete the local file-source equivalent first; Kafka is an optional infrastructure extension.
2. Follow KAFKA_LAB.md to start or use a local broker and create retail-events.
3. Publish archived events keyed by event_id with a producer.
4. Read Kafka value using from_json and the event schema.
5. Compare fresh startingOffsets earliest with resumed checkpoint offsets and design a dead-letter output.

## Starter pattern

This is a starting example, not the full assignment solution. Define any referenced input DataFrames first.

```python
raw = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "retail-events").option("startingOffsets", "earliest").load()
```

## More examples to solve

1. Malformed JSON in Kafka value. Create your own tiny fixture, predict the result, and then verify it in Spark.
2. Restart producer and send a duplicate key. Create your own tiny fixture, predict the result, and then verify it in Spark.
3. Retained source offsets disappear before recovery. Create your own tiny fixture, predict the result, and then verify it in Spark.
4. Change one assumption in today's business logic and explain how the output changes.
5. Add one edge-case check that fails when you intentionally break your code.

## Daily question bank - 30 questions

Solve in order: questions 1-10 establish the basics, 11-20 apply them to retail data, and 21-30 test edge cases, debugging, and design. Advanced questions are relative to this day; later days build on earlier work.

Answer conceptual questions in your own words. For practical questions, submit executable code, a small input fixture, expected output, and observed results. Preserve question numbers in `answers.md`. Optional infrastructure questions may use the stated file-source alternative.

### Foundation questions (1-10)

1. What is a Kafka topic?
2. What is a Kafka partition?
3. What is a record offset?
4. How do a record key and value differ?
5. Why does a Kafka key not automatically deduplicate events?
6. What are bootstrap servers used for?
7. Why is a Spark Kafka connector package needed?
8. What does startingOffsets='earliest' request for a fresh query?
9. How does a checkpoint affect offsets on restart?
10. What is a dead-letter or quarantine output?

### Hands-on questions (11-20)

11. Complete the equivalent file-source parse-and-quarantine lab first.
12. For the optional broker lab, create a retail-events topic.
13. Publish one archive event as a Kafka value.
14. Publish keyed events using event_id as the key.
15. Read Kafka topic, partition, offset, key, and value columns.
16. Parse value with from_json and the explicit event schema.
17. Preserve source metadata when flattening event fields.
18. Route a malformed JSON record into quarantine.
19. Restart from the same checkpoint and inspect resumed source progress.
20. Record connector coordinates, broker version, and observed event counts.

### Advanced challenges (21-30)

21. Explain why adding partitions affects ordering assumptions across keys.
22. Compare earliest, latest, and explicit offsets only on fresh isolated queries.
23. Explain how source retention can prevent checkpoint-based recovery.
24. Send duplicate keyed values and verify your Spark business deduplication.
25. Distinguish Kafka log ordering within a partition from global event-time ordering.
26. Design output event keys for downstream duplicate handling.
27. Explain why a Kafka sink can contain duplicates during retry.
28. Configure an ingestion-rate bound and observe its effect on lag.
29. Design offset-range evidence for replay and reconciliation without claiming Kafka consumer commits drive Spark recovery.
30. Write a broker-unavailable and retention-loss runbook; provide a file-source simulation if no broker is available.


## Completion checks

File-source core lab passes; for Kafka extension, record broker version, package coordinate, offsets, and parsed event counts.
Complete all 30 numbered daily questions, retaining expected-versus-actual evidence for coding exercises and written reasoning for conceptual/design questions.
Compare values and business keys, not only row counts. Save the input fixture and expected rows for at least one example. Sort only when presentation or a deterministic comparison needs it.

## Submit today

- `submissions/day-26/assignment.py` or an equivalent notebook with executable cells.
- `submissions/day-26/notes.md`: assumptions, answers, one error you fixed, and the completion evidence.
- Outputs under `outputs/day26/`, with a small sample and a schema summary in the notes.
- At least three extra examples solved with expected-versus-actual results.
- `submissions/day-26/answers.md` with answers numbered 1-30, referencing solution code and evidence. Clearly label any optional infrastructure question completed using its supported alternative.

## Review questions

1. What is the input and output grain, and which operation can change the row count?
2. Which null, duplicate, time, or retry case could make today's result wrong?
3. Which action executes your work, and where could a shuffle or state growth occur?

## Stretch challenge

Turn today's logic into a reusable function with explicit inputs and document one scale limitation. For streaming days, include a saved `lastProgress` record and explain state and checkpoint behavior.

[Course index](../README.md) · [Business definitions](../DATA_DICTIONARY.md) · [Project rubrics](../PROJECTS.md)
