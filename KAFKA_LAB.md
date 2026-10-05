# Optional Kafka lab (Day 26)

The core streaming assignments work with file arrival. This extension needs a running local Kafka broker, Kafka CLI tools, and the matching Spark connector. Follow the [official Kafka quickstart](https://kafka.apache.org/quickstart) for your broker version; CLI flags and installation layout vary. The commands below use the Unix Kafka tools (WSL is convenient).

Create a topic against a local broker:

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic retail-events --partitions 3 --replication-factor 1
```

Use a console producer and paste one complete line from `data/events_archive/batch_001.json`:

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic retail-events
```

This initial smoke test publishes an unkeyed value. For the keyed assignment, write a producer or use console producer key parsing with a delimiter absent from your JSON; set the key to event_id. Kafka keys do not automatically deduplicate records. Repeat the exact same event to verify your Spark deduplication logic.

Submit your assignment using the Spark 3.5.8/Scala 2.12 connector:

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8 submissions/day-26/assignment.py
```

Use the equivalent `.venv/Scripts/spark-submit.cmd` on native Windows if available, or the environment's spark-submit command in WSL. The connector must match the Spark release and Scala binary version. See the [official Spark Kafka integration guide](https://spark.apache.org/docs/3.5.8/structured-streaming-kafka-integration.html).

Parse values:

```python
raw = (spark.readStream.format('kafka')
       .option('kafka.bootstrap.servers', 'localhost:9092')
       .option('subscribe', 'retail-events')
       .option('startingOffsets', 'earliest').load())
parsed = raw.select('topic', 'partition', 'offset',
                    F.from_json(F.col('value').cast('string'), event_schema).alias('event'))
# Keep Kafka metadata when flattening event.* and split invalid records to quarantine.
```

Inspect source progress and offsets. Restart using the same checkpoint. Initial startingOffsets applies to a new query; resumed queries use checkpoint progress. Use a new checkpoint only for a deliberate fresh replay. A Kafka sink can duplicate records under retries; document your downstream deduplication key. Record broker availability, topic retention, and recovery assumptions. A local single-broker setup is a learning environment, not a production availability design.
