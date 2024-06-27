import os
import sys
from datetime import datetime
import pickle as pkl
import numpy as np

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SUBPROC_NUM = sys.argv[1]
    else:
        print("SUBPROC_NUM is not provided !")
        print("EXIT !")
        exit()
    # s2s matrix generation

    with open('./var_02_sparse_tuple_list.pkl', 'rb') as fp:
        spOccur_list = pkl.load(fp)
    fp.close()

    print("type of spOccur_list: ", type(spOccur_list))
    print("entry count of spOccur_list: ", len(spOccur_list))

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

    with open("var_03_dict_p2sc.pkl", "rb") as fp:
        dict_p2sc = pkl.load(fp)
    fp.close()

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
    #     10 subprocess in total
    N_s2s_subproc = int(SUBPROC_NUM)
    for i, (s_, p_, c_) in enumerate(spOccur_list[ N_s2s_subproc :: 10 ]):
        if i % 5000 == 0:
            print(f"{str(datetime.now())} progress: N_s2s_subproc = {N_s2s_subproc} : {i} / {len(spOccur_list) / 10}")
        # p_ as the phrase id with c_ occurance
        sc_list = dict_p2sc.get(p_)
        if sc_list is None:
            continue
        for (s__, c__) in sc_list:
            MAT_S2S_COOCCUR[ s_ , s__ ] += c_ * c__

    with open(f"var_04_MAT_S2S_COOCCUR_subproc{SUBPROC_NUM}.pkl", "wb") as fp:
        pkl.dump(MAT_S2S_COOCCUR, fp)
    fp.close()
    print("finish generate s2s matrix")
