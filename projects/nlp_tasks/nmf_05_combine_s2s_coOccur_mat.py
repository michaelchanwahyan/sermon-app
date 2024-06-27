import os
from datetime import datetime
import pickle as pkl
import numpy as np

if __name__ == '__main__':
    __main__filename = 'nmf_05_combine_s2s_coOccur_mat()'
    try:
        for subproc_num in range(0,10):
            # for subproc 0
            fname = f"var_04_MAT_S2S_COOCCUR_subproc{subproc_num}.pkl"
            with open(fname, "rb") as fp:
                M = pkl.load(fp)
            fp.close()
            print(f'[{str(datetime.now())} @ {__main__filename}]    load {fname} success !')

        # OUTPUT
        fname = "var_05_MAT_S2S_COOCCUR.pkl"
        with open(fname, "wb") as fp:
            M = pkl.dump(M, fp)
        fp.close()
        print(f'[{str(datetime.now())} @ {__main__filename}]    combine and write file {fname} success !')

        # # remove subprocess part file
        # print(f'[{str(datetime.now())} @ {__main__filename}]    removing subprocess part files ...')
        # for subproc_num in range(0,10):
        #     # for subproc 0
        #     fname = f"var_04_MAT_S2S_COOCCUR_subproc{subproc_num}.pkl"
        #     _ = os.system(f"rm -f {fname}")
        print("done !")
    except:
        print(f'[{str(datetime.now())} @ {__main__filename}]    file combine s2s matrix goes wrong !')
        exit()
