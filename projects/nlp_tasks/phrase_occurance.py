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

import itertools
import collections

import re
from re import compile as recompile

import pickle as pkl

if not 'sc' in locals():
    import pyspark
    sc = pyspark.SparkContext()

print('done !')


# from subprocess import Popen, PIPE                                              
# def execute_commands(commands):                                                 
#     p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)                   
#     out, err = p.communicate()                                                  
#     print(out)                                                                  
#     print()                                                                     
#     print(err)                                                                  
#     return out, err                                                             
                                                                                
                                                                                
# from datetime import datetime, timedelta                                        
# import time                                                                     
# import json                                                                     
# import os.path                                                                  
# import logging                                                                  
# import argparse                                                                 
# import matplotlib.pyplot as plt                                                 
# import numpy as np                                                              
# from matplotlib.backends.backend_pdf import PdfPages                            
# import pandas as pd                                                             
                                                                                
# import itertools                                                                
# import collections                                                              
                                                                                
# import pickle as pkl                                                            
                                                                                
# import re                                                                       
# from re import compile as recompile                                             
                                                                                
# # PySpark and create Spark context                                              
# if not 'sc' in locals():                                                        
#     import pyspark                                                              
#     sc = pyspark.SparkContext()                                                 
                                                                                
# print('done !')


# with open('CORPUS/ci.pkl', 'rb') as fp:
#     CI = pkl.load(fp)
# fp.close()


PROJ_NAME = 'STBC'
DATA_DIR_NAME = '../../data/' + PROJ_NAME


sermonfilelist = os.listdir(DATA_DIR_NAME)


sermonpathfilelist = [ DATA_DIR_NAME + '/' + _ for _ in sermonfilelist ]


dict_sid2spfn = {} # dictionary mapping of sermon-id to sermon-pathfilename
for sid, sermonpathfilename in enumerate(sermonpathfilelist):
    dict_sid2spfn[sid] = sermonpathfilename


MAX_SID = sid
print('maximum sermon-id : %d' % MAX_SID)


# spark context parallelized sermon-id
rdd_SERMON = sc.parallelize([ _ for _ in range(MAX_SID + 1) ])


rdd_SERMON.count()


rdd_SERMON.sample(False, 0.05).count()


# for _ in rdd_SERMON.take(3):
#     print(_)


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


# obtain the textual content per file
rdd_SERMON2 = \
    rdd_SERMON \
    .sample(False, 0.05) \
    .map(get_sermontext) \
    .map(cleanse_special_char) \
    .map(symbol_removal)


# for _ in rdd_SERMON2.take(3):
#     print(_)


def sermon_tokenize(intext):
    N = len(intext)
    phrase_list = []
    # bi gram
    for i in range(N-1):
        phrase_list.append(intext[i : i+2])
    # # tri gram
    # for i in range(N-2):
    #     phrase_list.append(intext[i : i+3])
    # tetra gram
    # for i in range(N-3):
    #     phrase_list.append(intext[i : i+4])
    # # penta gram
    # for i in range(N-4):
    #     phrase_list.append(intext[i : i+5])
    return phrase_list


print('='*50)
print('start of tokenization spark process')
print('='*50)


rdd_TOKENS = rdd_SERMON2.map(sermon_tokenize) \
    .flatMap(lambda w: w) \
    .distinct()
# distinct() operation deduplicates repeated phrase pattern


MAX_PHID = rdd_TOKENS.count()
print('phrase token total count: %d' % MAX_PHID)


phrase_list_total = rdd_TOKENS.collect()


print('='*50)
print('finish tokenization spark process')
print('='*50)


print('length of array list of collected spark rdd: %d' % len(phrase_list_total))


dict_phid2ph = {} # dictionary mapping of phrase-id to phrase
for phid, ph in enumerate(phrase_list_total):
    dict_phid2ph[phid] = ph


len(dict_phid2ph.keys())


# MAX_SID = 10
MAX_PHID = 10000


rdd_sid_phid_pair = sc.parallelize( \
    list(
        itertools.product( \
            [ _ for _ in range(MAX_SID+1) ] ,
            [ _ for _ in range(MAX_PHID+1) ]
        )
    )
)
# an rdd of (sid, phid) pairs


def phrase_occurance_count(sid_phid_input_pair):
    insid = sid_phid_input_pair[0]
    inphid = sid_phid_input_pair[1]
    occCnt = 0
    PHR = dict_phid2ph.get(inphid)
    SERMONTEXT = \
        symbol_removal(
            cleanse_special_char(
                get_sermontext(insid)
            )
        )
    occCnt = sum(1 for m in re.finditer(PHR, SERMONTEXT))
    return occCnt


print('='*50)
print('start of occurance mapping count')
print('='*50)


rdd_OCCURANCE = rdd_sid_phid_pair \
    .map(lambda w: (w, phrase_occurance_count(w))) \
    .filter(lambda w: w[1] > 0)


OCC = rdd_OCCURANCE.collect()


print('='*50)
print('finish occurance mapping count')
print('='*50)


OCC





print('='*50)
print('start of dumping results')
print('='*50)


with open('ENV.pkl', 'wb') as fp:
    pkl.dump((dict_sid2spfn, dict_phid2ph, OCC), fp)
fp.close()


print('='*50)
print('finish dumping results')
print('='*50)








