#!/bin/python3
import os
import sys
from operator import add
# PySpark and create Spark context
if not 'sc' in locals():
    import pyspark
    sc = pyspark.SparkContext()

PROJ_NAME = sys.argv[1]

filelist = os.listdir(PROJ_NAME)
for filename in filelist:
    pathfilename = PROJ_NAME + '/' + filename
    with open(pathfilename, 'r') as fp:
        lines = [ _.strip() for _ in fp.readlines() ]
    fp.close()
    rdd = sc.parallelize(lines)
    rdd1 = rdd.map(lambda w: (w, 1)).reduceByKey(add)
    rdd2 = rdd1.filter(lambda w: w[1] > 10)
    RDD2 = rdd2.collect()
    print(f'-------------{filename}-------------')
    for r_ in RDD2:
        print(r_)

