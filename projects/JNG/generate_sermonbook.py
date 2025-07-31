#!/usr/local/bin/python3



from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err


import os.path
import pickle as pkl
import re
#from re import compile as recompile
import pandas as pd
print('done !')


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


c2p_dict   = {}
c2b_dict   = {}
c2ch_dict  = {}
c2v_dict   = {}
c2s_dict   = {}
c2t_dict   = {}
c2bvc_dict = {}

df = pd.read_csv('index_byp.csv')
for d in df.iterrows():
    df_row = d[1]
    c2p_dict[df_row['code']]  = df_row['preacher'] if not pd.isna(df_row['preacher']) else ' '
    c2b_dict[df_row['code']]  = df_row['book']     if not pd.isna(df_row['book']) else ' '
    c2ch_dict[df_row['code']] = df_row['chapter']  if not pd.isna(df_row['chapter']) else ' '
    c2v_dict[df_row['code']]  = df_row['verse']    if not pd.isna(df_row['verse']) else ' '
    c2s_dict[df_row['code']]  = df_row['title']
    c2t_dict[df_row['code']]  = df_row['date']
    c = df_row['code']
    bvc = ''
    bk = c2b_dict.get(c)
    if bk is not None:
        # ch = c2ch_dict.get(c)
        v = c2v_dict.get(c)
        if pd.isna(v):
            continue
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
                #vn1 = vs[1].split('-')[0
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

p_list = sorted([ _ for _ in list(set(list(df['preacher']))) if not pd.isna(_) ])       
print(sorted(p_list))


# with open("code_dictionary.pkl", "rb") as fp:
#     c2p_dict, bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict, c2bvc_dict = pkl.load(fp)
# fp.close()


# with open("x2code_dictionary.pkl", "rb") as fp:
#     p2c_dict, b2c_dict = pkl.load(fp)
# fp.close()


# # generate
# preacher 1
#  --------------------------------
# | Book  Ch:Vs  Theme  Date  Code
# |--------------------------------
# |  .
# |  .
# |  .
# |
#  --------------------------------
#
# preacher 2
#  --------------------------------
# | Book  Ch:Vs  Theme  Date  Code
# |--------------------------------
# |  .
# |  .
# |  .
# |
#  --------------------------------
#









'''### print the latex document : sermon content'''


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
    txt2 = txt2.replace('$', '\\$') # preserve this here since its higher priority than in html arguments
    txt2 = rgx.sub(r'$\1^\2$', txt2)
    for rep_ in rep_list:
        txt2 = txt2.replace(rep_[0], rep_[1])
    txt2 = txt2.replace('&', ' and ') # preserve this here since its lower priority than in html arguments
    txt2 = txt2.strip()
    return txt2


with open('../rep_whisper_trailing.txt', 'r') as fp:
    whisper_trailing_rep_list = [ cleanse_special_char(_.strip()) for _ in fp.readlines() ]
fp.close()


def check_in_year_range(code, year_range=[2012,2018]):
    # tstr = c2t_dict.get(code, ' ')
    # # print(tstr)
    in_range = False
    for yr in range(year_range[0], year_range[1] + 1):
        # if str(yr) in tstr:
        if str(yr) in code:
            in_range = True
            break
    return in_range


with open("./index_byp.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


print('all time sermon count:',
    len( lines )
     )


print('2012-2018 sermon count:',
    len(   [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [2012,2018]
                     )
            ] )
     )


print('2019-2020 sermon count:',
    len(   [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [2019,2020]
                     )
            ] )
     )


print('2021-2022 sermon count:',
    len(   [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [2021,2022]
                     )
            ] )
     )


print('2023-2024 sermon count:',
    len(   [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [2023,2024]
                     )
            ] )
     )


