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

import math

import re
from re import compile as recompile

print('done !')
# with open("./index_byd.csv", "r") as fp:
#     lines = fp.readlines()
# fp.close()
df = pd.read_csv("./index_byd.csv")
print(f"total entry count: {df['date'].count()}")
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
def cleanse_special_char(inputText):
    txt2 = inputText \
        .replace("#", "\\#") \
        .replace("$", "\\$") \
        .replace("（", "(") \
        .replace("）", ")") \
        .replace("？", "?") \
        .replace("！", "!") \
        .replace("，", ",") \
        .replace("。", ".") \
        .replace("、", ",") \
        .replace("「", "``") \
        .replace("」", "\"") \
        .replace("：", ":") \
        .replace('&nbsp;', '') \
        .replace('&quot;', '\'') \
        .replace('&#39;', '\'') \
        .replace('&ldquo;', '``') \
        .replace('&rdquo;', '"') \
        .replace('&lsquo;', '`') \
        .replace('&rsquo;', '\'') \
        .replace('&hellip;', '...') \
        .replace('&Omicron;', '零') \
        .replace('&mdash;', '─') \
        .replace('&ndash;', '─') \
        .replace('\\tab', ' ') \
        .replace('\\cs16', '') \
        .replace(' &divide;', '$\\div$') \
        .replace(' X ', '$\\times$') \
        .replace('&eacute;', '\\\'e') \
        .replace('ἵ', 'ι') \
        .replace('&nu;', 'ν') \
        .replace('&alpha;', 'α') \
        .replace('&beta;', 'β') \
        .replace('&gamma;', 'γ') \
        .replace('&delta;', 'δ') \
        .replace('&epsilon;', 'ε') \
        .replace('&sigma;', 'σ') \
        .replace('&iota;', 'ι') \
        .replace('&sigmaf;', 'ς') \
        .replace('-&gt', '$\rightarrow$') \
        .replace('שְׁאוֹל&lrm;', '\sblgoodhebrew{שְׁאוֹל}') \
        .replace('&middot;', '$\\,\\cdot\\,$') \
        .replace("&amp;", '') \
        .replace('哋', '地') \
        .replace('嚟', '黎') \
        .replace('嘅', 'ge ') \
        .replace('喺', '係') \
        .replace('㗎', '架') \
        .replace('咗', 'jor ') \
        .replace('嗰', 'gwo ') \
        .replace('啲', 'D ') \
        .replace('嗱', 'la ') \
        .replace('嘢', 'ye ') \
        .replace('裏', '裡') \
        .replace('産', '產') \
        .replace('啱', 'arm ') \
        .replace('唞', '抖') \
        .replace('啓', '啟') \
        .replace('攞', 'lor ') \
        .replace('啫', 'je ') \
        .replace('噃', 'bor ') \
        .replace('吖', '呀') \
        .replace('噏', 'up ') \
        .replace('爲', '為') \
        .replace('揾', '搵') \
        .replace('揸', 'zar ') \
        .replace('揼', 'dump ') \
        .replace('圣', '聖') \
        .replace('冚', 'cum ') \
        .replace('絶', '絕') \
        .replace('衞', '衛') \
        .replace('誔', '誕') \
        .replace('歴', '歷') \
        .replace('亜', '亞') \
        .replace('様', '樣') \
        .replace('祢', '你') \
        .replace('窰', 'yiu ') \
        .replace('纪', '記') \
        .replace('緃', '縱') \
        .replace('约', '約') \
        .replace('櫈', '凳') \
        .replace('枱', '台') \
        .replace('喐', 'yuk ') \
        .replace('氹', 'tum ') \
        .replace('着', '著') \
        .replace('孭', 'meh ') \
        .replace('瞓', '訓') \
        .replace('嫲', '麻') \
        .replace('嘥', 'sai ') \
        .replace('嘭', 'bang ') \
        .replace('軚', 'tie ') \
        .replace('揦', 'la ') \
        .replace('恒', '恆') \
        .replace('滙', '匯') \
        .replace('啩', '掛') \
        .replace('肶', '脾') \
        .replace('糭', '粽') \
        .replace('糉', '粽') \
        .replace('邨', '村') \
        .replace('冧', 'lum ') \
        .replace('㖭', '添') \
        .replace('攰', 'gui ') \
        .replace('埗', 'Po ') \
        .replace('燶', 'lone ') \
        .replace('峯', '峰') \
        .replace('餸', 'sung ') \
        .replace('忟', 'mung ') \
        .replace('両', '兩') \
        .replace('掹', 'mung ') \
        .replace('吔', 'ye ') \
        .replace('綫', '線') \
        .replace('乸', '痴') \
        .replace('菓', 'gwo ') \
        .replace('嘞', '啦') \
        .replace('吡', '悲') \
        .replace('劏', 'tong ') \
        .replace('喼', 'gip ') \
        .replace('睺', 'hau ') \
        .replace('脷', '利') \
        .replace('濶', '闊') \
        .replace('紥', 'zhak ') \
        .replace('踎', 'mau ') \
        .replace('鈎', '勾') \
        .replace('廸', 'dik ') \
        .replace('噔', '等') \
        .replace('梘', 'gang ') \
        .replace('厠', '廁') \
        .replace('糍', 'chi ') \
        .replace('搲', '掘') \
        .replace('㷫', 'hing ') \
        .replace('㷫', 'hing ') \
        .replace('丶', '. ') \
        .replace('晩', '晚') \
        .replace('㷛', '煲') \
        .replace('眞', '真') \
        .replace('等', '等') \
        .replace('丿', '. ') \
        .replace('銹', '鏽') \
        .replace('曱甴', '小強') \
        .replace('鎅', 'gai ') \
        .replace('踭', 'zoung ') \
        .replace('牀', '床') \
        .replace('唥', 'lang ') \
        .replace('曺', '嘈') \
        .replace('㩒', '禁') \
        .replace('抺', '抹') \
        .replace('敍', '敘') \
        .replace('叙', '敘') \
        .replace('腭', 'ngok ') \
        .replace('衆', '眾') \
        .replace('哣', '逗') \
        .replace('刧', '劫') \
        .replace('鱲', 'Lap ') \
        .replace('儍', 'sor ') \
        .replace('丨', '. ') \
        .replace('錬', '鏈') \
        .replace('畀', '比') \
        .replace('喆', '. ') \
        .replace('裇', 'seuk ') \
        .replace('镕', 'yeun ') \
        .replace('効', '效') \
        .replace('酦', '. ') \
        .replace('劵', '券') \
        .replace('粧', '裝') \
        .replace('卽', '即') \
        .replace('㬹', 'zoung ') \
        .replace('啰', 'lor ') \
        .replace('栢', '柏') \
        .replace('鰂', '魚則') \
        .replace('逹', '達') \
        .replace('堃', '坤') \
        .replace('讃', '讚') \
        .replace('⾃', '自') \
        .replace('频', '頻') \
        .replace('记', '記') \
        .replace('话', '話') \
        .replace('竉', '寵') \
        .replace('呑', '吞') \
        .replace('傈', '僳') \
        .replace('淸', '清') \
        .replace('寛', '寬') \
        .replace('唿', '弗') \
        .replace('叁', '參') \
        .replace('唓', '即係') \
        .replace('嘣', '崩') \
        .replace('廻', '迴') \
        .replace('麽', '麼') \
        .replace('猬', '蝟') \
        .replace('綉', '繡') \
        .replace('箓', '籙') \
        .replace('氷', '冰') \
        .replace('祎', '禕') \
        .replace('咔', 'ka ') \
        .replace('&', ' and ') \
        .replace('羣', '群') \
        .replace('鍳', '鑒') \
        .replace('僞', '偽') \
        .replace('\ue226', '祐') \
        .replace('隣', '鄰') \
        .replace('\u200b', '') \
        .replace('\u3000', '~') \
        .replace('\ue233', '身') \
        .replace('\ue313', '涉') \
        .replace('\ue314', '麃') \
        .replace('\ue2de', '鬮') \
        .replace('\ue2df', '鬥') \
        .replace('\ue096', '芒') \
        .replace('\ue0e1', '載') \
        .replace('\ue05e', '瑟') \
        .replace('\ue05e', '繫') \
        .replace('\ue052', '的') \
        .replace('\ue05e', '配') \
        .replace('\ue010', '憂') \
        .replace('\ue0f5', '付') \
        .replace('\ue17a', '使') \
        .replace('\ue031', '步') \
        .replace('\ue315', '犁') \
        .replace('\ue339', '草') \
        .replace('\ue14c', '冤') \
        .replace('释', '釋') \
        .replace('义', '義') \
        .replace('请', '請') \
        .replace('没', '沒') \
        .replace('赋', '賦') \
        .replace('诗', '詩') \
        .replace('稣', '穌') \
        .replace('细', '細') \
        .replace('随', '隨') \
        .replace('细', '細') \
        .replace('终', '終') \
        .replace('残', '殘') \
        .replace('结', '結') \
        .replace('给', '給') \
        .replace('内', '內') \
        .replace('统', '統') \
        .replace('强', '強') \
        .replace('课', '課') \
        .replace('别', '別') \
        .replace('专', '專') \
        .replace('却', '卻') \
        .replace('\ue1f5', '') \
        .replace('\ue1f5', '') \
        .replace('\ue045', '實') \
        .replace('\ue00e', '洶') \
        .replace('窑', 'yiu') \
        .replace('躭', '耽') \
        .replace('\ue097', '呔') \
        .replace('亘', '亙') \
        .replace('‐', '-') \
        .replace('犠', '犧') \
        .replace('怱', '匆') \
        .replace('｣', '」') \
        .replace('｢', '「') \
        .replace('﹑', '、') \
        .replace('寃', '冤') \
        .replace('閙', '鬧') \
        .replace('虚', '虛') \
        .replace('温', '溫') \
        .replace('凖', '準') \
        .replace('墻', '牆') \
        .replace('侓', '律') \
        .replace('﹣', '-') \
        .replace('踪', '蹤') \
        .replace('鐧', '簡') \
        .replace('袮', '你') \
        .replace('涶', '唾') \
        .replace('説', '說') \
        .replace('駡', '罵') \
        .strip()
    return txt2
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
bible_srcpath = '../../data/bible_src/cuv2/'
book_list_engsymbol = [
    'Gen','Exo','Lev','Num','Deu',
    'Jos','Jug','Rut','1Sa','2Sa','1Ki','2Ki',
    '1Ch','2Ch','Ezr','Neh','Est',
    'Job','Psa','Pro','Ecc','Son',
    'Isa','Jer','Lam','Eze','Dan',
    'Hos','Joe','Amo','Oba','Jon','Mic',
    'Nah','Hab','Zep','Hag','Zec','Mal',
    'Mat','Mak','Luk','Jhn','Act',
    'Rom','1Co','2Co','Gal','Eph',
    'Phl','Col','1Ts','2Ts',
    '1Ti','2Ti','Tit','Phm','Heb',
    'Jas','1Pe','2Pe','1Jn','2Jn',
    '3Jn','Jud','Rev']

