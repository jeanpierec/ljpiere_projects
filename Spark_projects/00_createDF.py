#-*- coding: utf-8 -*-
# Importe librerias
import uuid
from decimal import Decimal
from datetime import datetime
rom pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import HiveContext
from pyspark.sql import functions as fn
import time

# Configuracion sesion
sc_conf = SparkConf()
sc_conf.setAppName("Colombia")
sc_conf.set("spark.executor.memory", "1g")
sc_conf.set("park.sql.sources.partitionOverwriteMode","dynamic")

# Configuracion del context
sc = SparkContext(conf=sc_conf)
hc = HiveContext(sc)

hc.setConf("spark.sql.parquet.compression.codec","snappy")
hc.setConf("hive.exec.dynamic.partition.mode", "nonstrict")

#------------------------------------------------------------------------
# Empty RDD
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)

#------------------------------------------------------------------------
# Empty df with schema
from pyspark.sql.types import StructType,StructField, StringType
# StructType doesn't have printschema/show functions
schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
  ])

