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
    sermonpathfilelist += [ data_dir_name_curr + _ for _ in os.listdir(data_dir_name_curr) ]
sermonpathfilelist = sorted(sermonpathfilelist)


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
        phr_curr = intext[i : i+2]
        if phr_curr in phrase_list_total:
            continue
        elif phr_curr in CI_curr:
            phrase_list_total.append(phr_curr)
            CI_curr.remove(phr_curr)
    # tri gram
    for i in range(N-2):
        phr_curr = intext[i : i+3]
        if phr_curr in phrase_list_total:
            continue
        elif phr_curr in CI_curr:
            phrase_list_total.append(phr_curr)
            CI_curr.remove(phr_curr)
    # tetra gram
    for i in range(N-3):
        phr_curr = intext[i : i+4]
        if phr_curr in phrase_list_total:
            continue
        elif phr_curr in CI_curr:
            phrase_list_total.append(phr_curr)
            CI_curr.remove(phr_curr)
    # end of 2- 3- 4- gram
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
            print('%s  already in extracted spfn list.    SKIP' % dict_sid2spfn.get(sid))
            continue
        else:
            print('%s  in progress ...' % dict_sid2spfn.get(sid))
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
        print('existing file     phrase_list_total.pkl    is found !')
        print('read in and append in operation')
        with open('phrase_list_total.pkl', 'rb') as fp:
            phrase_list_total = pkl.load(fp)
        fp.close()
    else:
        print('file     phrase_list_total.pkl    is not found !')
        print('create and append in operation')
        phrase_list_total = []
    for i in range(THREAD_NUM):
        phrase_arr_curr = phrase_list_totalQueue[i].get()
        phrase_list_total.extend(phrase_arr_curr)
    phrase_list_total = list(set(phrase_list_total))
    with open('phrase_list_total.pkl', 'wb') as fp:
        pkl.dump(phrase_list_total, fp)
    fp.close()
    print('%s    finish append phrase list total' % datetime.now())


    # ================================================
    # OLD EXISTING FILE INTEGRATION
    already_extracted_spfn_list = sorted(already_extracted_spfn_list)
    overwrite_already_extracted_spfn_list(already_extracted_spfn_list)


    with open('phrase_list_total.txt', 'w') as fp:
        for p_curr in sorted(phrase_list_total):
            fp.write(p_curr + '\n')
    fp.close()


