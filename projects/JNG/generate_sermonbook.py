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
print('done !')


with open("code_dictionary.pkl", "rb") as fp:
    c2p_dict, bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict, c2bvc_dict = pkl.load(fp)
fp.close()


with open("x2code_dictionary.pkl", "rb") as fp:
    p2c_dict, b2c_dict = pkl.load(fp)
fp.close()


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
    txt2 = txt2.replace('$','\$') # preserve this here since its higher priority than in html arguments
    txt2 = rgx.sub(r'$\1^\2$', txt2)
    for rep_ in rep_list:
        txt2 = txt2.replace(rep_[0], rep_[1])
    txt2 = txt2.replace('&', ' and ') # preserve this here since its lower priority than in html arguments
    txt2 = txt2.strip()
    return txt2


with open('../rep_whisper_trailing.txt', 'r') as fp:
    whisper_trailing_rep_list = [ cleanse_special_char(_.strip()) for _ in fp.readlines() ]
fp.close()


p_list = list(p2c_dict.keys())
print(p_list)


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


def sermon_tex_from_year(yyyy_start, yyyy_end):
    # yyyy_start : starting year, e.g. 2012
    # yyyy_end.  : ending year, e.g. 2018
    progressStepCnt = 0
    # --------------------------------------
    # read the index table and only take
    # into account within desired year range
    # --------------------------------------
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: reading in full index file")
    with open('./index_byp.csv', 'r') as fp:
        lines = fp.readlines()
    fp.close()
    lines = [ line \
                 for line in lines \
                     if check_in_year_range(
                         line.split(',')[-1],
                         [yyyy_start,yyyy_end]
                     )
            ]
    sermon_tex_filepath = f"../../build/JNG/sermon_JNG_{str(yyyy_start)}-{str(yyyy_end)[-2:]}.tex"
    # --------------------------------------
    # print the latex document : prefix
    # --------------------------------------
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: printing out prefixing")
    _ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/J. Ng 頻道輯錄 粵語講道逐字稿 {str(yyyy_start)}-{str(yyyy_end)[-2:]}/' | sed 's/Youtube Channel:/Youtube Channel: JohnsonNg/' > " + sermon_tex_filepath)

    # --------------------------------------
    # index table partitioned by preachers
    # --------------------------------------
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
                    c2s_dict.get(cc, ' ').replace('_','\_').replace('&','\&')
                )
                tstr = c2t_dict.get(cc, ' ')
                ystr = "\\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ " + cc.replace('_','\_') + "}}"
                fp.write(bstr + ' ' + vstr + " & " \
                         + "\\hyperref[sec:"+cc.replace('-','_')+"]{"+sstr+"}" + " & " \
                         + tstr + " & " \
                         + ystr \
                         + " \\\\\n")
        fp.write("\\end{xltabular}\n")
        # --------------------------------------
        # end of partitioned-by-preachers table
        # --------------------------------------
        fp.write("}\n")
        print('sermon count in current book: %d' % sermonCnt)
    fp.close()

    # --------------------------------------
    # per-preacher index and sermon content
    # --------------------------------------
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
            print(f"{lineId+1} of {len(lines)}")
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
                                c2s_dict.get(cc_, ' ').replace('_','\_').replace('&','\&')
                            )
                            tstr = c2t_dict.get(cc_, ' ')
                            ystr = "\\href{https://youtube.com/watch?v=" + cc_ +"}{\\texttt{ " + cc_.replace('_','\_') + "}}"
                            fp.write(bstr + ' ' + vstr + " & " \
                                     + "\\hyperref[sec:"+cc_.replace('-','_')+"]{"+sstr+"}" + " & " \
                                     + tstr + " & " \
                                     + ystr \
                                     + " \\\\\n")
                    fp.write("\\hline\n")
                    fp.write("\\end{xltabular}\n")
                    fp.write("}\n")
                    # END OF chapter tabular-toc with sermon title
                    # ------------------------------------
                    fp.write("\\newpage\n\n")
                fp.close()
            with open(sermon_tex_filepath, "a") as fp:
                #fp.write("\n\n\\section{"+c2s_dict.get(cc).replace('_','\\_')+"}\n")
                sectionNameStr = ''
                b = c2b_dict.get(cc)
                sectionNameStr += b if b is not None else ''
                v = c2v_dict.get(cc)
                sectionNameStr += ' ' + v if b is not None and v is not None else ''
                ch = c2ch_dict.get(cc)
                sectionNameStr += ' ' + ch if b is not None and ch is not None and v is None else ''
                fp.write("\n\n\\section{"+sectionNameStr+"}\n")
                fp.write("\\label{sec:"+cc.replace('-','_')+"}\n")
                sstr = cleanse_special_char(
                    c2s_dict.get(cc).replace('_','\_').replace('&','\&')
                )
                fp.write("\\textbf{"+sstr+"}\n")
                fp.write("\\newline\n\\newline\n")
                fp.write("連結: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ https://youtube.com/watch?v=" + cc.replace('_','\_') + "}} ~~~~ 語音日期: " + c2t_dict.get(cc) + " \n")
                fp.write("\\newline\n\\newline\n")
                fp.write("\\hyperref[sec:"+cc_prev.replace('-','_')+"]{< < < PREV SERMON < < <}\n")
                fp.write("~\n")
                fp.write("\\hyperlink{toc}{[返主目錄]}\n")
                fp.write("~\n")
                fp.write("\\hyperref[ch:preacher"+str(p_id)+"]{[返講員目錄]}\n")
                fp.write("~\n")
                fp.write("\\hyperref[sec:"+cc_next.replace('-','_')+"]{> > > NEXT SERMON > > >}\n")
                fp.write("\\newline\n\\newline\n")
            fp.close()
            # _ = os.system(f"cat ../data/JNG/{cc}.txt >> " + sermon_tex_filepath)
            with open(sermon_tex_filepath, "a") as fp:
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
                                bvc_line = bvc_line[:si].replace(".",":") +  " & " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line[si+1:]
                                nli = bvc_line.find(" \\\\") # newline char index
                                bvc_line = bvc_line[:nli] + " \\end{tabularx}" + bvc_line[nli:]
                            fp.write(bvc_line)
                    fp.write("[1ex]\n")
                    fp.write("\\hline\n\\hline\n")
                    fp.write("\\end{longtable}\n")
                # ----------------------
                # add the sermon part
                with open("../../data/JNG/"+cc+".txt", "r") as fp_:
                    the_sermon_text = fp_.read()
                fp_.close()
                the_sermon_text = cleanse_special_char(the_sermon_text)
                the_sermon_text = the_sermon_text.replace("\\n\\n","\\n")
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
            fp.close()

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



'''## 2012-2018 Sermons'''


sermon_tex_from_year(2012, 2018)



'''## 2019-2020 Sermons'''


sermon_tex_from_year(2019,2020)



'''## 2021-2022 Sermons'''


sermon_tex_from_year(2021,2022)



'''## 2023-2024 Sermons'''


sermon_tex_from_year(2023,2024)








