import os
from datetime import datetime
import pickle as pkl
import numpy as np

with open('./var_sparse_tuple_list.pkl', 'rb') as fp:
    spOccur_list = pkl.load(fp)
fp.close()

# data structure of spOccur_list
# list of triples 
# [
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#      ( < sermon-id > , < phrase-id > , < occurance count > )
#        ...
#      ( < sermon-id > , < phrase-id > , < occurance count > )
# ]

with open('./var_phrDict.pkl', 'rb') as fp:
    phrDict = pkl.load(fp) # the phrase dictionary is in sorted order
    dict_pid2phr = {}
    pid = 0
    for phr_ in phrDict:
        dict_pid2phr[pid] = phr_
        pid += 1
fp.close()

with open('./var_sermonDict.pkl', 'rb') as fp:
    sermonDict = pkl.load(fp) # the sermon spfn dictionary is in sorted order
    dict_sid2spfn = {}
    sid = 0
    for spfn_ in sermonDict:
        dict_sid2spfn[sid] = spfn_
        sid += 1
fp.close()

#       0  1  2  3  ...
#     --------------------------
#  0 |  a  b  c  d  ...
#  1 |  e  f  g  h  ...
#  2 |  i  j  k  l  ...
#  . |     .
#  . |     .
#  . |     .

# -----------------------
# counting criteria 1 :
# -----------------------
#     total phrasal co-occurance from all found phrase
MAX_SID = len(dict_sid2spfn.keys())
MAT_S2S_COOCCUR = np.zeros((MAX_SID, MAX_SID))