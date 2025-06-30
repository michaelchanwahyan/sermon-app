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
import logging
import argparse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

import itertools
import collections

import pickle as pkl

import re
from re import compile as recompile

# PySpark and create Spark context
if not 'sc' in locals():
    import pyspark
    sc = pyspark.SparkContext()

print('done !')


# obtain the whole webpage of the sermon videos uploaded by Johnson_Ng
import os
_ = os.system("rm -f vinehk.videos")
_ = os.system("wget -O vinehk.videos https://www.youtube.com/@thevinehk/videos")
_ = os.system("rm -f vinehk.streams")
_ = os.system("wget -O vinehk.streams https://www.youtube.com/@thevinehk/streams")
_ = os.system("rm -f vineyl.videos")
_ = os.system("wget -O vineyl.videos https://www.youtube.com/@thevine_yl/videos")
_ = os.system("rm -f vineyl.streams")
_ = os.system("wget -O vineyl.streams https://www.youtube.com/@thevine_yl/streams")
_ = os.system("cat vinehk.videos vinehk.streams vineyl.videos vineyl.streams > videos")
_ = os.system("rm -f vine*.*")


# read in the html source of the webpage
with open("videos", "r") as fp:
    vtext = fp.read()
fp.close()



'''### Run By Your Host System if new audio files are included
cd ~/TPPHC/SERMON/VINE/

ls *.mp3 > ~/SOURCE/sermon-app/projects/VINE/exlist.txt

#vim ~/SOURCE/sermon-app/projects/VINE/exlist.txt # edit to only preserve the 11-character hash code'''


# refetch the list of existing audio files
with open("exlist.txt", "r") as fp:
    ex_list = fp.readlines()
fp.close()
ex_list_2 = []
for ex in ex_list:
    ex = ex.strip()
    if ex[-5] == ']':
        ex = ex[-16:-5]
    else:
        ex = ex[-15:-4]
    ex_list_2.append(ex)
ex_list = ex_list_2
print('existing list contains %d' % len(ex_list))


# use regular expression to find all the occurance of video
# by the youtube code pattern
_list = re.findall( r'watch\?v=(...........)', vtext)
print('The Vine Church completed list contains %d' % len(_list))


# for newly found youtube videos in webpage html but
# not yet in the list of audio files, we identify them
# and pack them into 'needed_list'
needed_list =  [_ for _ in _list if _ not in ex_list]
needed_list = list(set(needed_list))
N = len(needed_list)
print('total count of new recording contents: %d' % N)


# generate download script
_ = os.system("rm -f download.sh")
cnt = 1
if not os.path.isfile("download.sh"):
    with open("download.sh", "w") as fp:
        fp.write('#!/bin/bash\n')
        for needed_code in needed_list:
            fp.write('echo ; echo ; date ; ')
            fp.write('echo ; echo ; echo %d / %d ; ' % (cnt, N))
            fp.write('echo ; echo ; yt-dlp -x --audio-format mp3 ')
            fp.write('https://youtube.com/watch?v=%s\n' % needed_code)
            cnt += 1
    fp.close()









'''### Run By Your Host System
cd ~/SOURCE/sermon-app/projects

bash download.sh

### move the downloaded mp3 back to my audio storage directory
mv \*.mp3 ~/TPPHC/SERMON/VINE/'''








# the initial of different kind of preacher
preacherTitle_list = ['博士','牧師','傳道','老師','先生','教授','弟兄','社長']


# the bible books
book_list = [
    '創世記','出埃及記','利未記','民數記','申命記',
    '約書亞記','士師記','撒母耳記上','撒母耳記下','列王記上','列王記下',
    '以賽亞書','耶利米書','以西結書',
    '何西阿書','約珥書','阿摩司書','俄巴底亞書','約拿書','彌迦書',
    '那鴻書','哈巴谷書','西番雅書','哈該書','撒迦利亞書','瑪拉基書',
    '詩篇','箴言','約伯記','雅歌','路得記','耶利米哀歌','傳道書',
    '以斯帖記','但以理書','以斯拉記','尼希米記','歷代志上','歷代志下',
    '馬太福音','馬可福音','路加福音','約翰福音','使徒行傳',
    '羅馬書','哥林多前書','哥林多後書','加拉太書','以弗所書',
    '腓立比書','腓利比書','歌羅西書','帖撒羅尼迦前書','帖撒羅尼迦後書',
    '提摩太前書','提摩太後書','提多書','腓利門書','希伯來書',
    '雅各書','彼得前書','彼得後書','約翰壹書','約翰一書','約翰貳書','約翰二書',
    '約翰參書','約翰三書','猶大書','啟示錄']


