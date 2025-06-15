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


with open("./index_byt.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


print('sermon count:', len(lines))


rgx_bv = re.compile(r'(?<=\d)[_](?=\d)')


def gfc_title_processing(cc):
    sstr = c2s_dict.get(cc, ' ')
    sstr = re.sub(r'[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]', '', sstr) # remove date from title
    sstr = rgx_bv.sub(':', sstr) # adjust bible verse , use ':' to replace '_'
    sstr = sstr[:-13] # remove trailing youtube code
    sstr = sstr.replace('網上崇拜', '')
    sstr = sstr.replace('網上聖餐崇拜', '')
    sstr = cleanse_special_char(
        sstr.replace('_', '\\_').replace('&', '\\&')
    )
    sstr = sstr.strip()
    return sstr


def print_prefix(sermon_tex_filepath, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: printing out prefixing")
    _ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/宣道會洪恩堂 粵語講道逐字稿 2020-present/' | sed 's/Youtube Channel:/Youtube Channel: Graceflow Church/' > " + sermon_tex_filepath)
    return progressStepCnt


def generate_toc(sermon_tex_filepath, index_file, toc_type, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: reading in full index file")
    with open(index_file, 'r') as fp:
        lines = fp.readlines()

    progressStepCnt += 1
    print(f"Step {progressStepCnt}: writing TOC in {toc_type} order")
    with open(sermon_tex_filepath, "a") as fp:
        if   toc_type == 'title':
            fp.write(f"\\section{{目錄\\small{{(順題)}}}}\n")
        elif toc_type == 'chronic':
            fp.write(f"\\section{{目錄\\small{{(順時)}}}}\n")
        elif toc_type == 'preacher':
            fp.write(f"\\section{{目錄\\small{{(順仕)}}}}\n")
        elif toc_type == 'scriptual':
            fp.write(f"\\section{{目錄\\small{{(順卷)}}}}\n")
        fp.write(f"\\label{{sec:index_{toc_type}}}\n")
        fp.write("{ \\scriptsize\n")
        # --------------------------------------
        # start of TOC table
        # --------------------------------------
        fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n")
        fp.write("\\hline\n")
        # --------------------------------------
        # lines is the line content in index_{toc_type}
        # --------------------------------------
        for lineId, line in enumerate(lines):
            cc = line.split(",")[0]
            # --------------------------------------
            # only include this code cc if it is
            # ready in the transcription folder
            # --------------------------------------
            if os.path.isfile(f'../../data/GFC/{cc}.txt'):
                bstr = c2b_dict.get(cc, ' ')
                vstr = c2v_dict.get(cc, ' ')
                sstr = c2s_dict.get(cc, ' ')
                sstr = gfc_title_processing(cc)
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
        fp.write("}\n")
        fp.write("\\newpage\n\n")
        # --------------------------------------
        # end of table sorted by toc_type
        # --------------------------------------
    return progressStepCnt


def write_scripture_part(fp, cc):
    # ----------------------
    # add the scripture part if not None
    bvc_curr = c2bvc_dict.get(cc)
    if bvc_curr is not None:
        bvc_curr = bvc_curr.split("\n")
        # first row shall be book + verse info
        fp.write(bvc_curr[0].strip() + "\n")
        fp.write("\\newline\n")
        fp.write("\\begin{longtable}{cl}\n")
        fp.write("\\hline\n\\hline\n")
        fp.write("章節 & 經文 (和合本修訂版)\\\\\n")
        fp.write("\\hline\n")
        for bvc_line in bvc_curr[1:]:
            bvc_line = bvc_line.strip()
            if len(bvc_line) > 0:
                if bvc_line != [_.strip() for _ in bvc_curr if len(_.strip())][-1]:
                    bvc_line += " \\\\ \\\\ \\relax\n"
                else:
                    bvc_line += " \\\\ \\\\\n"
                si = bvc_line.find(" ")
                if si == -1:
                    bvc_line = "& " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line + " \\end{tabularx}"
                else:
                    bvc_line = bvc_line[:si].replace(".", ":") + " & " + "\\begin{tabularx}{0.7\\textwidth}{X} " + bvc_line[si+1:]
                    nli = bvc_line.find(" \\\\")
                    bvc_line = bvc_line[:nli] + " \\end{tabularx}" + bvc_line[nli:]
                fp.write(bvc_line)
        fp.write("[1ex]\n")
        fp.write("\\hline\n\\hline\n")
        fp.write("\\end{longtable}\n")


def write_sermon_text(fp, cc):
    with open(f"../../data/GFC/{cc}.txt", "r") as fp_:
        the_sermon_text = fp_.read()
    the_sermon_text = cleanse_special_char(the_sermon_text).replace("\\n\\n", "\\n")
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


def write_sermon_section(sermon_tex_filepath, cc, cc_prev, cc_next):
    with open(sermon_tex_filepath, "a") as fp:
        sectionNameStr = ''
        b = c2b_dict.get(cc)
        sectionNameStr += b if b is not None else ''
        v = c2v_dict.get(cc)
        sectionNameStr += ' ' + v if b is not None and v is not None else ''
        ch = c2ch_dict.get(cc)
        sectionNameStr += ' ' + ch if b is not None and ch is not None and v is None else ''
        fp.write(f"\n\n\\section{{{sectionNameStr}}}\n")
        fp.write(f"\\label{{sec:{cc.replace('-', '_')}}}\n")
        sstr = cleanse_special_char(c2s_dict.get(cc, ' ').replace('_', '\\_').replace('&', '\\&'))
        fp.write(f"\\textbf{{{sstr}}}\n")
        fp.write("\\newline\n\\newline\n")
        cc_ud_protect = cc.replace('_', '\\_')
        fp.write(f"連結: \\href{{https://youtube.com/watch?v={cc}}}{{\\texttt{{https://youtube.com/watch?v={cc_ud_protect}}}}} ~~~~ 語音日期: {c2t_dict.get(cc)}\n")
        fp.write("\\newline\n\\newline\n")
        fp.write(f"\\hyperref[sec:{cc_prev.replace('-', '_')}]{{\\small{{< < < PREV SERMON < < <}}}}\n")
        fp.write("~\n")
        fp.write("\\hyperref[sec:index_chronic]{\\small{[返順時目]}}\n")
        fp.write("~\n")
        fp.write("\\hyperref[sec:index_scriptual]{\\small{[返順卷目]}}\n")
        fp.write("~\n")
        fp.write(f"\\hyperref[sec:{cc_next.replace('-', '_')}]{{\\small{{> > > NEXT SERMON > > >}}}}\n")
        fp.write("\\newline\n\\newline\n")
        write_scripture_part(fp, cc)
        write_sermon_text(fp, cc)
        fp.write("\\newpage\n\n")


def generate_main_content(sermon_tex_filepath, index_file, progressStepCnt):
    with open(index_file, "r") as fp:
        lines = fp.readlines()
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: generate main content")
    for lineId, line in enumerate(lines):
        if (lineId+1) % 100 == 0:
            print(f"{lineId+1} of {len(lines)} in {sermon_tex_filepath}")
        cc = line.split(",")[0]
        cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
        cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
        if os.path.isfile(f'../../data/GFC/{cc}.txt'):
            write_sermon_section(sermon_tex_filepath, cc, cc_prev, cc_next)
    return progressStepCnt


def generate_afterword_and_postfix(sermon_tex_filepath):
    _ = os.system("cat ../afterword.tex >> " + sermon_tex_filepath)
    _ = os.system("cat ../postfix.tex >> " + sermon_tex_filepath)


def sermon_tex():
    progressStepCnt = 0
    sermon_tex_filepath = f"../../build/GFC/sermon_GFC_2020-present.tex"
    # --------------------------------------
    # print the latex document : prefix
    # --------------------------------------
    progressStepCnt = print_prefix(sermon_tex_filepath, progressStepCnt)
    # --------------------------------------
    # index table sorted by name order
    # only take into account
    # within desired year range
    # --------------------------------------
    progressStepCnt = generate_toc(sermon_tex_filepath, './index_byt.csv', 'chronic', progressStepCnt)
    progressStepCnt = generate_main_content(sermon_tex_filepath, './index_byt.csv', progressStepCnt)
    # --------------------------------------
    # print the latex document : afterword and postfix
    # --------------------------------------
    generate_afterword_and_postfix(sermon_tex_filepath)

    print("done !")


sermon_tex()








