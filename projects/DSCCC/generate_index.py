#!/usr/local/bin/python3

from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err
from datetime import datetime, timedelta
import time
import json
import os.path
import pandas as pd

import itertools
import collections

import pickle as pkl

import re
from re import compile as recompile

print('done !')
# obtain the whole source of DSCCC
import os
dsccc_path = '../../data/DSCCC/'
filelist = sorted(os.listdir(dsccc_path))


# the initial of different kind of preacher
preacherTitle_list = ['博士','牧師','傳道','老師','先生','教授','弟兄','社長','長老','醫生']
# the bible books
book_list = [
    '創世記','出埃及記','利未記','民數記','申命記',
    '約書亞記','士師記','路得記','撒母耳記上','撒母耳記下','列王記上','列王記下',
    '歷代志上','歷代志下','以斯拉記','尼希米記','以斯帖記',
    '約伯記','詩篇','箴言','傳道書','雅歌',
    '以賽亞書','耶利米書','耶利米哀歌','以西結書','但以理書',
    '何西阿書','約珥書','阿摩司書','俄巴底亞書','約拿書','彌迦書',
    '那鴻書','哈巴谷書','西番雅書','哈該書','撒迦利亞書','瑪拉基書',
    '馬太福音','馬可福音','路加福音','約翰福音','使徒行傳',
    '羅馬書','哥林多前書','哥林多後書','加拉太書','以弗所書',
    '腓立比書','歌羅西書','帖撒羅尼迦前書','帖撒羅尼迦後書',
    '提摩太前書','提摩太後書','提多書','腓利門書','希伯來書',
    '雅各書','彼得前書','彼得後書','約翰一書','約翰二書',
    '約翰三書','猶大書','啟示錄']


# cannot use datetime as the key
# because there can have multiple sermon
# marked on the same date
# dt2t_dict = {} # datetime-to-title dict
# dt2p_dict = {} # datetime-to-preacher dict
rid2dtptcv_dict = {} # record_id to datetime, preacher, title, and bible chapter-verse dictionary
# {rid: [dt, p, t]}
record_id = 0
for fname in filelist:
    if '.txt' not in fname:
        continue
    _ = fname.split('_')
    dt = _[0] # datetime
    title = _[1].replace('.txt', '') # title
    with open(dsccc_path + fname, 'r') as fp:
        # to obtain the preacher name
        row1st = fp.readline()
        # print(row1st)
        if '-' in row1st:
            _ = row1st.split('-')
        else:
            _ = row1st.split('–')
        p = _[0].strip() # preacher
        # to obtain bible chapter and verse coverage
        cv_text = ''
        lines = fp.readlines()
        for line in lines:
            try:
                remaining_text = line
                if '經文：' in remaining_text[:3] \
                or '讀經：' in remaining_text[:3] \
                or '經課：' in remaining_text[:3]:
                    cv_text = remaining_text.split('：')[1].strip()
                    cv_text = cv_text \
                        .replace('：', ':') \
                        .replace('章', ':') \
                        .replace('節', '') \
                        .replace('，', ',') \
                        .replace('；', ';') \
                        .replace(' ', '') \
                        .replace('"', '') \
                        .strip()
                    # cv_text description rules:
                    #     if multiple number of books are included
                    #     there is a ';' serving as a delimiter
                    #     if multiple verses / chapters / chapter-verses are included
                    #     from the same book, a ',' serves as a delimiter
                    # if ',' in cv_text or ';' in cv_text:
                    #     print(dt, title)
                    #     print(cv_text)
                    break
                else:
                    continue
            except:
                break
    fp.close()
    rid2dtptcv_dict[record_id] = [dt, title, p, cv_text]
    # print(rid2dtptcv_dict[record_id])
    record_id += 1
df = pd.DataFrame(
    [rid2dtptcv_dict.get(rid) for rid in range(len(rid2dtptcv_dict.keys()))],
    columns = [
        'date',
        'title',
        'preacher',
        'coverage'
    ]
)
print(df)
print(f"total number of sermons count: {len(rid2dtptcv_dict.keys())}")
df = df.sort_values(['date', 'title'])
for index, row in df.iterrows():
    print(
        row['date'],
        row['title'],
        row['preacher'],
        row['coverage']
    )


df.to_csv('./index_byd.csv', index=False)


