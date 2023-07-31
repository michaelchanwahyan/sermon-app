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
# obtain the whole source of HKBC
import os
hkbc_path = '../../data/HKBC/'
filelist = os.listdir(hkbc_path)
for filename in filelist:
    if not filename.isdigit():
        print(f"{filename} is unable to be converted to integer !")
print("removing these files from filelist ...")
filelist = [ filename for filename in filelist if filename.isdigit() ]
print("done !")


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


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    sermonNum = 0
    titleStr = '' # the title
    confNum = '' # the bible conference number
    lectNum = '' # the lecture number in current session
    speaker = '' # the speaker
    titleStrFound = False
    confNumFound = False
    speakerFound = False
    # sermonTextFound = False
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.titleStrFound = True
        elif tag == 'h1' and \
             len(attrs) == 1 and \
             'color-1a8090 bg-white text-center pb-2 pt-3 h2' in attrs[0]:
            self.confNumFound = True
        elif tag == 'a' and \
             len(attrs) == 1 and \
             '/speaker/view' in attrs[0][1]:
            self.speakerFound = True
        return

    def handle_endtag(self, tag):
        return

    def handle_data(self, data):
        # retrieve the sermon title
        if self.titleStrFound and ~len(self.titleStr):
            self.titleStr = re.sub(r'\ +', ' ', data.strip().replace('\xa0', ''))
            # print(self.titleStr)
            self.titleStrFound = False
        # retrieve the conference sermon session number (code)
        elif self.confNumFound and ~len(self.confNum):
            full_sess_lect_data = data.strip()
            _data = full_sess_lect_data.split(' ')
            self.confNum = _data[0]
            if self.confNum == '首屆':
                self.confNum = '第1屆'
            self.lectNum = _data[-1]
            # print(self.confNum, self.lectNum)
            self.confNumFound = False
        # retrieve the speaker name
        elif self.speakerFound and ~len(self.speaker):
            self.speaker = data.strip()
            # print(self.speaker)
            self.speakerFound = False
        return
def sermonBkgndInfoRetrieval(pathfilename):
    with open(pathfilename, "r") as fp:
        htmltext = fp.read()
    fp.close()
    parser = MyHTMLParser()
    parser.feed(htmltext)
    return parser
def sermonBibleVersesCoverageRetrieval(pathfilename):
    with open(pathfilename, "r") as fp:
        lines = fp.readlines()
    fp.close()
    c_v_line = '' # the line with chapter and verse
    for line in lines:
        if "article-citation" in line \
        and "data-book" in line \
        and "data-start-chapter" in line \
        and "data-start-verse" in line:
            c_v_line = line
            break
    b = ''
    c_start = ''
    v_start = ''
    c_end = ''
    v_end = ''
    if len(c_v_line) > 0:
        # obtain the book number
        key_pattern = "data-book=\""
        idx_curr = c_v_line.find(key_pattern)
        for i in range(3):
            if c_v_line[idx_curr + len(key_pattern) + i].isdigit():
                b += c_v_line[idx_curr + len(key_pattern) + i]
            else:
                break
        # obtain the starting chapter number
        key_pattern = "data-start-chapter=\""
        idx_curr = c_v_line.find(key_pattern)
        for i in range(3):
            if c_v_line[idx_curr + len(key_pattern) + i].isdigit():
                c_start += c_v_line[idx_curr + len(key_pattern) + i]
            else:
                break
        # obtain the starting versse number
        key_pattern = "data-start-verse=\""
        idx_curr = c_v_line.find(key_pattern)
        for i in range(3):
            if c_v_line[idx_curr + len(key_pattern) + i].isdigit():
                v_start += c_v_line[idx_curr + len(key_pattern) + i]
            else:
                break
        # obtain [potentially there] the ending chapter number
        key_pattern = "data-end-chapter=\""
        idx_curr = c_v_line.find(key_pattern)
        if idx_curr == -1:
            c_end = c_start
        else:
            for i in range(3):
                if c_v_line[idx_curr + len(key_pattern) + i].isdigit():
                    c_end += c_v_line[idx_curr + len(key_pattern) + i]
                else:
                    break
        # obtain [potentially there] the ending versse number
        key_pattern = "data-end-verse=\""
        idx_curr = c_v_line.find(key_pattern)
        if idx_curr == -1:
            v_end = v_start
        else:
            for i in range(3):
                if c_v_line[idx_curr + len(key_pattern) + i].isdigit():
                    v_end += c_v_line[idx_curr + len(key_pattern) + i]
                else:
                    break
    return b, c_start, v_start, c_end, v_end
# testitem = sermonBkgndInfoRetrieval(f"{hkbc_path}{1203}")
# print(testitem.speaker)
# print(estitem.titleStr)
# print(testitem.confNum)
# print(testitem.lectNum)
handles = []
for filename in filelist:
    if int(filename) % 100 == 0:
        print(filename)
    sermonNum = int(filename)
    handles.append(
        (
            filename,
            sermonBkgndInfoRetrieval(f"{hkbc_path}{filename}"),
            sermonBibleVersesCoverageRetrieval(f"{hkbc_path}{filename}")
        )
    )
def remove_preacher_title(preacher_with_title, title_list):
    for title in title_list:
        if title in preacher_with_title:
            x = preacher_with_title.find(title)
            return preacher_with_title[:x]
df = pd.DataFrame(
    columns = [
        'code',
        'preacher',
        'conference no.',
        'lecture no.',
        'title',
        'book no.',
        'book',
        'verses'
    ]
)

# handles element contains
# (h[0], h[1])
# h[0]: sermon number
# h[1] attributes:
#     titleStr # the title
#     confNumNum # the bible conference number
#.    lectNum # the lecture number of current session
#     speaker # the speaker
for h in handles:
    if len(h[2][0]) > 0:
        b = book_list[int(h[2][0])-1]
        cv = f"{h[2][1]}:{h[2][2]}"
        if len(h[2][3]) > 0 and len(h[2][4]) > 0:
            cv += f"-{h[2][3]}:{h[2][4]}"
        else:
            cv += f"-{h[2][1]}:{h[2][2]}"
    else:
        b = ''
        cv = ''
    print(
        h[0],
        remove_preacher_title(h[1].speaker, preacherTitle_list),
        h[1].confNum,
        h[1].lectNum,
        h[1].titleStr,
        h[2][0],
        b,
        cv
    )
    df = pd.concat(
        [df,
         pd.DataFrame(
             [[h[0],
               remove_preacher_title(h[1].speaker, preacherTitle_list),
               int(h[1].confNum[1:-1]),
               int(h[1].lectNum[1:-1]),
               h[1].titleStr,
               h[2][0],
               b,
               cv]],
             columns=[
                 'code',
                 'preacher',
                 'conference no.',
                 'lecture no.',
                 'title',
                 'book no.',
                 'book',
                 'verses'
             ]
         )
        ]
    )
print(df)
df['conference no.'] = pd.to_numeric(df['conference no.'], errors='coerce')
df['lecture no.'] = pd.to_numeric(df['lecture no.'], errors='coerce')
df = df.sort_values(['conference no.', 'preacher', 'lecture no.'])
for index, row in df.iterrows():
    print(
        row['code'],
        row['preacher'],
        row['conference no.'],
        row['lecture no.'],
        row['title'],
        row['book no.'],
        row['book'],
        row['verses']
    )


df.to_csv('./index_byc.csv', index=False)


