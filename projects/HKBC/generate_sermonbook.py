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
import re


with open("./index_byc.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


print('all time sermon count:',
    len( lines )
     )








def cleanse_p_tag_span_tag(inputText):
    txt2 = re.sub(r'<.+?>', '', inputText)
    return txt2


with open('../rep_common.txt', 'r') as fp:
    rep_list = [ _.strip() for _ in fp.readlines() ]
fp.close()
rep_list = [ _.split(", '", 1) for _ in rep_list ]
rep_list = [ [_[0], _[1][:-1]] for _ in rep_list ]


def cleanse_special_char(inputText):
    txt2 = inputText
    for rep_ in rep_list:
        txt2 = txt2.replace(rep_[0], rep_[1])
    txt2 = txt2.replace('&', ' and ') # preserve this here since is lower priority than in html arguments
    txt2 = txt2.strip()
    return txt2


def sermonBibleVersesCoverageRetrieval(pathfilename):
    with open(pathfilename, "r") as fp:
        lines = fp.readlines()
    fp.close()
    c_v_line = ''
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


# sermonBibleVersesCoverageRetrieval("../../data/HKBC/1312")


with open("./index_byc.csv", "r") as fp:
    lines = fp.readlines()
fp.close()

for lineId in range(len(lines)):
    line = lines[lineId]
    line_contents = line.split(",")
    s_curr = line_contents[0]
    if os.path.isfile(f'../../data/HKBC/{s_curr}'):
        sermonBibleVersesCoverageRetrieval(f'../../data/HKBC/{s_curr}')


def sermonContentRetrieval(pathfilename):
    with open(pathfilename, "r") as fp:
        lines = fp.readlines()
    fp.close()
    sermon_text = []
    for line in lines:
        if "<p style=" in line and "text-align:" in line and "justify;" in line:
            # print((cleanse_p_tag_span_tag(line)).strip())
            line = (cleanse_p_tag_span_tag(line)).strip()
            line = cleanse_special_char(line).strip()
            sermon_text.append(line)
    return sermon_text








# progressStepCnt = 0
# --------------------------------------
# read the index table and only take
# --------------------------------------
# progressStepCnt += 1
# print(f"Step {progressStepCnt}: reading in full index file")
print("reading in full index file")
with open("./index_byc.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


bible_srcpath = '../../data/bible_src/cuv2/'


book_list_engsymbol = ['',
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


def sermon_tex_from_generation(confno_start, confno_end):
    progressStepCnt = 0
    str_year_start = str(1928+confno_start-1)
    if 1928+confno_end-1 < 2008:
        str_year_end = str(1928+confno_end-1)
    else:
        str_year_end = 'present'
    sermon_tex_filepath = f'../../build/HKBC/sermon_HKBC_{str_year_start}-{str_year_end}.tex'
    # --------------------------------------
    # print the latex document : prefix
    # --------------------------------------
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: printing out prefixing")
    _ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/港九培靈研經會講章/' | sed 's/Youtube Channel:/Hong Kong Bible Conference {str_year_start}-{str_year_end}/' > " + sermon_tex_filepath)

    # --------------------------------------
    # index table
    # --------------------------------------
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: writing TOC")
    with open(sermon_tex_filepath, "a") as fp:
        fp.write("\\section{目錄}\\label{sec:toc}\n")
        fp.write("{ \\scriptsize\n")
        fp.write("\n\n\\begin{xltabular}{\\textwidth}" + \
                 "{|p{0.08\\textwidth} p{0.07\\textwidth} p{0.25\\textwidth}|p{0.15\\textwidth} p{0.35\\textwidth}|}\n")
        # lllr: |Conference No.  Lecture No. | bk+v | Preacher| Title |
        #        0.08            0.07          0.25   0.15      0.45 
        fp.write("\\hline\n")
        fp.write("屆別 & 講號 & 經卷參照 & 講員 & 講題 \\\\\n")
        conf_no_prev = ''
        for line in lines[1:]: # skip the first row (header row)
            line_content = line.split(',')
            conf_no = line_content[2].strip()
            # handle whether current entry belongs to conf no of interest
            if int(conf_no) < confno_start or int(conf_no) > confno_end:
                continue
            lect_no = line_content[3].strip()
            title_str = cleanse_special_char(line_content[4].strip())
            bv = line_content[6].strip()+line_content[7].strip() # might be empty string
            preacher = line_content[1].strip()
            code = line_content[0].strip()
            toc_tex_str = ""
            if conf_no != conf_no_prev:
                toc_tex_str += "\\hline\n\\hline\n"
                conf_no_prev = conf_no
            toc_tex_str += "第"+conf_no+"屆 & "
            toc_tex_str += "第"+lect_no+"講 & "
            toc_tex_str += bv+" & "+preacher+" & "
            toc_tex_str += "\hyperref[sec:"+code+"]{"+cleanse_special_char(title_str)+"} \\\\\n"
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
    hkbc_path = '../../data/HKBC/'
    s_prev = '' # previous HKBC html conference session & lecture number id code
    s_curr = '' # current HKBC html conference session & lecture number id code
    s_next = '' # next HKBC html conference session & lecture number id code

    # --------------------------------------
    # lines is the line content in index_byc
    # --------------------------------------
    for lineId in range(1,len(lines)):
        if (lineId+1) % 100 == 0:
            print(f"{lineId+1} of {len(lines)}")
        line = lines[lineId]
        line_contents = line.split(",")
        s_curr = line_contents[0]
        s_prev = lines[(lineId-1)%len(lines)].split(",")[0]
        s_next = lines[(lineId+1)%len(lines)].split(",")[0]
        p_curr = line_contents[1].strip() # preacher name
        cn_curr = line_contents[2].strip() # conference no.
        ln_curr = line_contents[3].strip() # lecture no.
        t_curr = cleanse_special_char(line_contents[4]) # full title
        # handle whether current entry belongs to conf no of interest
        if int(cn_curr) < confno_start or int(cn_curr) > confno_end:
            continue
        if os.path.isfile(f'{hkbc_path}{s_curr}'):
            # --------------------------------------
            # print out lecture title and misc. info
            # --------------------------------------
            with open(sermon_tex_filepath, "a") as fp:
                sectionNameStr = ''
                sectionNameStr = f'第{cn_curr}屆~港九培靈會~{p_curr}~{t_curr.split(" ", 1)[0]}'
                fp.write("\n\n\\newpage\n\n\\section{"+sectionNameStr+"}\n")
                fp.write("\\label{sec:"+s_curr+"}\n")
                fp.write("\\textbf{"+t_curr.split(" ", 1)[-1]+"}\n")
                fp.write("\\newline\n\\newline\n")
                fp.write(
                    "連結: \\href{https://www.hkbibleconference.org/session-message/view/" \
                    +s_curr \
                    +"}{\\texttt{https://www.hkbibleconference.org/session-message/view/" \
                    +s_curr \
                    +"}}\n"
                )
                fp.write("\\newline\n\\newline\n")
                fp.write("\\hyperref[sec:"+s_prev+"]{< < < PREV SERMON < < <}\n")
                fp.write("~\n")
                fp.write("\\hyperref[sec:toc]{[返目錄]}\n")
                fp.write("~\n")
                fp.write("\\hyperref[sec:"+s_next+"]{> > > NEXT SERMON > > >}\n")
                fp.write("\\newline\n\\newline\n")
            fp.close()
            pathfilename = f"{hkbc_path}{s_curr}"
            b_n = line_contents[5] # book number
            if len(b_n) > 0:
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
                srcfname = bible_srcpath + book_list_engsymbol[int(b_n)] + ".txt"
                with open(srcfname, 'r') as fp:
                    bktxtlines = fp.readlines()
                fp.close()
                v_n = line_contents[7].strip() # verse number
                # assumed format is c1:v1-c2:c2
                c1v1 = v_n.split('-')[0].replace(':','.')
                c2v2 = v_n.split('-')[1].replace(':','.')
                bvc = []
                c1v1_reached = False
                c2v2_reached = False
                for bktxtline in bktxtlines:
                    if c1v1 in bktxtline:
                        c1v1_reached = True
                    if c1v1_reached:
                        bvc.append(bktxtline)
                        if c1v1 == c2v2:
                            break
                    if c2v2 in bktxtline:
                        c2v2_reached = True
                    if c2v2_reached:
                        break
                if len(bvc) > 0:
                    with open(sermon_tex_filepath, "a") as fp:
                        # first row shall be book + verse info
                        fp.write(f"{line_contents[6]} {line_contents[7]}")
                        fp.write("\\newline\n")
                        fp.write("\\begin{longtable}{cl}\n")
                        fp.write("\\hline\n\\hline\n")
                        fp.write("章節 & 經文 (和合本修訂版)\\\\\n")
                        fp.write("\\hline\n")
                        for bvc_line in bvc:
                            bvc_line = bvc_line.strip()
                            if len(bvc_line) > 0:
                                if bvc_line != [ _.strip() for _ in bvc if len(_.strip()) ][-1]:
                                    bvc_line += " \\\\ \\\\ \\relax\n"
                                else:
                                    bvc_line += " \\\\ \\\\\n"
                                si = bvc_line.find(" ")
                                if si == -1:
                                    bvc_line = "& " \
                                        + "\\begin{tabularx}{0.7\\textwidth}{X} " \
                                        + bvc_line \
                                        + " \\end{tabularx}"
                                else:
                                    bvc_line = bvc_line[:si].replace(".",":") \
                                        +  " & " \
                                        + "\\begin{tabularx}{0.7\\textwidth}{X} " \
                                        + bvc_line[si+1:]
                                    nli = bvc_line.find(" \\\\") # newline char index
                                    bvc_line = bvc_line[:nli] + " \\end{tabularx}" + bvc_line[nli:]
                                fp.write(bvc_line)
                        fp.write("[1ex]\n")
                        fp.write("\\hline\n\\hline\n")
                        fp.write("\\end{longtable}\n")
                    fp.close()
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
            # --------------------------------------
            # retrieve lecture content
            # --------------------------------------
            sermon_text_lines = sermonContentRetrieval(pathfilename)
            with open(sermon_tex_filepath, "a") as fp:
                for sermon_text_line in sermon_text_lines:
                    text_curr = sermon_text_line.strip()
                    if len(text_curr) == 0:
                        continue
                    fp.write(text_curr)
                    fp.write("\n\\newline\n\\newline\n")
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



'''## The 1st to 80th HKBC'''


confno_start = 1
confno_end = 80
sermon_tex_from_generation(confno_start, confno_end)


confno_start = 81
confno_end = 95
sermon_tex_from_generation(confno_start, confno_end)