# the bible book ordering
bk2bkorder_dict = {
    '創世記':1, '出埃及記':2,'利未記':3,'民數記':4,'申命記':5,
    '約書亞記':6,'士師記':7,
    '撒母耳記上':8,'撒母耳記下':9,
    '列王記上':10,'列王記下':11,
    '以賽亞書':12,'耶利米書':13,'以西結書':14,
    '何西阿書':15,'約珥書':16,'阿摩司書':17,'俄巴底亞書':18,'約拿書':19,'彌迦書':20,
    '那鴻書':21,'哈巴谷書':22,'西番雅書':23,'哈該書':24,'撒迦利亞書':25,'瑪拉基書':26,
    '詩篇':27,'箴言':28,'約伯記':29,'雅歌':30,'路得記':31,'耶利米哀歌':32,'傳道書':33,
    '以斯帖記':34,'但以理書':35,'以斯拉記':36,'尼希米記':37,'歷代志上':38,'歷代志下':39,
    '馬太福音':40,'馬可福音':41,'路加福音':42,'約翰福音':43,'使徒行傳':44,
    '羅馬書':45,'哥林多前書':46,'哥林多後書':47,'加拉太書':48,'以弗所書':49,
    '腓立比書':50,'腓利比書':50,'歌羅西書':51,'帖撒羅尼迦前書':52,'帖撒羅尼迦後書':53,
    '提摩太前書':54,'提摩太後書':55,'提多書':56,'腓利門書':57,'希伯來書':58,
    '雅各書':59,'彼得前書':60,'彼得後書':61,'約翰壹書':62,'約翰一書':62,'約翰貳書':63,'約翰二書':63,
    '約翰參書':64,'約翰三書':64,'猶大書':65,'啟示錄':66
}


bkorder2bk_dict = {
    0:'',
    1:book_list[ 0], 2:book_list[ 1], 3:book_list[ 2], 4:book_list[ 3], 5:book_list[ 4],
    6:book_list[ 5], 7:book_list[ 6], 8:book_list[ 7], 9:book_list[ 8],10:book_list[ 9],
   11:book_list[10],12:book_list[11],13:book_list[12],14:book_list[13],15:book_list[14],
   16:book_list[15],17:book_list[16],18:book_list[17],19:book_list[18],20:book_list[19],
   21:book_list[20],22:book_list[21],23:book_list[22],24:book_list[23],25:book_list[24],
   26:book_list[25],27:book_list[26],28:book_list[27],29:book_list[28],30:book_list[29],
   31:book_list[30],32:book_list[31],33:book_list[32],34:book_list[33],35:book_list[34],
   36:book_list[35],37:book_list[36],38:book_list[37],39:book_list[38],40:book_list[39],
   41:book_list[40],42:book_list[41],43:book_list[42],44:book_list[43],45:book_list[44],
   46:book_list[45],47:book_list[46],48:book_list[47],49:book_list[48],50:book_list[49],
   51:book_list[50],52:book_list[51],53:book_list[52],54:book_list[53],55:book_list[54],
   56:book_list[55],57:book_list[56],58:book_list[57],59:book_list[58],60:book_list[59],
   61:book_list[60],62:book_list[61],63:book_list[62],64:book_list[63],65:book_list[64],
   66:book_list[65],
   67:''
}



'''### clean up punctuation'''


rgx = recompile(r'(?<=\d)[_](?=\d)')


def cleanse_punctuation(inputText, textReplacement):
    txt2 = re.sub(r'[\xa0（）()\'\"「」!！?？.《》＜＞<>〈〉、·・。：:－\-=＝【】,|｜⧸-]', textReplacement, inputText)
    txt3 = rgx.sub(':', txt2)
    return txt3



