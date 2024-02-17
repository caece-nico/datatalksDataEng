import sys
import os
from pyspark.sql import SparkSession
import pyspark
print(type(sys.argv))

#print(f'Nombre app {sys.argv[0]}' )
#print(f'Primer parametro {sys.argv[1]}' )
#print(f'Segundo parametro {sys.argv[2]}' )

import os

spark = SparkSession.builder.appName("niclas").getOrCreate()

print(spark)
