import os
from datetime import datetime as datetime
import pickle as pkl
import numpy as np


if __name__ == '__main__':
    __main__filename = 'nmf_07_find_similarity()'

    with open('./var_02_sermonDict.txt', 'r') as fp:
        sermonDict = fp.read().split('\n') # the sermon spfn dictionary is in sorted order
    fp.close()
    sermonDict = [ _ for _ in sermonDict if len(_) ]
    dict_sid2spfn = {}
    sid = 0
    for spfn_ in sermonDict:
        dict_sid2spfn[sid] = spfn_
        sid += 1

    print(f'[{str(datetime.now())} @ {__main__filename}]    type of sermonDict: {type(sermonDict)}')
    print(f'[{str(datetime.now())} @ {__main__filename}]    type of dict_sid2spfn: {type(dict_sid2spfn)}')

    p_matrix_fname = 'var_06_P.txt'
    print(f'[{str(datetime.now())} @ {__main__filename}]    loading P ...')
    P = np.loadtxt(p_matrix_fname)
    print(f'[{str(datetime.now())} @ {__main__filename}]    done loading P !')
    
    