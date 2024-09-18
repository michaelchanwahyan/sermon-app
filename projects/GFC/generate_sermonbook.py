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
    b2c_dict = pkl.load(fp)
fp.close()


# compile regular expression rgx to cater math symbol '^'


rgx = re.compile(r'([A-Za-z0-9=]+)\^([A-Za-z0-9\-]+)')


print('checking of "rgx.sub(r\'$\\1^\\2$\', \'E=MC^2\')" :', rgx.sub(r'$\1^\2$', 'E=MC^-2'))



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


with open("./index_byt.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


print('sermon count:', len(lines))


rgx_bv = re.compile(r'(?<=\d)[_](?=\d)')


def yfcx_sermon_title_processing(cc):
    sstr = c2s_dict.get(cc, ' ')
    sstr = re.sub(r'[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]', '', sstr) # remove date from title
    sstr = rgx_bv.sub(':', sstr) # adjust bible verse , use ':' to replace '_'
    sstr = sstr[:-13] # remove trailing youtube code
    sstr = sstr.replace('網上崇拜', '')
    sstr = sstr.replace('網上聖餐崇拜', '')
    sstr = cleanse_special_char(
        sstr.replace('_','\_').replace('&','\&')
    )
    sstr = sstr.strip()
    return sstr


# sermon tex generation
progressStepCnt = 0
# --------------------------------------
# read the index table and only take
# into account within desired year range
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: reading in full index file")
with open('./index_byt.csv', 'r') as fp:
    lines = fp.readlines()
fp.close()

sermon_tex_filepath = f"../../build/GFC/sermon_GFC_2020-present.tex"
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/粵語講道逐字稿 2020-present/' | sed 's/Youtube Channel:/Youtube Channel: 宣道會洪恩堂 Graceflow Church/' > " + sermon_tex_filepath)



'''## generate index table in chronic order'''


progressStepCnt += 1
print(f"Step {progressStepCnt}: generate index in chronic order")
with open("./index_byt.csv", "r") as fp:
    lines = fp.readlines()
fp.close()
# --------------------------------------
# index table sorted by chronic order
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC in chronic order")
with open(sermon_tex_filepath, "a") as fp:
    sermonCnt = 0
    fp.write("\\section{目錄\\small{(順時)}}\n")
    fp.write("\\label{sec:index_chronic}\n")
    fp.write("{ \\scriptsize\n")
    # --------------------------------------
    # start of TOC table
    # --------------------------------------
    fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
    fp.write("\\hline\n")
    # --------------------------------------
    # lines is the line content in index_byt
    # --------------------------------------
    for lineId, line in enumerate(lines):
        cc = line.split(",")[0]
        # --------------------------------------
        # only include this code cc if it is
        # ready in the transcription folder
        # --------------------------------------
        if os.path.isfile(f'../../data/GFC/{cc}.txt'):
            sermonCnt += 1
            bstr = c2b_dict.get(cc, ' ')
            vstr = c2v_dict.get(cc, ' ')
            sstr = c2s_dict.get(cc, ' ')
            sstr = yfcx_sermon_title_processing(cc)
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
    # end of table sorted by chronic order
    # --------------------------------------
    fp.write("}\n")
    print('sermon count in current book: %d' % sermonCnt)
    fp.write("\\newpage\n\n")
fp.close()



'''## generate index in scriptual order'''


progressStepCnt += 1
print(f"Step {progressStepCnt}: generate index in scriptual order")
with open("./index_byb.csv", "r") as fp:
    lines = fp.readlines()
fp.close()
# --------------------------------------
# index table sorted by scriptual order
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC in scriptual order")
with open(sermon_tex_filepath, "a") as fp:
    sermonCnt = 0
    fp.write("\\section{目錄\\small{(順卷)}}\n")
    fp.write("\\label{sec:index_scriptual}\n")
    fp.write("{ \\scriptsize\n")
    # --------------------------------------
    # start of TOC table
    # --------------------------------------
    fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
    fp.write("\\hline\n")
    # --------------------------------------
    # lines is the line content in index_byb
    # --------------------------------------
    for lineId, line in enumerate(lines):
        cc = line.split(",")[0]
        # --------------------------------------
        # only include this code cc if it is
        # ready in the transcription folder
        # --------------------------------------
        if os.path.isfile(f'../../data/GFC/{cc}.txt'):
            sermonCnt += 1
            bstr = c2b_dict.get(cc, ' ')
            vstr = c2v_dict.get(cc, ' ')
            sstr = c2s_dict.get(cc, ' ')
            sstr = yfcx_sermon_title_processing(cc)
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
    # end of table sorted by scriptual order
    # --------------------------------------
    fp.write("}\n")
    print('sermon count in current book: %d' % sermonCnt)
    fp.write("\\newpage\n\n")
fp.close()



'''## generate main content'''


with open("./index_byt.csv", "r") as fp:
    lines = fp.readlines()
fp.close()
progressStepCnt += 1
print(f"Step {progressStepCnt}: generate main content")
cc_prev = ''
cc_next = ''
# --------------------------------------
# lines is the line content in index_byt
# --------------------------------------
for lineId, line in enumerate(lines):
    if (lineId+1) % 100 == 0:
        print(f"{lineId+1} of {len(lines)}")
    cc = line.split(",")[0]
    cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
    cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
    if os.path.isfile(f'../../data/GFC/{cc}.txt'):
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
            sstr = yfcx_sermon_title_processing(cc)
            sstr = cleanse_special_char(
                c2s_dict.get(cc, ' ').replace('_','\_').replace('&','\&')
            )
            fp.write("\\textbf{"+sstr+"}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("連結: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ https://youtube.com/watch?v=" + cc.replace('_','\_') + "}} ~~~~ 語音日期: " + c2t_dict.get(cc) + " \n")
            fp.write("\\newline\n\\newline\n")
            fp.write("\\hyperref[sec:"+cc_prev.replace('-','_')+"]{\\small{< < < PREV SERMON < < <}}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:index_chronic]{\\small{[返順時目]}}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:index_scriptual]{\\small{[返順卷目]}}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:"+cc_next.replace('-','_')+"]{\\small{> > > NEXT SERMON > > >}}\n")
            fp.write("\\newline\n\\newline\n")
        fp.close()
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
            with open("../../data/GFC/"+cc+".txt", "r") as fp_:
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








