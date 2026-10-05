"""Run from course root; Ctrl+C stops the local stream safely."""
from pathlib import Path
import argparse
import json
from pyspark.sql import SparkSession
from schemas import event_schema

p = argparse.ArgumentParser()
p.add_argument('--available-now', action='store_true', help='Process existing files then stop')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
(root / 'data/stream_input').mkdir(parents=True, exist_ok=True)
spark = (SparkSession.builder.master('local[2]').appName('RetailStreamStarter')
         .config('spark.sql.session.timeZone', 'UTC')
         .config('spark.sql.shuffle.partitions', '4').getOrCreate())
stream = (spark.readStream.schema(event_schema).option('maxFilesPerTrigger', 1)
          .json(str(root / 'data/stream_input')))
writer = (stream.writeStream.format('parquet').outputMode('append')
          .option('path', str(root / 'outputs/day22/events'))
          .option('checkpointLocation', str(root / 'checkpoints/day22')))
query = writer.trigger(availableNow=True).start() if a.available_now else writer.trigger(processingTime='5 seconds').start()
try:
    query.awaitTermination()
except KeyboardInterrupt:
    query.stop()
finally:
    print(json.dumps(query.lastProgress, indent=2, default=str))
    spark.stop()
