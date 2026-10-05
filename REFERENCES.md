# Official reading by topic

This course targets Spark 3.5.8. Read examples against that version rather than mixing them with a newer release. Links were reviewed on 5 October 2026; versioned docs take precedence for the pinned course.

| Days | Official source |
| --- | --- |
| 1-2 | [Installation](https://spark.apache.org/docs/3.5.8/api/python/getting_started/install.html), [DataFrame quickstart](https://spark.apache.org/docs/3.5.8/api/python/getting_started/quickstart_df.html) |
| 3-15 | [SQL and DataFrames guide](https://spark.apache.org/docs/3.5.8/sql-programming-guide.html), [Python API reference](https://spark.apache.org/docs/3.5.8/api/python/reference/index.html) |
| 16-17 | [SQL performance tuning](https://spark.apache.org/docs/3.5.8/sql-performance-tuning.html), [Spark tuning](https://spark.apache.org/docs/3.5.8/tuning.html) |
| 18 | [PySpark testing guide](https://spark.apache.org/docs/3.5.8/api/python/getting_started/testing_pyspark.html) |
| 19-21 | [RDD programming guide](https://spark.apache.org/docs/3.5.8/rdd-programming-guide.html), [Submitting applications](https://spark.apache.org/docs/3.5.8/submitting-applications.html) |
| 22-25, 27, 29 | [Structured Streaming guide](https://spark.apache.org/docs/3.5.8/structured-streaming-programming-guide.html) |
| 26 | [Kafka integration](https://spark.apache.org/docs/3.5.8/structured-streaming-kafka-integration.html), [Kafka quickstart](https://kafka.apache.org/quickstart) |
| 28 | [MLlib guide](https://spark.apache.org/docs/3.5.8/ml-guide.html) |
| 30 | [Monitoring](https://spark.apache.org/docs/3.5.8/monitoring.html), [Configuration](https://spark.apache.org/docs/3.5.8/configuration.html), [Security](https://spark.apache.org/docs/3.5.8/security.html) |

## Coverage boundaries

The required track covers Python DataFrames and SQL, ingestion and schemas, expressions, nulls, quality, duplicates, joins, windows, calendars/cohorts, nested types, UDF tradeoffs, Parquet, execution and shuffles, caching/skew/AQE, testing, incremental design/SCD, RDDs, streaming sources/sinks, windows/watermarks, deduplication, recovery, foreachBatch, stream joins, sessions, ML pipelines, and production design.

Pandas UDF/Arrow, pandas API on Spark, Connect, custom state APIs, RocksDB, transactional table formats, Kafka infrastructure, ALS/classification implementations, and real cluster deployment are extensions or design exercises. GraphX is a JVM API, SparkR is a separate language API, and legacy DStreams are outside this modern PySpark course. Those topics should not be confused with missing everyday DataFrame tasks.
