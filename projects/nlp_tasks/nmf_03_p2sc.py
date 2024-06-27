#!/usr/local/bin/python3



from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err


import os
from datetime import datetime
import pickle as pkl
import numpy as np

# PySpark and create Spark context
if not 'sc' in locals():
    import pyspark
    sc = pyspark.SparkContext()

print('done !')


__main__filename = 'nmf_03_p2sc()'


with open('./var_02_sparse_tuple_list.pkl', 'rb') as fp:
    spOccur_list = pkl.load(fp)
fp.close()


print(f'[{str(datetime.now())} @ {__main__filename}]    type of spOccur_list: {type(spOccur_list)}')


print(f'[{str(datetime.now())} @ {__main__filename}]    entry count of spOccur_list: {len(spOccur_list)}')



'''# data structure of spOccur_list'''


# list of triples 
# [
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#        ...
#      ( < sermon-id > , < phrase-id > , < occurance count > )
# ]


print(f'[{str(datetime.now())} @ {__main__filename}]    try print out spOccur_list samples:')
for i, spc in enumerate(spOccur_list):
    print(spc)
    if i > 10:
        break









'''# s2s matrix outlook'''








#       0  1  2  3  ...
#     --------------------------
#  0 |  a  b  c  d  ...
#  1 |  e  f  g  h  ...
#  2 |  i  j  k  l  ...
#  . |     .
#  . |     .
#  . |     .








# -------------------
# sermon-to-phrase
# -------------------

# for i, spc in enumerate(spOccur_list):
#     if spc[2] <30:
#         continue
#     print(f"record {i}    spc: {spc}")
#     if i >= 10000:
#         break


rdd = sc.parallelize(spOccur_list)


print(f'[{str(datetime.now())} @ {__main__filename}]    parallelized spOccur_list, try take 20 samples:')
for spc_ in rdd.take(20):
    print(spc_)


# rdd :: (sid, pid, cnt)

rdd2 = rdd \
    .map(lambda w: (w[1], (w[0], w[2])))

# rdd2 :: (pid, (sid, cnt))


rdd_keyBy_pid = rdd2 \
    .groupByKey() \
    .mapValues(list) \
    .filter(lambda w: len(w[1]) > 100)
# rdd_keyBy_pid :: (pid, [(sid, cnt), (sid, cnt), ... ])


print(f'[{str(datetime.now())} @ {__main__filename}]    RDD_KEYBY_PID collect():')
RDD_KEYBY_PID = rdd_keyBy_pid.collect()


print(f'[{str(datetime.now())} @ {__main__filename}]    entry count in RDD_KEYBY_PID: {len(RDD_KEYBY_PID)}')
# RDD_KEYBY_PID :: (pid, [(sid, cnt), (sid, cnt), ... ])


for (pid_in_RDD, _) in sorted(RDD_KEYBY_PID):
    if pid_in_RDD % 1000 == 0:
        # print(pid_in_RDD, dict_pid2phr.get(pid_in_RDD))
        print(pid_in_RDD)
        print(f"[{_[0]}, {_[1]}, {_[2]}, ...]")
    else:
        continue


dict_p2sc = {}
for (pid_in_RDD, sc_list) in RDD_KEYBY_PID:
    dict_p2sc[pid_in_RDD] = sc_list


print(f'[{str(datetime.now())} @ {__main__filename}]    save var_03_dict_p2sc.pkl')
with open("var_03_dict_p2sc.pkl", "wb") as fp:
    pkl.dump(dict_p2sc, fp)
fp.close()
print(f'[{str(datetime.now())} @ {__main__filename}]    done !')








