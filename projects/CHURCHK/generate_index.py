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
# import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

import itertools
import collections

import pickle as pkl

import re
from re import compile as recompile








# the initial of different kind of preacher
preacherTitle_list = ['博士','牧師','傳道','老師','先生','教授','弟兄','社長', '神學生', '師母']


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








def func_retrieve_title_from_html(inhlines):
    for hline in inhlines:
        if "<h2 class=\"white\">" in hline:
            break
    if hline == "</html>": # criteria true if search pattern is not in inhlines
        return None
    try:
        titlestr = re.findall(r">.*<", hline)[0]
        titlestr = titlestr[1:-1]
    except:
        titlestr = None
    return titlestr


def func_retrieve_preacher_from_html(inhlines):
    for hline, rowIdx in zip(inhlines, range(len(inhlines))):
        if "講員：" in hline and "語言：" in inhlines[rowIdx+1]:
            break
    if hline == "</html>": # criteria true if search pattern is not in inhlines
        return None
    try:
        preacherstr = re.findall(r"'>.*</a></span><br>", hline)[0]
        preacherstr = preacherstr[2:-15]
    except:
        preacherstr = None
    return preacherstr


def func_retrieve_scripture_from_html(inhlines):
    for hline, rowIdx in zip(inhlines, range(len(inhlines))):
        if "s = '" in hline and "經文" in inhlines[rowIdx+1]:
            break
    if hline == "</html>": # criteria true if search pattern is not in inhlines
        return None
    try:
        scripturestr = re.findall(r"s = '.*'.replace", hline)[0]
        scripturestr = scripturestr[5:-9]
        scripturestr = scripturestr.replace(" ", "")
    except:
        scripturestr = None
    return scripturestr


def func_retrieve_date_from_html(inhlines):
    for hline, rowIdx in zip(inhlines, range(len(inhlines))):
        if "s = '20" in hline and "日期" in inhlines[rowIdx+1]:
            break
    if hline == "</html>": # criteria true if search pattern is not in inhlines
        return None
    try:
        datestr = re.findall(r"20[0-9][0-9]-[0-9]*-[0-9]*", hline)[0]
        datestr_seg = datestr.split("-")
        yystr = datestr_seg[0]
        mmstr = datestr_seg[1]
        if len(mmstr) < 2:
            mmstr = "0" + mmstr
        ddstr = datestr_seg[2]
        if len(ddstr) < 2:
            ddstr = "0" + ddstr
        datestr = "-".join([yystr, mmstr, ddstr])
    except:
        datestr = None
    return datestr








churchk_src_dir = os.getcwd() + "/church.com.hk.html/"
files_in_curr_dir = os.listdir(churchk_src_dir)
files_in_curr_dir.sort()


html_file_found = False
for filename in files_in_curr_dir:
    if ".html" in filename:
        html_file_found = True
        break
if not html_file_found:
    print("no new html file found !")
    print("exit() !")
    exit()


