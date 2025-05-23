#!/usr/local/bin/python3



from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err


from datetime import datetime, timedelta
import time
import json
import os
import os.path
import logging
import argparse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

import itertools
import collections

import pickle as pkl

import re
from re import compile as recompile

# PySpark and create Spark context
if not 'sc' in locals():
    import pyspark
    sc = pyspark.SparkContext()

print('done !')


from operator import add


def readfile(infname):
    try:
        with open(infname, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()
        fp.close()
    except:
        lines = ['']
    lines = lines[2::4]
    lines = [ line.strip() for line in lines ]
    lines = [ line for line in lines if len(line) ]
    return lines


def whisper_failure_check_1(insrtdir):
    file_list = os.listdir(insrtdir)
    # get file list
    pathfname_list = []
    for fname in file_list:
        #if not fname[-4:] == '.whisper.log':
        if not fname[-4:] == '.srt':
            continue
        else:
            pathfname = insrtdir + fname
            pathfname_list.append(pathfname)
    # prepare RDD
    rdd = sc.parallelize(pathfname_list)
    # read in the files
    rdd1 = rdd.map(lambda w: (w, readfile(w)))
    rdd2 = rdd1.map(lambda w: (w[0], [ _.strip() for _ in w[1]]))
    # use pathfilename and its lineCnt as the key of each phrase transcription
    rdd3 = rdd2.map(lambda w: [ ((w[0], len(w[1])), _) for _ in w[1] ])
    # parallelize them
    rdd4 = rdd3.flatMap(lambda w: w)
    # give an entity '1' as their value, and meanwhile use ('pathfilename', 'phrase transcription') as key
    rdd5 = rdd4.map(lambda w: (w, 1))
    # map reduce by key
    rdd6 = rdd5.reduceByKey(add) \
        .filter(lambda w: w[1] > 1)
    # RDD6 as side debug info 
    RDD6 = rdd6.collect()
    RDD6_sorted = sorted(RDD6, key=lambda w: w[1])
    # # show case the first 800 repeated phrases
    # RDD6_sorted[-800:]
    # # plot out statistics
    # R = np.array([ _[1] for _ in RDD6_sorted ])
    # _ = plt.plot(np.log10(R))
    # _ = plt.plot(R[-150:])
    # final results
    # for _ in RDD6_sorted[:10]:
    #     print(_)
    rdd7 = rdd6.filter(lambda w: float(w[1])/float(w[0][0][1]) > 0.05 or w[1] > 20) \
        .filter(lambda w: len(w[0][1])) \
        .map(lambda w: (w[0][0], w[0][1], w[1]))
    RDD7 = rdd7.collect()
    RDD7u = sorted(list(set(RDD7)))
    # for _ in RDD7u[:100]:
    #     print(_)
    return RDD7u


for PROJ_NAME in ['./ACSMHK/', './CBI/', './CGST/', './FVC/', './JNG/', './WWBS/', './YFCX/']:
    for fn in whisper_failure_check_1(PROJ_NAME):
        print(fn)


# _ = os.system('wc -l */*.srt | sort -r')


def whisper_failure_check_2(insrtdir):
    fn_return = []
    file_list = os.listdir(insrtdir)
    # get file list
    pathfname_list = []
    for fname in file_list:
        #if not fname[-4:] == '.whisper.log':
        if not fname[-4:] == '.srt':
            continue
        else:
            pathfname = insrtdir + fname
            pathfname_list.append(pathfname)
    for pathfname in pathfname_list:
        # print('----    %s    ----' % pathfname)
        with open(pathfname, 'r') as fp:
            lines_curr = [ _.strip() for _ in fp.readlines() ]
        fp.close()
        lines_curr = lines_curr[2::4]
        trail_curr = lines_curr[-20:]
        text_tmp = ' '.join(trail_curr)
        if '阿門' not in text_tmp \
            and '阿們' not in text_tmp \
            and '祈禱' not in text_tmp \
            and '禱告' not in text_tmp \
            and '但願' not in text_tmp \
            and '願神' not in text_tmp \
            and '求主' not in text_tmp \
            and '幫助' not in text_tmp \
            and '最後' not in text_tmp \
            and '最後' not in text_tmp \
            and '保守' not in text_tmp \
            and '我們' not in text_tmp \
            and '停在這' not in text_tmp \
            and '奉耶穌' not in text_tmp:
            #print(pathfname)
            fn_return.append(pathfname)
    return fn_return


for PROJ_NAME in ['./ACSMHK/', './CBI/', './CGST/', './FVC/', './JNG/', './WWBS/', './YFCX/']:
    for fn in whisper_failure_check_2(PROJ_NAME):
        print(fn)