'''## Start of sermon tex generation'''
# def sermon_tex_generation():
progressStepCnt = 0
sermon_tex_filepath = '../../build/DSCCC/sermon_DSCCC.tex'
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/崇基神學院 崇拜講章/' | sed 's/Youtube Channel:/Chaplaincy, Div. Scl. of CCC/' > " + sermon_tex_filepath)

# --------------------------------------
# index table
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC")

# year-month integer for comparison
ym_prev = -1
ym_curr = -1
with open(sermon_tex_filepath, "a") as fp:
    fp.write("\\section{目錄}\\label{sec:toc}\n")
    fp.write("{ \\scriptsize\n")
    fp.write("\n\n\\begin{xltabular}{\\textwidth}" + \
             "{|p{0.15\\textwidth}|p{0.15\\textwidth}|p{0.4\\textwidth}|p{0.3\\textwidth}|}\n")
    # lllr: |Date | Preacher | Title | Coverage |
    #        0.15   0.15    0.3        0.4
    fp.write("\\hline\n")
    fp.write("日期 & 講員 & 經課 & 講題 \\\\\n")
    for index, row in df.iterrows():
        dt = row['date']
        ym_curr = int(dt / 100) # obtain current sermon's year-month integer
        sermondt = str(dt)
        titlestr = row['title']
        preacher = row['preacher']
        if is_float(row['coverage']):
            bv = ''
        else:
            bv = row['coverage']
        # ---------------------------------------------
        # start of tex string content
        # preparation for current item
        # ---------------------------------------------
        toc_tex_str = ""
        # if year-month is changed, add double hline for spacing
        if ym_prev != ym_curr:
            toc_tex_str += "\\hline\n\\hline\n"
            ym_prev = ym_curr
        dt_ = ''
        dt_ += sermondt[0:4] + '年'
        if sermondt[4] != '0':
            dt_ += sermondt[4]
        dt_ += sermondt[5] + '月'
        if sermondt[6] != '0':
            dt_ += sermondt[6]
        dt_ += sermondt[7] + '日'
        toc_tex_str += dt_ + " & "
        toc_tex_str += preacher + " & "
        toc_tex_str += bv + " & "
        toc_tex_str += "\hyperref[sec:"+str(index)+"]{"+cleanse_special_char(titlestr)+"} \\\\\n"
        fp.write(toc_tex_str)
    fp.write("\\end{xltabular}\n\n")
    # --------------------------------------
    # end of TOC
    # --------------------------------------
    fp.write("}\n") # end of fp.write("{ \\scriptsize\n")