new_html_results = []
for filename in files_in_curr_dir:
    if ".html" in filename:
        # ==========================
        # initialize target results
        # ==========================
        titlestr = None
        preacherstr = None
        scripturestr = None
        bookstr = []
        chapterstr = None
        versestr = None
        datestr = None
        # ==========================
        code_curr = filename.replace(".html", "")
        with open(churchk_src_dir+filename, "r") as fp:
            hlines = [ _.strip() for _ in fp.readlines() ]
        # ==========================
        # obtain title
        # ==========================
        titlestr = func_retrieve_title_from_html(hlines)
        if titlestr is None:
            print(f"new sermon {code_curr} title None ! skip {code_curr} ...")
            print(f"go check https://www.church.com.hk/acms/content.asp?site=cdc&op=show&type=product&code={code_curr}&layout=sermon")
            continue
        else:
            print(f"new sermon {code_curr} title {titlestr}")
        # ==========================
        # obtain preacher
        # ==========================
        preacherstr = func_retrieve_preacher_from_html(hlines)
        if preacherstr is None:
            print(f"new sermon {code_curr} preacher None !")
        else:
            print(f"new sermon {code_curr} preacher {preacherstr}")
        # ==========================
        # obtain scripture
        # ==========================
        scripturestr = func_retrieve_scripture_from_html(hlines)
        if scripturestr is None:
            bookstr = None
            versestr = None
            print(f"new sermon {code_curr} scripture None !")
        else:
            print(f"new sermon {code_curr} scripture: {scripturestr}")
            # ==========================
            # obtain book
            # ==========================
            try:
                for bk in book_list:
                    if bk in scripturestr:
                        bookstr.append(bk)
                if len(bookstr): # there has matched book name
                    bookstr = list(set(bookstr)) # deduplicate
                    bookstr = bookstr[0]
                else:
                    bookstr = None
            except:
                bookstr = None
            if bookstr is None:
                versestr = None
                print(f"new sermon {code_curr} book None !")
            else:
                print(f"new sermon {code_curr} book: {bookstr}")
                # ==========================
                # obtain verse
                # ==========================
                try:
                    m = re.search(r'(?<=[0-9])[:]', scripturestr) # m := match
                    if m is None:
                        versestr = None
                    else:
                        [i, j] = m.span()
                        versestr = ''
                        for ii in range(i, 1, -1):
                            if scripturestr[ii] in '0123456789-:':
                                # print(ii, scripturestr[ii])
                                versestr += scripturestr[ii]
                            else:
                                break
                        versestr = versestr[::-1]
                        for ii in range(i+1, len(scripturestr)):
                            if scripturestr[ii] in '0123456789-:':
                                # print(ii, scripturestr[ii])
                                versestr += scripturestr[ii]
                            else:
                                break
                        while versestr[-1] == '-':
                            versestr = versestr[:-1]
                except:
                    vsersestr = None
                if versestr is None:
                    print(f"new sermon {code_curr} verse None !")
                else:
                    print(f"new sermon {code_curr} verse: {versestr}")
                    # ==========================
                    # obtain chapter
                    # ==========================
                    try:
                        chapterstr = versestr.split(":")[0]
                    except:
                        chapterstr = None
                    if chapterstr is None:
                        print(f"new sermon {code_curr} chapter None !")
                    else:
                        print(f"new sermon {code_curr} chapter: {chapterstr}")
        # ==========================
        # obtain date
        # ==========================
        datestr = func_retrieve_date_from_html(hlines)
        if datestr is None:
            print(f"new sermon {code_curr} date None !")
        else:
            print(f"new sermon {code_curr} date: {datestr}")
        # ==========================
        new_html_results.append([\
            code_curr, \
            preacherstr, \
            bookstr, \
            chapterstr, \
            versestr, \
            titlestr, \
            datestr \
        ])
        print()



'''### code : "c"
### sermon title: "s"
c2s_dict : 1-to-1 dictionary from code to sermon title'''


c2s_dict = {} # 1-to-1 dictionary
# new_html_results: [code, preacher, book, chapter, verse, title, date]
for new_html_entry in new_html_results:
    c2s_dict[new_html_entry[0]] = new_html_entry[5]



'''### preacher : "p"
c2p_dict : 1-to-1 dictionary from code to preacher name

p2c_dict : 1-to-N dictionary from preacher name to [ list of code ]'''


c2p_dict = {} # 1-to-1 dictionary
p2c_dict = {} # 1-to-N dictionary
# new_html_results: [code, preacher, book, chapter, verse, title, date]
for new_html_entry in new_html_results:
    # 1-to-1 dictionary
    c2p_dict[new_html_entry[0]] = new_html_entry[1]
    print(new_html_entry[0], new_html_entry[1])
    # 1-to-N dictionary
    if new_html_entry[1] in p2c_dict:
        p2c_dict.get(new_html_entry[1]).append(new_html_entry[0])
    else:
        p2c_dict[new_html_entry[1]] = [new_html_entry[0]]



'''### book : "b"
c2b_dict : 1-to-1 dictionary from code to book

b2c_dict : 1-to-N dictionary from book to [ list of code ]'''


c2b_dict = {} # 1-to-1 dictionary
b2c_dict = {} # 1-to-N dictionary
# new_html_results: [code, preacher, book, chapter, verse, title, date]
for new_html_entry in new_html_results:
    # 1-to-1 dictionary
    c2b_dict[new_html_entry[0]] = new_html_entry[2]
    print(new_html_entry[0], new_html_entry[2])
    # # 1-to-N dictionary
    # if new_html_entry[2] in b2c_dict:
    #     b2c_dict.get(new_html_entry[2]).append(new_html_entry[0])
    # else:
    #     b2c_dict[new_html_entry[2]] = [new_html_entry[0]]



'''### verse : "v"
c2v_dict : 1-to-1 dictionary from youtube code to chapter verse'''


c2v_dict = {} # 1-to-1 dictionary
c2ch_dict = {} # 1-to-1 dictionary
# new_html_results: [code, preacher, book, chapter, verse, title, date]
for new_html_entry in new_html_results:
    # 1-to-1 dictionary
    c2v_dict[new_html_entry[0]] = new_html_entry[4]
    print(new_html_entry[0], new_html_entry[4])
    # 1-to-N dictionary
    c2ch_dict[new_html_entry[0]] = new_html_entry[3]
    print(new_html_entry[0], new_html_entry[3])