def print_prefix(sermon_tex_filepath, yyyy_start, yyyy_end, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: printing out prefixing")
    _ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/J. Ng 頻道輯錄 粵語講道逐字稿 {str(yyyy_start)}-{str(yyyy_end)[-2:]}/' | sed 's/Youtube Channel:/Youtube Channel: JohnsonNg/' > " + sermon_tex_filepath)
    return progressStepCnt


def write_toc(sermon_tex_filepath, index_file, toc_type, yyyy_start, yyyy_end, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: reading in full index file")
    with open(index_file, 'r') as fp:
        lines = fp.readlines()
    lines = [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [yyyy_start, yyyy_end]
                     )
            ]

    progressStepCnt += 1
    print(f"Step {progressStepCnt}: writing TOC which gathers up all preachers")
    with open(sermon_tex_filepath, "a") as fp:
        sermonCnt = 0
        p_prev = ''
        p_curr = ''
        p_id = 0
        fp.write("{ \\scriptsize\n")
        # --------------------------------------
        # start of partitioned-by-preachers table
        # --------------------------------------
        fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
        fp.write("\\hline\n")
        # --------------------------------------
        # lines is the line content in index_byp
        # --------------------------------------
        for lineId, line in enumerate(lines):
            cc = line.split(",")[0]
            # --------------------------------------
            # only include this code cc if it is
            # ready in the transcription folder
            # --------------------------------------
            if os.path.isfile(f'../../data/JNG/{cc}.txt'):
                sermonCnt += 1
                p_prev = p_curr
                p_curr = c2p_dict.get(cc)
                if p_prev != p_curr:
                    p_id += 1
                    fp.write("\\multicolumn{4}{c}{} \\\\\n")
                    fp.write("\\multicolumn{4}{c}{\\hyperref[ch:preacher"+str(p_id)+"]{"+p_curr+"}} \\\\\n") # <----------- this defines the column num
                    fp.write("\\multicolumn{4}{c}{} \\\\\n")
                    fp.write("\\hline\n")
                bstr = c2b_dict.get(cc, ' ')
                vstr = c2v_dict.get(cc, ' ')
                sstr = cleanse_special_char(
                    c2s_dict.get(cc, ' ').replace('_', '\\_').replace('&', '\\&')
                )
                tstr = c2t_dict.get(cc, ' ')
                ystr = "\\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{" + cc.replace('_', '\\_') + "}}"
                fp.write(bstr + ' ' + vstr + " & " \
                         + "\\hyperref[sec:"+cc.replace('-', '_')+"]{"+sstr+"}" + " & " \
                         + tstr + " & " \
                         + ystr \
                         + " \\\\\n")
        fp.write("\\end{xltabular}\n")
        # --------------------------------------
        # end of partitioned-by-preachers table
        # --------------------------------------
        fp.write("}\n")
        print('sermon count in current book: %d' % sermonCnt)
    return progressStepCnt


def write_preacher_toc(fp, p_id, p_curr, lines):
    # ------------------------------------
    # chapter toc
    fp.write("\n\n\\chapter{"+p_curr+"}")
    fp.write("\label{ch:preacher"+str(p_id)+"}\n")
    fp.write("\\begin{multicols}{3}\n")
    fp.write("\\minitoc\n")
    fp.write("\\end{multicols}\n")
    # END OF chapter toc
    # ------------------------------------
    # ------------------------------------
    # chapter tabular-toc with sermon title
    fp.write("{ \\scriptsize\n")
    fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
    fp.write("\\hline\n")
    for lineId_, line_ in enumerate(lines):
        cc_ = line_.split(",")[0]
        if os.path.isfile(f'../../data/JNG/{cc_}.txt') and p_curr == c2p_dict.get(cc_):
            bstr = c2b_dict.get(cc_, ' ')
            vstr = c2v_dict.get(cc_, ' ')
            sstr = cleanse_special_char(
                c2s_dict.get(cc_, ' ').replace('_', '\\_').replace('&', '\&')
            )
            tstr = c2t_dict.get(cc_, ' ')
            ystr = "\\href{https://youtube.com/watch?v=" + cc_ +"}{\\texttt{" + cc_.replace('_', '\\_') + "}}"
            fp.write(bstr + ' ' + vstr + " & " \
                        + "\\hyperref[sec:"+cc_.replace('-', '_')+"]{"+sstr+"}" + " & " \
                        + tstr + " & " \
                        + ystr \
                        + " \\\\\n")
    fp.write("\\hline\n")
    fp.write("\\end{xltabular}\n")
    fp.write("}\n")
    # END OF chapter tabular-toc with sermon title
    # ------------------------------------
    fp.write("\\newpage\n\n")


def add_section_title(fp, cc_prev, cc, cc_next, p_id):
    sectionNameStr = ''
    b = c2b_dict.get(cc)
    sectionNameStr += b if b is not None else ''
    v = c2v_dict.get(cc)
    sectionNameStr += ' ' + v if b is not None and v is not None else ''
    ch = c2ch_dict.get(cc)
    sectionNameStr += ' ' + ch if b is not None and ch is not None and v is None else ''
    fp.write("\n\n\\section{"+sectionNameStr+"}\n")
    fp.write("\\label{sec:"+cc.replace('-', '_')+"}\n")
    sstr = cleanse_special_char(
        c2s_dict.get(cc).replace('_', '\\_').replace('&', '\\&')
    )
    fp.write("\\textbf{"+sstr+"}\n")
    fp.write("\\newline\n\\newline\n")
    fp.write("連結: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{https://youtube.com/watch?v=" + cc.replace('_', '\\_') + "}} ~~~~ 語音日期: " + c2t_dict.get(cc) + "\n")
    fp.write("\\newline\n\\newline\n")
    fp.write("\\hyperref[sec:"+cc_prev.replace('-', '_')+"]{< < < PREV SERMON < < <}\n")
    fp.write("~\n")
    fp.write("\\hyperlink{toc}{[返主目錄]}\n")
    fp.write("~\n")
    fp.write("\\hyperref[ch:preacher"+str(p_id)+"]{[返講員目錄]}\n")
    fp.write("~\n")
    fp.write("\\hyperref[sec:"+cc_next.replace('-', '_')+"]{> > > NEXT SERMON > > >}\n")
    fp.write("\\newline\n\\newline\n")


def add_scripture_text(fp, cc):
    # ----------------------
    # add the scripture part if not None
    bvc_curr = c2bvc_dict.get(cc)
    if bvc_curr is not None:
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
                    bvc_line = bvc_line[:si].replace(".", ":") + " & " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line[si+1:]
                    nli = bvc_line.find(" \\\\") # newline char index
                    bvc_line = bvc_line[:nli] + " \\end{tabularx}" + bvc_line[nli:]
                fp.write(bvc_line)
        fp.write("[1ex]\n")
        fp.write("\\hline\n\\hline\n")
        fp.write("\\end{longtable}\n")


def add_sermon_text(fp, cc):
    # ----------------------
    # add the sermon part
    with open("../../data/JNG/"+cc+".txt", "r") as fp_:
        the_sermon_text = fp_.read()
    fp_.close()
    the_sermon_text = cleanse_special_char(the_sermon_text)
    the_sermon_text = the_sermon_text.replace("\\n\\n", "\\n")
    textlines = the_sermon_text.split("\n")
    _textrow_cnt = 0
    textline_prev = ''
    for textline in textlines:
        # ----------------------------------------------------------------------
        # check if whisper_trailing_rep_list any 2 match
        iterator = iter(whisper_trailing_rep_list)
        matchCnt = 0
        # Use the next function to retrieve the elements of the iterator
        try:
            while True:
                ele = next(iterator)
                if ele in textline:
                    matchCnt += 1
        except StopIteration:
            pass
        whisper_trailing_pattern_match = matchCnt >= 2
        # END OF check if whisper_trailing_rep_list any 2 match
        # ----------------------------------------------------------------------
        if textline == textline_prev:
            textline_prev = textline
            continue
        elif re.sub(r'[()]', '', textline.strip()) in whisper_trailing_rep_list:
            continue
        elif whisper_trailing_pattern_match:
            continue
        else:
            textline_prev = textline
        _textrow_cnt += 1
        if _textrow_cnt % 40 == 1:
            fp.write("$^{%d}$" % _textrow_cnt)
        if textline.count('$') == 1:
            # if the text line contains odd number of
            # dollar sign '$', it would probably bring up error
            # over 95% of the situation is that there only has 1 '$' sign
            textline = textline.replace('$', '\\$')
        fp.write(textline + "\n")
        if _textrow_cnt % 40 == 0:
            fp.write("\n")
    fp.write("\\newpage\n\n")


def generate_preacher_sections(sermon_tex_filepath, index_file, toc_type, yyyy_start, yyyy_end, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: reading in full index file")
    with open(index_file, 'r') as fp:
        lines = fp.readlines()
    lines = [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [yyyy_start, yyyy_end]
                     )
            ]

    progressStepCnt += 1
    print(f"Step {progressStepCnt}: generate per-preacher TOC for each preacher section")
    p_prev = ''
    p_curr = ''
    p_id = 0
    cc_prev = ''
    cc_next = ''
    # --------------------------------------
    # lines is the line content in index_byp
    # --------------------------------------
    for lineId, line in enumerate(lines):
        if (lineId+1) % 100 == 0:
            print(f"{lineId+1} of {len(lines)} in {sermon_tex_filepath}")
        cc = line.split(",")[0]
        cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
        cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
        if os.path.isfile(f'../../data/JNG/{cc}.txt'):
            p_prev = p_curr
            p_curr = c2p_dict.get(cc)
            if p_prev != p_curr:
                progressStepCnt += 1
                print(f"Step {progressStepCnt}: a new preacher {p_curr} is reached !")
                p_id += 1
                with open(sermon_tex_filepath, "a") as fp:
                    write_preacher_toc(fp, p_id, p_curr, lines)
            with open(sermon_tex_filepath, "a") as fp:
                add_section_title(fp, cc_prev, cc, cc_next, p_id)
                add_scripture_text(fp, cc)
                add_sermon_text(fp, cc)
    return progressStepCnt


def add_afterword_and_postfix(sermon_tex_filepath):
    """Adds the afterword and postfix to the LaTeX file."""
    os.system("cat ../afterword.tex >> " + sermon_tex_filepath)
    os.system("cat ../postfix.tex >> " + sermon_tex_filepath)


def sermon_tex_from_year(yyyy_start, yyyy_end):
    sermon_tex_filepath = f"../../build/JNG/sermon_JNG_{str(yyyy_start)}-{str(yyyy_end)[-2:]}.tex"
    progressStepCnt = 0

    # Step 1: Print LaTeX prefix
    progressStepCnt = print_prefix(sermon_tex_filepath, yyyy_start, yyyy_end, progressStepCnt)

    # Step 2: Write Table of Contents (TOC)
    progressStepCnt = write_toc(sermon_tex_filepath, './index_byp.csv', 'preacher', yyyy_start, yyyy_end, progressStepCnt)

    # Step 3: Generate per-preacher TOC and sermon content
    progressStepCnt = generate_preacher_sections(sermon_tex_filepath, './index_byp.csv', 'preacher', yyyy_start, yyyy_end, progressStepCnt)

    # Step 4: Add afterward and postfix
    add_afterword_and_postfix(sermon_tex_filepath)

    print("done!")



'''## 2012-2018 Sermons'''


sermon_tex_from_year(2012, 2018)



'''## 2019-2020 Sermons'''


sermon_tex_from_year(2019,2020)



'''## 2021-2022 Sermons'''


sermon_tex_from_year(2021,2022)



'''## 2023-2024 Sermons'''


sermon_tex_from_year(2023,2024)



'''## 2025-2026 Sermons'''


sermon_tex_from_year(2025,2026)