'''### Run By Your Host System if new audio files are included'''


'''
cd ~/TPPHC/SERMON/VINE/
ls *.mp3 > ~/SOURCE/sermon-app/projects/VINE/ls.txt
'''


with open("../sermon_fs_date_record.txt", "r") as fp:
    lines = [ _.strip() for _ in fp.readlines() ]

fs_c2t_dict = {}
for line in lines:
    if len(line) == 22: # fs date record line format: yyyy-mm-dd xxxxxxxxxxx
        _ = line.split(' ')
        fs_c2t_dict[_[1]] = _[0]


# from full catalog file obtain required info
rdd = sc.textFile('ls.txt')
rdd1 = rdd.map(lambda w: (w[:-18].strip(), w[-16:-5])) \
    .map(lambda w: (w[0], w[1], fs_c2t_dict.get(w[1]))) \
    .map(lambda w: (cleanse_punctuation(w[0], ' '), w[1], w[0], w[2])) \
    .map(lambda w: (w[0].split(' '), w[1], w[-2], w[-1])) \
    .map(lambda w: ([_ for _ in w[0] if len(_) > 0], w[1], w[-2], w[-1]))


print('w[0]= name segments ; w[1]= youtube code ; w[2]= original name ; w[3]= date')
rdd1.take(10)


# data engineering work 1: one-to-many detection
# ideally none are detected
from operator import add
rdd1_checkcode_1tomany = rdd1.map(lambda w: (w[1], 1)).reduceByKey(add)


checkcode_1tomany = rdd1_checkcode_1tomany.map(lambda w: w[1]).collect()


if max(checkcode_1tomany) > 1:
    code_1tomany = rdd1_checkcode_1tomany.filter(lambda w: w[1] > 1).collect()
    print(code_1tomany)
    print("=============================")
    print("need to fix here")
    print("=============================")


# data engineering work 2: preacher stop word
rdd2 = rdd1.map(
    lambda w: ([j for i in preacherTitle_list \
                      for j in w[0] \
                          if i in j \
                              and i != j \
                              and not '傳道書' in j \
                              and not '傳道人' in j \
                              and not '先知的' in j \
                              and not '堅持'   in j ],
               list(set([i for i in book_list for j in w[0] if i in j])),
               w[1], w[-2], w[-1]))


print('w[0]= preacher ; w[1]= book; w[2]= youtube code ; w[3]= original name ; w[4]= date')
# rdd2.take(3)



'''### youtube code : "c"
### sermon youtube title: "s"
c2s_dict : 1-to-1 dictionary from youtube code to sermon youtube title'''


c2s_dict = {} # 1-to-1 dictionary
for (c, s) in rdd2.map(lambda w: (w[2], w[3])).collect():
    c2s_dict[c] = s.strip()



'''### book : "b"
c2b_dict : 1-to-1 dictionary from youtube code to book

b2c_dict : 1-to-N dictionary from book to [ list of youtube code ]'''


rdd2.map(lambda w: (w[2], w[1])).take(3)


c2b_dict = {} # 1-to-1 dictionary
b2c_dict = {} # 1-to-N dictionary
for (c, b) in rdd2.map(lambda w: (w[2], w[1])) \
                  .filter(lambda w: len(w[1]) > 0) \
                  .map(lambda w: (w[0], ''.join(w[1]))).collect():
    # 1-to-1 dictionary
    c2b_dict[c] = b
    # 1-to-N dictionary
    if b in b2c_dict:
        b2c_dict.get(b).append(c)
    else:
        b2c_dict[b] = [c]


rdd2.take(10)



'''### verse : "v"
c2v_dict : 1-to-1 dictionary from youtube code to chapter verse'''


