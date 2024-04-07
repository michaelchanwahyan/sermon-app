#!/usr/local/bin/python3


import os

import itertools
import collections

import re
from re import compile as recompile

from datetime import datetime

import pickle as pkl

import multiprocessing


with open('CORPUS/ci.pkl', 'rb') as fp:
    CI = pkl.load(fp)
fp.close()

THREAD_NUM = 8
CI_ = [None] * THREAD_NUM
for THR in range(THREAD_NUM):
    CI_[THR] = CI[THR::THREAD_NUM]
#CI_[0] = CI[0::8]
#CI_[1] = CI[1::8]
#CI_[2] = CI[2::8]
#CI_[3] = CI[3::8]
#CI_[4] = CI[4::8]
#CI_[5] = CI[5::8]
#CI_[6] = CI[6::8]
#CI_[7] = CI[7::8]


# print('size of CI series:')
# print('  CI0      |  CI1      |  CI2      |  CI3      |  CI4      |  CI5      |  CI6      |  CI7')
# print('  %07d  |  %07d  |  %07d  |  %07d  |  %07d  |  %07d  |  %07d  |  %07d' % (len(CI_[0]),len(CI_[1]),len(CI_[2]),len(CI_[3]),len(CI_[4]),len(CI_[5]),len(CI_[6]),len(CI_[7])))


PROJ_NAME_LIST = [
    'ACSMHK',
    'CBI',
    'CGST',
    'FLWC',
    'FVC',
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
    sermonpathfilelist += [ data_dir_name_curr + _ for _ in os.listdir(data_dir_name_curr) ]


dict_sid2spfn = {} # dictionary mapping of sermon-id to sermon-pathfilename
for sid, sermonpathfilename in enumerate(sermonpathfilelist):
    dict_sid2spfn[sid] = sermonpathfilename


MAX_SID = sid
# print('maximum sermon-id : %d' % MAX_SID)


def get_already_extracted_spfn_list():
    already_list_fname = 'already_extracted_spfn_list.txt'
    if os.path.exists(already_list_fname):
        with open(already_list_fname, 'r') as fp:
            lines = fp.readlines()
        fp.close()
        lines = [ line.strip() for line in lines ]
        lines = [ line for line in lines if len(line) ]
        return lines
    else:
        return []


def overwrite_already_extracted_spfn_list(inlist):
    with open('already_extracted_spfn_list.txt', 'w') as fp:
        for _ in inlist:
            _ = _.strip()
            if len(_) == 0:
                continue
            else:
                fp.write(_)
                fp.write('\n')
        fp.close()
    return


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


def sermon_tokenize(pid, intext, q, CI_curr):
    phrase_list_total = q.get()
    N = len(intext)
    # bi gram
    for i in range(N-1):
        # if i % 8000 == 0:
        #     print('CI no. %d :    %d / %d' % (pid, i, N))
        phr_curr = intext[i : i+2]
        if phr_curr in phrase_list_total:
            continue
        elif phr_curr in CI_curr:
            phrase_list_total.append(phr_curr)
            CI_curr.remove(phr_curr)
    # # tri gram
    # for i in range(N-2):
    #     phrase_list.append(intext[i : i+3])
    # # tetra gram
    # for i in range(N-3):
    #     phrase_list.append(intext[i : i+4])
    # # penta gram
    # for i in range(N-4):
    #     phrase_list.append(intext[i : i+5])
    q.put(phrase_list_total)


if __name__ == '__main__':

    # ================================================
    # OLD EXISTING FILE INTEGRATION
    already_extracted_spfn_list = get_already_extracted_spfn_list()

    dict_sid2s = {} # dictionary mapping of sermon-id to sermon text (cleansed)
    # ===========================
    # threading manipulaion
    phrase_list_totalQueue = [None] * THREAD_NUM
    for i in range(THREAD_NUM):
        phrase_list_totalQueue[i] = multiprocessing.Queue()
        phrase_list_totalQueue[i].put([])
    # END threading manipulaion
    # ===========================
    for sid in range(0, MAX_SID + 1):
        if sid % 1 == 0:
            print('%s    progress: %d / %d' % (str(datetime.now()), sid, MAX_SID))
        if dict_sid2spfn.get(sid) in already_extracted_spfn_list:
            continue
        else:
            already_extracted_spfn_list.append(dict_sid2spfn.get(sid))
            dict_sid2s[sid] = symbol_removal(
                cleanse_special_char(
                    get_sermontext(
                        sid
                    )
                )
            )
            # ===========================
            # threading manipulaion
            p = [None] * THREAD_NUM
            for i in range(THREAD_NUM):
                p[i] = multiprocessing.Process(
                    target=sermon_tokenize,
                    args=(
                        i,
                        dict_sid2s[sid],
                        phrase_list_totalQueue[i],
                        CI_[i]
                    )
                )
                p[i].start()
            for i in range(THREAD_NUM):
                p[i].join()
            # END threading manipulaion
            # ===========================
            qSize = 0
            for i in range(THREAD_NUM):
                phrase_arr_curr = phrase_list_totalQueue[i].get()
                qSize += len(phrase_arr_curr)
                phrase_list_totalQueue[i].put(phrase_arr_curr)
            print('%s    phrase_list_total size: %d' % (datetime.now(), qSize))
        # END OF if dict_sid2spfn.get(sid) in already_extracted_spfn_list:


    print('%s    prepare append phrase list total' % datetime.now())





    # ================================================
    # OLD EXISTING FILE INTEGRATION
    if os.path.exists('phrase_list_total.pkl'):
        with open('phrase_list_total', 'rb') as fp:
            phrase_list_total = pkl.load(fp)
        fp.close()
    else:
        phrase_list_total = []
    for i in range(THREAD_NUM):
        phrase_arr_curr = phrase_list_totalQueue[i].get()
        phrase_list_total.append(phrase_arr_curr)
    with open('phrase_list_total.pkl', 'wb') as fp:
        pkl.dump(phrase_list_total, fp)
    fp.close()
    print('%s    finish append phrase list total' % datetime.now())


    # ================================================
    # OLD EXISTING FILE INTEGRATION
    overwrite_already_extracted_spfn_list(already_extracted_spfn_list)