'''### time : "t"
c2t_dict : 1-to-1 dictionary from youtube code to time'''


c2t_dict = {} # 1-to-1 dictionary
# new_html_results: [code, preacher, book, chapter, verse, title, date]
for new_html_entry in new_html_results:
    c2t_dict[new_html_entry[0]] = new_html_entry[6]



'''### bible verse content: "bvc"
c2bvc_dict : 1-to-1 dictionary from youtubecode to bible verse(s) content'''


# bible_srcpath = '../../data/bible_src/cuv2/'


# book_list_engsymbol = ['',
#     'Gen','Exo','Lev','Num','Deu',
#     'Jos','Jug','1Sa','2Sa','1Ki','2Ki',
#     'Isa','Jer','Eze',
#     'Hos','Joe','Amo','Oba','Jon','Mic',
#     'Nah','Hab','Zep','Hag','Zec','Mal',
#     'Psa','Pro','Job','Son','Rut','Lam','Ecc',
#     'Est','Dan','Ezr','Neh','1Ch','2Ch',
#     'Mat','Mak','Luk','Jhn','Act',
#     'Rom','1Co','2Co','Gal','Eph',
#     'Phl','Col','1Ts','2Ts',
#     '1Ti','2Ti','Tit','Phm','Heb',
#     'Jas','1Pe','2Pe','1Jn','2Jn',
#     '3Jn','Jud','Rev']


# c2bvc_dict = {}
# for c in list(c2s_dict.keys()):
#     bvc = ''
#     bk = c2b_dict.get(c)
#     if bk is not None:
#         # ch = c2ch_dict.get(c)
#         v = c2v_dict.get(c)
#         if v is not None and ':' in v:
#             if not bk in bk2bkorder_dict.keys():
#                 # print(f'{bk} not in bk-2-bkorder dict keys !, skip and continue !')
#                 continue
#             # print(bk, v)
#             srcfname = bible_srcpath + book_list_engsymbol[bk2bkorder_dict.get(bk)] + '.txt'
#             with open(srcfname, 'r') as fp:
#                 bktxtlines = fp.readlines()
#             fp.close()
#             # --------------------------------------------------
#             # compile the starting verse A:B and
#             # ending verse C:D from v,
#             # then check coverage
#             # --------------------------------------------------
#             # cn := chapter number
#             # vn := verse number
#             # case 0 -> A:B
#             if v.count(':') == 1 and v.count('-') == 0:
#                 vs = v.split(':')
#                 cn1 = vs[0]
#                 cn2 = cn1
#                 vn1 = vs[1]
#                 vn2 = vn1
#             # case 1 -> A:B-C
#             elif v.count(':') == 1 and v.count('-') == 1:
#                 vs = v.split(':')
#                 cn1 = vs[0]
#                 cn2 = cn1
#                 vn1 = vs[1].split('-')[0]
#                 vn2 = vs[1].split('-')[1]
#             # case 2 -> A:B-C-D-...-X
#             elif v.count(':') == 1 and v.count('-') > 1:
#                 vs = v.split(':')
#                 cn1 = vs[0]
#                 cn2 = cn1
#                 #vn1 = vs[1].split('-')[0
#                 #vn2 = vs[1].split('-')[-1]
#                 vn1 = str(min([ int(_) for _ in vs[1].split('-') ]))
#                 vn2 = str(max([ int(_) for _ in vs[1].split('-') ]))
#             # case 3 -> A:B-C:D where C > A
#             elif v.count(':') == 2 and v.count('-') == 1:
#                 vs = v.split('-')
#                 cn1 = vs[0].split(':')[0]
#                 vn1 = vs[0].split(':')[1]
#                 cn2 = vs[1].split(':')[0]
#                 vn2 = vs[1].split(':')[1]
#             # case 4 -> otherwise, we dont handle it
#             else:
#                 continue
#             # print concluded coverage
#             # print(f'{cn1}:{vn1} - {cn2}:{vn2}')
#             # --------------------------------------------------
#             # END OF check coverage
#             # --------------------------------------------------
#             header1 = cn1 + '.' + vn1
#             header2 = cn2 + '.' + vn2
#             # -- -- -- -- -- --
#             # cn and vn overflow handling:
#             # e.g. 12:1-18 but scripture actually only numbers
#             #      the verses 12:1-17, while 12:18 is just the splitted version of 12:17
#             # -- -- -- -- -- --
#             header2_exists = False
#             for bktxtline in bktxtlines:
#                 if header2 == bktxtline[:len(header2)]:
#                     header2_exists = True
#                     break
#             # if overflow of verses number occurs,
#             # update ending verse to become the last verse
#             # of the same chapter of starting verse
#             h1_reached = False
#             header2_curr = header1
#             if not header2_exists:
#                 ch_desired = c2ch_dict.get(c)
#                 for bktxtline in bktxtlines:
#                     if not h1_reached:
#                         h1_reached = header1 in bktxtline[:len(header1)]
#                     if h1_reached:
#                         header2_prev = header2_curr
#                         header2_curr = bktxtline.split(' ')[0]
#                         ch_curr = bktxtline.split('.')[0]
#                         if ch_curr != ch_desired:
#                             header2 = header2_prev
#                             break
#                         else:
#                             header2 = header2_curr
#             # -- -- -- -- -- --
#             # END OF cn and vn overflow handling
#             # -- -- -- -- -- --
#             # loop through each line until reaching the starting verse
#             h1_reached = False
#             h2_reached = False
#             for bktxtline in bktxtlines:
#                 # loop through each line until reaching the destinating chapter
#                 if not h1_reached:
#                     h1_reached = header1 in bktxtline[:len(header1)]
#                 if h1_reached:
#                     bvc += bktxtline
#                 if not h2_reached:
#                     h2_reached = header2 in bktxtline[:len(header2)]
#                 if h2_reached:
#                     break
#             bvc = bk + ' ' + v + '\n\n' + bvc
#             c2bvc_dict[c] = bvc
#     # break









