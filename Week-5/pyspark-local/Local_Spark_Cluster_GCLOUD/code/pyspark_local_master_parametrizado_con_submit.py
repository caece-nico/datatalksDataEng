#!/usr/bin/env python
# coding: utf-8


import pyspark
from pyspark.sql import SparkSession
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input_data', required=True)
parser.add_argument('--output_data', required=True)

args = parser.parse_args()

input_data = args.input_data
output_data = args.output_data


spark = SparkSession.builder \
    .appName('TestMaster01') \
        .getOrCreate()


mi_parquet = spark.read.parquet(input_data)

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


mi_totalizador.coalesce(1).write.parquet(output_data)