c2v_dict = {} # 1-to-1 dictionary
c2ch_dict = {} # 1-to-1 dictionary
for c in c2s_dict.keys():
    # recall: s := the sermon title
    titleStr = cleanse_punctuation(c2s_dict.get(c), '-')
    # print(titleStr)
    m = re.search(r'(?<=[0-9])[:]', titleStr) # m := match
    if m is None:
        # print("None ...")
        continue
    [i, j] = m.span()
    vStr = ''
    for ii in range(i, 1, -1):
        if titleStr[ii] in '0123456789-:':
            # print(ii, titleStr[ii])
            vStr += titleStr[ii]
        else:
            break
    vStr = vStr[::-1]
    for ii in range(i+1, len(titleStr)):
        if titleStr[ii] in '0123456789-:':
            # print(ii, testStr[ii])
            vStr += titleStr[ii]
        else:
            break
    # if vStr[-1] == '-':
    #     vStr = vStr[:-1]
    while vStr[-1] == '-':
        vStr = vStr[:-1]
    # print(vStr)
    c2v_dict[c] = vStr
    chStr = vStr.split(':')[0]
    if '-' not in chStr:
        c2ch_dict[c] = chStr



'''### time : "t"
c2t_dict : 1-to-1 dictionary from youtube code to time'''


c2t_dict = {} # 1-to-1 dictionary
for (c, t) in rdd2.map(lambda w: (w[2], w[-1])).collect():
    c2t_dict[c] = t



'''### bible verse content: "bvc"
c2bvc_dict : 1-to-1 dictionary from youtubecode to bible verse(s) content'''


bible_srcpath = '../../data/bible_src/cuv2/'


book_list_engsymbol = ['',
    'Gen','Exo','Lev','Num','Deu',
    'Jos','Jug','1Sa','2Sa','1Ki','2Ki',
    'Isa','Jer','Eze',
    'Hos','Joe','Amo','Oba','Jon','Mic',
    'Nah','Hab','Zep','Hag','Zec','Mal',
    'Psa','Pro','Job','Son','Rut','Lam','Ecc',
    'Est','Dan','Ezr','Neh','1Ch','2Ch',
    'Mat','Mak','Luk','Jhn','Act',
    'Rom','1Co','2Co','Gal','Eph',
    'Phl','Col','1Ts','2Ts',
    '1Ti','2Ti','Tit','Phm','Heb',
    'Jas','1Pe','2Pe','1Jn','2Jn',
    '3Jn','Jud','Rev']


c2bvc_dict = {}
for c in list(c2s_dict.keys()):
    bvc = ''
    bk = c2b_dict.get(c)
    if bk is not None:
        # ch = c2ch_dict.get(c)
        v = c2v_dict.get(c)
        if v is not None and ':' in v:
            if not bk in bk2bkorder_dict.keys():
                # print(f'{bk} not in bk-2-bkorder dict keys !, skip and continue !')
                continue
            # print(bk, v)
            srcfname = bible_srcpath + book_list_engsymbol[bk2bkorder_dict.get(bk)] + '.txt'
            with open(srcfname, 'r') as fp:
                bktxtlines = fp.readlines()
            fp.close()
            # --------------------------------------------------
            # compile the starting verse A:B and
            # ending verse C:D from v,
            # then check coverage
            # --------------------------------------------------
            # cn := chapter number
            # vn := verse number
            # case 0 -> A:B
            if v.count(':') == 1 and v.count('-') == 0:
                vs = v.split(':')
                cn1 = vs[0]
                cn2 = cn1
                vn1 = vs[1]
                vn2 = vn1
            # case 1 -> A:B-C
            elif v.count(':') == 1 and v.count('-') == 1:
                vs = v.split(':')
                cn1 = vs[0]
                cn2 = cn1
                vn1 = vs[1].split('-')[0]
                vn2 = vs[1].split('-')[1]
            # case 2 -> A:B-C-D-...-X
            elif v.count(':') == 1 and v.count('-') > 1:
                vs = v.split(':')
                cn1 = vs[0]
                cn2 = cn1
                #vn1 = vs[1].split('-')[0]
                #vn2 = vs[1].split('-')[-1]
                vn1 = str(min([ int(_) for _ in vs[1].split('-') ]))
                vn2 = str(max([ int(_) for _ in vs[1].split('-') ]))
            # case 3 -> A:B-C:D where C > A
            elif v.count(':') == 2 and v.count('-') == 1:
                vs = v.split('-')
                cn1 = vs[0].split(':')[0]
                vn1 = vs[0].split(':')[1]
                cn2 = vs[1].split(':')[0]
                vn2 = vs[1].split(':')[1]
            # case 4 -> otherwise, we dont handle it
            else:
                continue
            # print concluded coverage
            # print(f'{cn1}:{vn1} - {cn2}:{vn2}')
            # --------------------------------------------------
            # END OF check coverage
            # --------------------------------------------------
            header1 = cn1 + '.' + vn1
            header2 = cn2 + '.' + vn2
            # -- -- -- -- -- --
            # cn and vn overflow handling:
            # e.g. 12:1-18 but scripture actually only numbers
            #      the verses 12:1-17, while 12:18 is just the splitted version of 12:17
            # -- -- -- -- -- --
            header2_exists = False
            for bktxtline in bktxtlines:
                if header2 == bktxtline[:len(header2)]:
                    header2_exists = True
                    break
            # if overflow of verses number occurs,
            # update ending verse to become the last verse
            # of the same chapter of starting verse
            h1_reached = False
            header2_curr = header1
            if not header2_exists:
                ch_desired = c2ch_dict.get(c)
                for bktxtline in bktxtlines:
                    if not h1_reached:
                        h1_reached = header1 in bktxtline[:len(header1)]
                    if h1_reached:
                        header2_prev = header2_curr
                        header2_curr = bktxtline.split(' ')[0]
                        ch_curr = bktxtline.split('.')[0]
                        if ch_curr != ch_desired:
                            header2 = header2_prev
                            break
                        else:
                            header2 = header2_curr
            # -- -- -- -- -- --
            # END OF cn and vn overflow handling
            # -- -- -- -- -- --
            # loop through each line until reaching the starting verse
            h1_reached = False
            h2_reached = False
            for bktxtline in bktxtlines:
                # loop through each line until reaching the destinating chapter
                if not h1_reached:
                    h1_reached = header1 in bktxtline[:len(header1)]
                if h1_reached:
                    bvc += bktxtline
                if not h2_reached:
                    h2_reached = header2 in bktxtline[:len(header2)]
                if h2_reached:
                    break
            bvc = bk + ' ' + v + '\n\n' + bvc
            c2bvc_dict[c] = bvc
    # break









