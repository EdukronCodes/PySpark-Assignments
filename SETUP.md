# Setup and run instructions

Use Python 3.10 or 3.11 and Java 17 for this course. PySpark is pinned to 3.5.8 for consistent exercises. Check Java with `java -version`, and set `JAVA_HOME` to your installed JDK directory if needed. See the official [installation requirements](https://spark.apache.org/docs/3.5.8/api/python/getting_started/install.html).

Open PowerShell in this course directory:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/generate_data.py
.\.venv\Scripts\python.exe -c "from pyspark.sql import SparkSession; s=SparkSession.builder.master('local[2]').getOrCreate(); print(s.range(5).count()); s.stop()"
```

If Python 3.11 is not installed, use an available compatible interpreter or install 3.11 first. Using the explicit virtual-environment executable avoids PowerShell activation restrictions. In Linux/WSL, replace it with `.venv/bin/python` after `python3.11 -m venv .venv`. Native Windows Hadoop filesystem errors can occur; use WSL2 with Java 17 rather than downloading untrusted helper executables.

For each batch assignment:

```python
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F
from pyspark.sql import types as T

spark = (SparkSession.builder.master('local[2]').appName('RetailAssignment')
         .config('spark.sql.session.timeZone', 'UTC')
         .config('spark.sql.shuffle.partitions', '4').getOrCreate())
# Read data using paths relative to the course root.
# Put your solution here, then stop the session:
# spark.stop()
```

Start the file stream in terminal 1:

```powershell
.\.venv\Scripts\python.exe examples/stream_ingest.py
```

Publish files in terminal 2:

```powershell
.\.venv\Scripts\python.exe scripts/publish_events.py --batch 1
.\.venv\Scripts\python.exe scripts/publish_events.py --batch 2
```

For watermarks, publish a batch, wait for its processing to finish, inspect progress, and then publish the next. Publishing all files immediately does not simulate wall-clock event arrivals accurately. `--interval 10` is a convenience, not a guarantee of completed micro-batches. Publish payment batches using `--source data/payments_archive --target data/payments_input`.

For a fresh streaming experiment, use a **new input, output, and checkpoint directory**, and supply those paths in your assignment script. Checkpoints belong to one query. Keep existing checkpoints for recovery exercises. `--available-now` handles all currently available input and exits; it is not a continuously running listener.

No Spark or Java environment has been installed by generating these materials. The dataset generator and file publisher use only Python's standard library. Optional pandas UDF, ML, Kafka, Connect, and lakehouse exercises require dependencies compatible with your chosen Spark/Python versions. Use a separate environment for Arrow/pandas experiments and consult REFERENCES.md before installing extras.