'''## rough overview on statistics
number of sermons by each preacher'''


for preacher in sorted([ k_ for k_ in p2c_dict.keys() if k_ is not None ]):
    print('%s : %d' % (preacher, len(p2c_dict.get(preacher))))


c2p_dict








# rdd_time = rdd2.map(lambda w: w[4]) \
#    .map(lambda w: [int(_) for _ in w.split('-')]) \
#    .map(lambda w: w[0]*365 + w[1]*30 + w[2])


# t_ = sorted(rdd_time.collect())


# # _ = plt.plot(t_)


# print('sermons upload date spans %0.2f years' % round((max(t_) - min(t_)) / 365, 2))









'''## data frame generation

c - p - b - v - s'''


def get_headerVerseVal(inVerse):
    if inVerse is None:
        vH = 0
        return vH
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


[ c2b_dict.get(c) for c in c2s_dict.keys() ]


df = pd.DataFrame(
    [
        [c,
         c2p_dict.get(c, ''),
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
        'preacher',
        'bkno',
        'book',
        'chapter',
        'verse',
        'headerVerse',
        'title',
        'date'
    ]
)


print(df)


df



'''### save the dictionary series'''


# with open('code_dictionary.pkl', 'wb') as f:
#     pkl.dump([c2p_dict, bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict, c2bvc_dict], f)


# with open('x2code_dictionary.pkl', 'wb') as f:
#     pkl.dump([p2c_dict, b2c_dict], f)


# df.chapter = pd.to_numeric(df.chapter, errors='coerce')
# df = df.sort_values(['date'])
# df = df.drop(columns='headerVerse') # throw away headerVerse column as it is not included in final df


# for index, row in df.iterrows():
#     print(row['code'], row['preacher'], row['book'], row['chapter'], row['verse'], row['title'], row['date'])








def integrate_to_existing_index_file(indf):
    existing_filename = "index_byc.csv"
    latest_filename = "index_output_latest.csv"
    indf.to_csv(latest_filename, index=False)
    
    if os.path.exists(existing_filename):
        headerline = ""
        with open(existing_filename, "r") as fp:
            indexlines = [ _.strip() for _ in fp.readlines() if len(_.strip()) ]
        headerline = indexlines[0]
        indexlines = indexlines[1:]
        with open(latest_filename, "r") as fp:
            indexlines_latest = [ _.strip() for _ in fp.readlines() if len(_.strip()) ]
        indexlines_latest = indexlines_latest[1:]
        indexlines_total = [ headerline ] + sorted(list(set(indexlines + indexlines_latest)))
        with open(existing_filename, "w") as fp:
            for line in indexlines_total:
                fp.write(line + "\n")
    else:
        indf.to_csv(existing_filename, index=False)








integrate_to_existing_index_file(df)








_ = os.system("rm -f index_output_latest.csv")


_ = os.system("rm -f videos download.sh")


_ = os.system("rm -f " + churchk_src_dir + "*.html")








