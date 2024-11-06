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


with open('../rep_common.txt', 'r') as fp:
    rep_list = [ _.strip() for _ in fp.readlines() ]
fp.close()
rep_list = [ _.split(", '", 1) for _ in rep_list ]
rep_list = [ [_[0], _[1][:-1]] for _ in rep_list ]


# compile regular expression rgx to cater math symbol '^'
rgx = re.compile(r'([A-Za-z0-9=+\-]+)\^([A-Za-z0-9=+\-]+)')
print('checking of "rgx.sub(r\'$\\1^\\2$\', \'E=MC^-2\')" :', rgx.sub(r'$\1^\2$', 'E=MC^-2'))


def cleanse_special_char(inputText):
    txt2 = inputText
    txt2 = txt2.replace('$','\$') # preserve this here since its higher priority than in html arguments
    txt2 = rgx.sub(r'$\1^\2$', txt2)
    for rep_ in rep_list:
        txt2 = txt2.replace(rep_[0], rep_[1])
    txt2 = txt2.replace('&', ' and ') # preserve this here since its lower priority than in html arguments
    txt2 = txt2.strip()
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
sermon_tex_filepath = '../../build/DSCCC/sermon_DSCCC_2009-present.tex'
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/香港中文大學崇基神學院~~校牧主日崇拜講章~~2009-present/' | sed 's/Youtube Channel:/Chaplaincy, Divinity School of Chung Chi College, CUHK/' > " + sermon_tex_filepath)

# --------------------------------------
# index table
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC")

# year integer for comparison
y_prev = -1
y_curr = -1
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
    fp.write("日期 & 講員 & 經課 & 講題 \\\\ \\hline \\hline\n")
    for index, row in df.iterrows():
        dt = row['date']
        y_curr = int(dt / 10000) # obtain current sermon's year integer
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
        # if year is progressed, add a hline
        if y_prev != y_curr:
            toc_tex_str += "\\hline "
            y_prev = y_curr
        # if year-month is progressed, add a hline
        if ym_prev != ym_curr:
            toc_tex_str += "\\hline\n"
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
        print(preacher)
        toc_tex_str += cleanse_special_char(preacher) + " & "
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
            fp.write("\n\n\\newpage\n\n\\section{" + cleanse_special_char(titlestr) + "}\n")
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
                    for char_idx, char_curr in enumerate(bv):
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
                        for char_idx, char_curr in enumerate(bv_seg):
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
                        ch_desired = cn2 #c2ch_dict.get(c)
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








