import os
from datetime import datetime
import pickle as pkl

import re
import multiprocessing
import time


THREAD_NUM = 2


with open('./phrase_list_total.txt', 'r') as fp:
    phrase_list_total = fp.read().split('\n')
fp.close()
phrase_list_total = [ _ for _ in phrase_list_total if len(_) ]


MAX_PID = len(phrase_list_total) - 1
print('total size of phrase_list_total:', MAX_PID+1)


PROJ_NAME_LIST = [
    'ACSMHK',
    'CBI',
    'CGST',
    'DSCCC',
    'FLWC',
    'FVC',
    'HKBC',
    'JNG',
    'KFC',
    'STBC',
    'WWBS',
    'YFCX',
    'YOS'
]


sermonpathfilelist = []
for PROJ_NAME in PROJ_NAME_LIST:
    data_dir_name_curr = '../../data/' + PROJ_NAME + '/'
    sermonpathfilelist += [ 
        data_dir_name_curr + _ 
        for _ in os.listdir(data_dir_name_curr)
    ]
sermonpathfilelist = sorted(sermonpathfilelist)


dict_sid2spfn = {} # dictionary mapping of sermon-id to sermon-pathfilename
for sid, sermonpathfilename in enumerate(sermonpathfilelist):
    dict_sid2spfn[sid] = sermonpathfilename


MAX_SID = sid
print('maximum sermon-id : %d' % MAX_SID)


def get_sermontext(insid):
    input_path_file_name = dict_sid2spfn.get(insid)
    with open(input_path_file_name, 'r') as fp:
        text = fp.read().replace('\n', '').strip()
    fp.close()
    return text


with open('../rep_common.txt', 'r') as fp:
    REP_LIST = [ _.strip() for _ in fp.readlines() ]
fp.close()
REP_LIST = [ _.split(", '", 1) for _ in REP_LIST ]
REP_LIST = [ [_[0], _[1][:-1]] for _ in REP_LIST ]


def cleanse_special_char(inputText):
    txt2 = inputText
    for rep_ in REP_LIST:
        txt2 = txt2.replace(rep_[0], rep_[1])
    txt2 = txt2.strip()
    return txt2


def symbol_removal(inputText):
    txt2 = inputText\
        .replace(' ', '').replace('.', '').replace(',', '') \
        .replace('?', '').replace('!', '').replace('-', '') \
        .replace('(', '').replace(')', '').replace('+', '') \
        .replace('[', '').replace(']', '').replace('*', '') \
        .replace('^', '').replace('$', '').replace('%', '') \
        .replace('#', '').replace('@', '') \
        .replace('\\', '')
    return txt2


# sermonText-to-phrase matrix dimension:
# MAX_SID x MAX_PID


scanBatchSize = 40


dict_sid2s = {}


def scan_through(sid_init, q):
    square = sid_init * sid_init
    # print(f'for sid in range({sid_init}, {MAX_SID + 1}, {THREAD_NUM})')
    for sid in range(sid_init, min(sid_init+scanBatchSize, MAX_SID + 1), THREAD_NUM):
        if sid % 10 == 0:
            print('%s    progress %d / %d ...' % (str(datetime.now()), sid, MAX_SID))
        dict_sid2s[sid] = symbol_removal(
            cleanse_special_char(
                get_sermontext(
                    sid
                )
            )
        )
    # q.put(square)
    for pid, p_curr in enumerate(phrase_list_total):
            s_curr = dict_sid2s[sid]
            if p_curr in s_curr:
                # pass
                n_ = len(re.findall(p_curr, s_curr))
                if n_: # if non-zero n)
                    # sparse_tuple_total_list.append((sid, pid, n_))
                    q.put((sid, pid, n_))

if __name__ == "__main__":
    
    # ===========================
    # threading manipulaion

    # to record the index of non-zero sparse element
    # expected data structure: [ (sid_1,pid_1,n1), (sid2,pid2,n2), ... ]

    sparse_tuple_list = []
    sparse_tuple_Queue = multiprocessing.Queue()
    # END threading manipulaion
    # ===========================

    sid_init = 0
    while sid_init < MAX_SID + 1:
        # Create subprocesses to compute occurance
        processes = []
        for i in range(THREAD_NUM):
            process = multiprocessing.Process(
                target=scan_through,
                args=(
                    sid_init + i,
                    sparse_tuple_Queue
                )
            )
            process.start()
            processes.append(process)

        # Wait for all subprocesses to finish
        for process in processes:
            process.join()

        # Collect results from the queue
        while not sparse_tuple_Queue.empty():
            sparse_tuple = sparse_tuple_Queue.get()
            sparse_tuple_list.append(sparse_tuple)

        print("progress: sparse_tuple_list length: %d" % len(sparse_tuple_list))
        sid_init += scanBatchSize

    print("Computed sparse tuple pairs:", sparse_tuple_list)
