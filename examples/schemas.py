from pyspark.sql.types import (StructType, StructField, StringType, TimestampType,
                              ArrayType, IntegerType, DecimalType, MapType)

event_schema = StructType([
    StructField('event_id', StringType()),
    StructField('event_time', TimestampType()),
    StructField('customer_id', StringType()),
    StructField('order_id', StringType()),
    StructField('event_type', StringType()),
    StructField('items', ArrayType(StructType([
        StructField('product_id', StringType()),
        StructField('quantity', IntegerType()),
        StructField('unit_price', DecimalType(12, 2)),
    ]))),
    StructField('device', StructType([
        StructField('os', StringType()), StructField('app_version', StringType())
    ])),
    StructField('attributes', MapType(StringType(), StringType())),
])

payment_schema = StructType([
    StructField('payment_id', StringType()), StructField('order_id', StringType()),
    StructField('payment_time', TimestampType()), StructField('amount', DecimalType(12, 2)),
])
