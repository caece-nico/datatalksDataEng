#!/usr/bin/env python
# coding: utf-8


import pyspark
from pyspark.sql import SparkSession
import argparse


spark = SparkSession.builder\
    .master("spark://de-zoomcamp.us-west4-b.c.projectonleali.internal:7077")\
        .appName('TestMaster01')\
            .getOrCreate()


mi_parquet = spark.read.parquet("../data/data/green/*/*")

mi_parquet.createOrReplaceTempView('mi_vista')

mi_totalizador = spark.sql(
    """
    select PULocationID as ZoneID,
    date_trunc('day', lpep_pickup_datetime) as dateID,
    sum(total_amount) as total
    from mi_vista
    group by ZoneID, dateID
    """
)


mi_totalizador.coalesce(1).write.parquet("../data/reportes/con_script/")