fp.close()
# --------------------------------------
# END OF index table
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: generate main content")
dsccc_path = '../../data/DSCCC/'
index_prev = '' # previous sermon dataframe index
index_curr = '' # current sermon dataframe index
index_next = '' # next sermon dataframe index

# to regex search url pattern
url_pattern_regexp = re.compile(r'[A-Za-z0-9/_\-?.=&:]')

for index, row in df.iterrows():
    # if index == 512:
    #     break
    if (index+1) % 100 == 0:
        print(f"{index+1} / {df['date'].count()}")
    # index for latex cross reference
    index_curr = index
    index_prev = max(index_curr-1, 0)
    index_next = index_curr+1
    # get ready the dictionary info
    sermondt = str(row['date'])
    titlestr = row['title']
    titlestr = cleanse_special_char(titlestr)
    preacher = row['preacher']
    preacher = cleanse_special_char(preacher)
    if is_float(row['coverage']):
        bv = ''
    else:
        bv = row['coverage']
    dsccc_sermon_pathfilename = f'{dsccc_path}{sermondt}_{titlestr}.txt'
    if os.path.isfile(dsccc_sermon_pathfilename):
        # --------------------------------------
        # read in sermon
        # --------------------------------------
        with open(dsccc_sermon_pathfilename, 'r') as fp_dsccc_src:
            sermon_lines = fp_dsccc_src.readlines()
            sermon_lines = [ sermon_line.strip() for sermon_line in sermon_lines if '_sermon' not in sermon_line]
            sermon_lines = [ sermon_line for sermon_line in sermon_lines if len(sermon_line) ]
        fp_dsccc_src.close()
        with open(sermon_tex_filepath, "a") as fp:
            # --------------------------------------
            # print out sermon headers
            # --------------------------------------
            fp.write("\n\n\\newpage\n\n\\section{" + titlestr + "}\n")
            fp.write("\\label{sec:" + str(index_curr) + "}\n")
            fp.write("\\textbf{" + cleanse_special_char(sermon_lines[0]) + "}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("\\hyperref[sec:"+str(index_prev)+"]{< < < PREV SERMON < < <}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:toc]{[返目錄]}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:"+str(index_next)+"]{> > > NEXT SERMON > > >}\n")
            fp.write("\n\n")
            # --------------------------------------
            # print out sermon bible verse coverage (if any)
            # --------------------------------------
            #print(f"bible coverage: {bv}")
            bkCnt = bv.count(';')+1
            if bv == '':
                bkCnt = 0
            #print(f"number of books: {bkCnt}")
                # **************************************
                # **************************************
                # **************************************
                #     ||||                      ||||
                #     ||||         START        ||||
                #     ||||       GET BIBLE      ||||
                #     ||||   SCRIPTURE VERSE    ||||
                #     ||||                      ||||
                #        \\\\                ////
                #           \\\\          ////
                #              \\\\    ////
                #                   v
                # --------------------------------------
                # retrieve bible chapters and
                # verses coverage ( if any )
                # --------------------------------------
            if bkCnt > 0:
                chisymbol_list = []
                engsymbol_list = []
                cv_list = []
                bkFound = False
                if bkCnt == 1:
                    for (chisymbol, engsymbol) in zip(book_list, book_list_engsymbol):
                        if chisymbol in bv:
                            chisymbol_list.append(chisymbol)
                            engsymbol_list.append(engsymbol)
                            bkFound = True
                    for char_idx in range(len(bv)):
                        char_curr = bv[char_idx]
                        if char_curr not in '0123456789:-,':
                            continue
                        else:
                            cv_list.append(bv[char_idx:])
                            break
                else: # i.e. if there are more books,
                    # then we need to capture bv in sequential order
                    bv_segments = bv.split(';')
                    for bv_seg in bv_segments:
                        for (chisymbol, engsymbol) in zip(book_list, book_list_engsymbol):
                            if chisymbol in bv_seg:
                                chisymbol_list.append(chisymbol)
                                engsymbol_list.append(engsymbol)
                                bkFound = True
                        cv_curr = ''
                        for char_idx in range(len(bv_seg)):
                            char_curr = bv_seg[char_idx]
                            if char_curr not in '0123456789:-,':
                                continue
                            elif char_curr == ';':
                                break
                            else:
                                cv_curr += char_curr
                        cv_list.append(cv_curr)
                # print(f'book found ! {chisymbol_list} {engsymbol_list}')
                # print(cv_list)
                # print()
                bvc = []
                for (chisymbol, engsymbol, v) in zip(chisymbol_list, engsymbol_list, cv_list):
                    # print(f" to cater{chisymbol} {v}")
                    bvc_curr = ''
                    srcfname = bible_srcpath + engsymbol + ".txt"
                    with open(srcfname, 'r') as fp_bible:
                        bktxtlines = fp_bible.readlines()
                    fp_bible.close()
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
                        if ',' in vn1:
                            vn1 = vn1.split(',')[0]
                        elif ',' in vn2:
                            vn2 = vn2.split(',')[-1]
                    # case 2 -> A:B-C-D-...-X
                    elif v.count(':') == 1 and v.count('-') > 1:
                        vs = v.split(':')
                        cn1 = vs[0]
                        cn2 = cn1
                        vn1 = vs[1].split('-')[0]
                        vn2 = vs[1].split('-')[-1]
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
                            bvc_curr += bktxtline
                        if not h2_reached:
                            h2_reached = header2 in bktxtline[:len(header2)]
                        if h2_reached:
                            break
                    bvc.append(chisymbol + ' ' + v + '\n\n' + bvc_curr)
                # END OF for (chisymbol, engsymbol, v) in zip(chisymbol_list, engsymbol_list, cv_list):
                # print(bvc)
                # if len(bvc) == 0:
                #     print(bv)
                #     print(bvc)
                #                   ^
                #              ////    \\\\
                #           ////          \\\\
                #        ////                \\\\
                #     ||||                      ||||
                #     ||||         FINISH       ||||
                #     ||||       GET BIBLE      ||||
                #     ||||   SCRIPTURE VERSE    ||||
                #     ||||                      ||||
                # **************************************
                # **************************************
                # **************************************
                # ----------------------
                # add the scripture part
                for bvc_curr in bvc:
                    # bvc is the list of scripture.
                    # often there contains 3 to 4 books
                    bvc_curr = bvc_curr.split("\n")
                    # first row shall be book + verse info
                    bvc_line = bvc_curr[0].strip() + "\n"
                    fp.write(bvc_line)
                    fp.write("\\newline\n")
                    fp.write("\\begin{longtable}{cl}\n")
                    fp.write("\\hline\n\\hline\n")
                    fp.write("章節 & 經文 (和合本修訂版)\\\\\n")
                    fp.write("\\hline\n")
                    for bvc_line in bvc_curr[1:]:
                        bvc_line = bvc_line.strip()
                        if len(bvc_line) > 0:
                            if bvc_line != [ _.strip() for _ in bvc_curr if len(_.strip()) ][-1]:
                                bvc_line += " \\\\ \\\\ \\relax\n"
                            else:
                                bvc_line += " \\\\ \\\\\n"
                            si = bvc_line.find(" ")
                            if si == -1:
                                bvc_line = "& " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line + " \\end{tabularx}"
                            else:
                                bvc_line = bvc_line[:si].replace(".",":") +  " & " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line[si+1:]
                                nli = bvc_line.find(" \\\\") # newline char index
                                bvc_line = bvc_line[:nli] + " \\end{tabularx}" + bvc_line[nli:]
                            fp.write(bvc_line)
                    fp.write("[1ex]\n")
                    fp.write("\\hline\n\\hline\n")
                    fp.write("\\end{longtable}\n")
            # --------------------------------------
            # print out sermon main content
            # --------------------------------------
            for sermon_line in sermon_lines[1:]: # the first line is already textbf above
                # --------------------------------------
                # tex url handling multiple number of http in the same line
                # --------------------------------------
                urlidx_start = 0
                urlidx_end = 0
                while urlidx_start != -1:
                    urlidx_start = sermon_line.find('http', urlidx_end) # find 'http' pattern
                    urlidx_end = urlidx_start
                    for char_curr in sermon_line[urlidx_start:]:
                        if url_pattern_regexp.search(char_curr):
                            urlidx_end += 1
                        else:
                            break
                    if urlidx_start != -1: # if 'http' pattern is never found, it is -1
                        sermon_line = sermon_line[:urlidx_start] + "\\url{" + sermon_line[urlidx_start:urlidx_end] + "}" + sermon_line[urlidx_end:]
                fp.write(cleanse_special_char(sermon_line) + "\n\n")
        fp.close() # close of with open(sermon_tex_filepath, "a") as fp:
    else:
        print(f"{dsccc_sermon_pathfilename} is not found !")
        continue
progressStepCnt += 1
print(f"Step {progressStepCnt}: generate afterward and postfix")
# --------------------------------------
# print the latex document : afterword
# --------------------------------------
_ = os.system("cat ../afterword.tex >> " + sermon_tex_filepath)
# --------------------------------------
# print the latex document : postfix
# --------------------------------------
_ = os.system("cat ../postfix.tex >> " + sermon_tex_filepath)
print("done !")


