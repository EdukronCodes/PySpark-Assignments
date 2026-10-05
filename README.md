# 30 days of PySpark with retail data

A practical assignment course from first DataFrame to reliable batch and streaming pipelines, with **30 topic-specific questions every day: 900 questions total**. Each day progresses through 10 foundation questions, 10 hands-on questions, and 10 advanced challenges, in addition to its original assignments and examples. Start with [setup](SETUP.md), [data definitions](DATA_DICTIONARY.md), and [projects](PROJECTS.md). This is a broad core curriculum, not every API or vendor-specific feature. Python basics are assumed; no prior Spark experience is required.

Suggested schedule: **6 October-4 November 2026**, 4-6 hours daily including all questions, with up to 6-8 hours for projects. Dates are a suggested next-day start in Asia/Kolkata; assignment data timestamps use UTC. Split a day's workload into two sessions or work at your own pace if needed.

The core track uses local files. Kafka, transactional lakehouse formats, custom streaming state, Arrow, and remote Spark Connect are extensions with additional setup. Examples are starters; assignments intentionally require your own implementation. No paid service is needed for the core track.

## Daily assignment files

| Day | Assignment | Suggested date |
| --- | --- | --- |
| 01 | [Setup and your first retail DataFrame](days/day-01-setup-and-your-first-retail-dataframe.md) | 2026-10-06 |
| 02 | [Explicit schemas and file ingestion](days/day-02-explicit-schemas-and-file-ingestion.md) | 2026-10-07 |
| 03 | [Filtering, expressions, and retail amounts](days/day-03-filtering-expressions-and-retail-amounts.md) | 2026-10-08 |
| 04 | [Cleaning and quarantine](days/day-04-cleaning-and-quarantine.md) | 2026-10-09 |
| 05 | [Deduplication and deterministic records](days/day-05-deduplication-and-deterministic-records.md) | 2026-10-10 |
| 06 | [Aggregations and business metrics](days/day-06-aggregations-and-business-metrics.md) | 2026-10-11 |
| 07 | [Project 1 - Retail sales report](days/day-07-project-1-retail-sales-report.md) | 2026-10-12 |
| 08 | [Joins and referential integrity](days/day-08-joins-and-referential-integrity.md) | 2026-10-13 |
| 09 | [Spark SQL and equivalent DataFrame queries](days/day-09-spark-sql-and-equivalent-dataframe-queries.md) | 2026-10-14 |
| 10 | [Window functions for rankings](days/day-10-window-functions-for-rankings.md) | 2026-10-15 |
| 11 | [Dates, calendars, and cohorts](days/day-11-dates-calendars-and-cohorts.md) | 2026-10-16 |
| 12 | [Nested JSON and complex types](days/day-12-nested-json-and-complex-types.md) | 2026-10-17 |
| 13 | [Functions, UDFs, and Arrow](days/day-13-functions-udfs-and-arrow.md) | 2026-10-18 |
| 14 | [Project 2 - Customer analytics mart](days/day-14-project-2-customer-analytics-mart.md) | 2026-10-19 |
| 15 | [Parquet, partitions, and table layouts](days/day-15-parquet-partitions-and-table-layouts.md) | 2026-10-20 |
| 16 | [Query plans and Spark execution](days/day-16-query-plans-and-spark-execution.md) | 2026-10-21 |
| 17 | [Performance, skew, and caching](days/day-17-performance-skew-and-caching.md) | 2026-10-22 |
| 18 | [Testing and data contracts](days/day-18-testing-and-data-contracts.md) | 2026-10-23 |
| 19 | [Incremental processing and changing dimensions](days/day-19-incremental-processing-and-changing-dimensions.md) | 2026-10-24 |
| 20 | [Project 3 - Reliable batch pipeline](days/day-20-project-3-reliable-batch-pipeline.md) | 2026-10-25 |
| 21 | [RDDs, distributed variables, and API choices](days/day-21-rdds-distributed-variables-and-api-choices.md) | 2026-10-26 |
| 22 | [First Structured Streaming pipeline](days/day-22-first-structured-streaming-pipeline.md) | 2026-10-27 |
| 23 | [Event time, windows, and watermarks](days/day-23-event-time-windows-and-watermarks.md) | 2026-10-28 |
| 24 | [Streaming deduplication and enrichment](days/day-24-streaming-deduplication-and-enrichment.md) | 2026-10-29 |
| 25 | [Recovery, foreachBatch, and sink idempotence](days/day-25-recovery-foreachbatch-and-sink-idempotence.md) | 2026-10-30 |
| 26 | [Kafka integration lab](days/day-26-kafka-integration-lab.md) | 2026-10-31 |
| 27 | [Stream joins, sessions, and state](days/day-27-stream-joins-sessions-and-state.md) | 2026-11-01 |
| 28 | [MLlib on retail data](days/day-28-mllib-on-retail-data.md) | 2026-11-02 |
| 29 | [Project 4 - Live retail monitoring](days/day-29-project-4-live-retail-monitoring.md) | 2026-11-03 |
| 30 | [Project 5 - Batch and streaming retail capstone](days/day-30-project-5-batch-and-streaming-retail-capstone.md) | 2026-11-04 |

## Included materials

- `data/raw/`: six synthetic CSV tables, including deliberately bad and duplicated line items.
- `data/events_archive/`: six ordered JSON purchase/activity batches; `data/payments_archive/`: matching payment events.
- `scripts/generate_data.py`: deterministic regeneration and expected statistics in `data/manifest.json`.
- `scripts/publish_events.py`: atomic file arrival simulator.
- `examples/schemas.py` and `examples/stream_ingest.py`: explicit schema and runnable stream starter.
- [Kafka lab](KAFKA_LAB.md), [references](REFERENCES.md), and [progress checklist](PROGRESS.md).

## Progression

Days 1-7: foundations and a sales report. Days 8-14: SQL, joins, windows, customer analytics. Days 15-21: storage, performance, testing, reliable batch processing, RDDs. Days 22-27: streaming, late events, recovery, Kafka, and state. Days 28-30: MLlib and integrated projects.

Use the dataset manifest to check raw row counts. For cleaned results, follow the business rules exactly before comparing totals. Never count rejected rows as sales. Raw data and outputs are different folders; keep source data intact.