'''## rough overview on statistics
number of sermons by each preacher'''








rdd_time = rdd1.map(lambda w: fs_c2t_dict.get(w[1])) \
    .map(lambda w: [ int(_) for _ in w.split('-') ]) \
    .map(lambda w: w[0]*365 + w[1]*30 + w[2])


t_ = sorted(rdd_time.collect())


_ = plt.plot(t_)


print('sermons upload date spans %0.2f years' % round((max(t_) - min(t_)) / 365, 2))









'''## data frame generation

c - b - v - s'''


def get_headerVerseVal(inVerse):
    if ':' in inVerse:
        v = inVerse.split(':')[1]
    else:
        vH = 0
        return vH
    if '-' in v:
        vH = int(v.split('-')[0])
    else:
        vH = int(v)
    return vH


df = pd.DataFrame(
    [
        [c,
         bk2bkorder_dict.get(c2b_dict.get(c), 67),
         c2b_dict.get(c, ''),
         c2ch_dict.get(c, '0'),
         c2v_dict.get(c, ''),
         get_headerVerseVal(c2v_dict.get(c, '')),
         c2s_dict.get(c, ''),
         c2t_dict.get(c, '')] for c in c2s_dict.keys()
    ],
    columns = [
        'code',
        'bkno',
        'book',
        'chapter',
        'verse',
        'headerVerse',
        'title',
        'date'
    ]
)



'''### save the dictionary series'''


with open('code_dictionary.pkl', 'wb') as f:
    pkl.dump([bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict, c2bvc_dict], f)


with open('x2code_dictionary.pkl', 'wb') as f:
    pkl.dump([b2c_dict], f)


df.chapter = pd.to_numeric(df.chapter, errors='coerce')
df = df.sort_values(['date', 'bkno', 'chapter', 'headerVerse', 'title']) # use headerVerse for verse-wise sorting
df = df.drop(columns='headerVerse') # throw away headerVerse column as it is not included in final df


for index, row in df.iterrows():
    print(row['code'], row['book'], row['chapter'], row['verse'], row['title'], row['date'])


df.to_csv('./index_byt.csv', index=False)








_ = os.system('rm -f videos download.sh')








