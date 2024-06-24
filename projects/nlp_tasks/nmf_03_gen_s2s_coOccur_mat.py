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


with open('./var_02_sparse_tuple_list.pkl', 'rb') as fp:
    spOccur_list = pkl.load(fp)
fp.close()


print("type of spOccur_list: ", type(spOccur_list))


print("entry count of spOccur_list: ", len(spOccur_list))



'''# data structure of spOccur_list'''


# list of triples 
# [
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#        ...
#      ( < sermon-id > , < phrase-id > , < occurance count > )
# ]


print(f"{str(datetime.now())} try print out spOccur_list samples:")
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


print(f"{str(datetime.now())} parallelized spOccur_list, try take 20 samples:")
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


print(f"{str(datetime.now())} RDD_KEYBY_PID collect():")
RDD_KEYBY_PID = rdd_keyBy_pid.collect()


print(f"{str(datetime.now())} entry count in RDD_KEYBY_PID: {len(RDD_KEYBY_PID)}")
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


print(f"{str(datetime.now())} save var_03_dict_p2sc.pkl")
with open("var_03_dict_p2sc.pkl", "wb") as fp:
    pkl.dump(dict_p2sc, fp)
fp.close()
print(f"{str(datetime.now())} done !")









'''# s2s matrix generation'''


with open('./var_02_sermonDict.txt', 'r') as fp:
    sermonDict = fp.read().split('\n') # the sermon spfn dictionary is in sorted order
fp.close()
sermonDict = [ _ for _ in sermonDict if len(_) ]


dict_sid2spfn = {}
sid = 0
for spfn_ in sermonDict:
    dict_sid2spfn[sid] = spfn_
    sid += 1


print("type of sermonDict: ", type(sermonDict))
print("type of dict_sid2spfn: ", type(dict_sid2spfn))


print("entry count of sermonDict: ", len(sermonDict))
print("entry count of dict_sid2spfn: ", len(dict_sid2spfn.keys()))


# (s1, p1, a)
# (s1, p2, b)

# (s2, p1, p)
# (s2, p2, q)

# algorithm flow:
# 1. iterate each sermon
#    S_1
#     1.2) check in current sermon S_1 which phrases have occurance
#     1.3) form these phrases in a list
#     1.4) iterate each (other) sermon
#          S_2
#           a) list out phrases occurred in current sermon S_2
#           b) check coocurring phrase





print(f"spOccur_list length b4 in-RDD_KEYBY_PID filter: {len(spOccur_list)}")
spOccur_list = [ spn_ for spn_ in spOccur_list if spn_[1] in dict_p2sc ]
print(f"spOccur_list length af in-RDD_KEYBY_PID filter: {len(spOccur_list)}")








# -----------------------
# counting criteria 1 :
# -----------------------
#     total phrasal co-occurance from all found phrase
#     phrase occurance frequency is hard-coded to 1

MAX_SID = len(dict_sid2spfn.keys())


MAT_S2S_COOCCUR = np.zeros((MAX_SID, MAX_SID))
print("MAT_S2S_COOCCUR shape:", MAT_S2S_COOCCUR.shape)

# s2s subprocess num
#     defining the spOccur_list portion
#     20 subprocess in total
for N_s2s_subproc in range(20):
    for i, (s_, p_, c_) in enumerate(spOccur_list[ N_s2s_subproc :: 20 ]):
        if i % 1000 == 0:
            print(f"{str(datetime.now())} progress: N_s2s_subproc = {N_s2s_subproc} : {i} / {len(spOccur_list) / 20}")
        # p_ as the phrase id with c_ occurance
        sc_list = dict_p2sc.get(p_)
        if sc_list is None:
            continue
        for (s__, c__) in sc_list:
            MAT_S2S_COOCCUR[ s_ , s__ ] += c_ * c__


with open("var_03_MAT_S2S_COOCCUR.pkl", "wb") as fp:
    pkl.dump(MAT_S2S_COOCCUR, fp)
fp.close()


print("finish generate s2s matrix")








