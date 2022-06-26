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
    c2p_dict, bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict = pkl.load(fp)
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
def text_transform_cantonStyle2normalStyle(inputfilename):
    with open(inputfilename, 'r') as infile_fp:
        cantonText = infile_fp.read()
    infile_fp.close()
    cantonText = re.sub(r'哋', '地', cantonText)
    cantonText = re.sub(r'嚟', '黎', cantonText)
    cantonText = re.sub(r'嘅', '既', cantonText)
    cantonText = re.sub(r'喺', '係', cantonText)
    cantonText = re.sub(r'㗎', '架', cantonText)
    cantonText = re.sub(r'咗', '左', cantonText)
    cantonText = re.sub(r'嗰', '果', cantonText)
    cantonText = re.sub(r'啲', 'D', cantonText)
    cantonText = re.sub(r'嗱', '拿', cantonText)
    cantonText = re.sub(r'嘢', '野', cantonText)
    cantonText = re.sub(r'裏', '裡', cantonText)
    cantonText = re.sub(r'産', '產', cantonText)
    cantonText = re.sub(r'啱', '岩', cantonText)
    return cantonText
p_list = list(p2c_dict.keys())
print(p_list)
with open("../index_byp.csv", "r") as fp:
    lines = fp.readlines()
fp.close()
sermon_tex_filepath = "../build/sermon.tex"
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
_ = os.system("cat prefix > " + sermon_tex_filepath)

# --------------------------------------
# index table partitioned by preachers
# --------------------------------------

with open(sermon_tex_filepath, "a") as fp:
    p_prev = ''
    p_curr = ''
    p_id = 0
    fp.write("{ \\scriptsize\n")
    fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
    fp.write("\\hline\n")
    for lineId in range(len(lines)):
        line = lines[lineId]
        cc = line.split(",")[0]
        if os.path.isfile(f'../data/JNG/{cc}.txt'):
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
            sstr = c2s_dict.get(cc, ' ').replace('_','\_')
            tstr = c2t_dict.get(cc, ' ')
            ystr = "\\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ " + cc.replace('_','\_') + "}}"
            fp.write(bstr + ' ' + vstr + " & " \
                     + "\\hyperref[sec:"+cc.replace('-','_')+"]{"+sstr+"}" + " & " \
                     + tstr + " & " \
                     + ystr \
                     + " \\\\\n")
    fp.write("\\end{xltabular}\n")
    fp.write("}\n")
fp.close()

# --------------------------------------
# Partitioned by preacher
# --------------------------------------
p_prev = ''
p_curr = ''
p_id = 0
cc_prev = ''
cc_next = ''
for lineId in range(len(lines)):
    line = lines[lineId]
    cc = line.split(",")[0]
    cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
    cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
    if os.path.isfile(f'../data/JNG/{cc}.txt'):
        p_prev = p_curr
        p_curr = c2p_dict.get(cc)
        if p_prev != p_curr:
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
                for lineId_ in range(len(lines)):
                    line_ = lines[lineId_]
                    cc_ = line_.split(",")[0]
                    if os.path.isfile(f'../data/JNG/{cc}.txt') and p_curr == c2p_dict.get(cc_):
                        bstr = c2b_dict.get(cc_, ' ')
                        vstr = c2v_dict.get(cc_, ' ')
                        sstr = c2s_dict.get(cc_, ' ').replace('_','\_')
                        tstr = c2t_dict.get(cc_, ' ')
                        ystr = "\\href{https://youtube.com/watch?v=" + cc_ +"}{\\texttt{ " + cc_.replace('_','\_') + "}}"
                        fp.write(bstr + ' ' + vstr + " & " \
                                 + "\\hyperref[sec:"+cc.replace('-','_')+"]{"+sstr+"}" + " & " \
                                 + tstr + " & " \
                                 + ystr \
                                 + " \\\\\n")
                fp.write("\\end{xltabular}\n")
                fp.write("}\n")
                # END OF chapter tabular-toc with sermon title
                # ------------------------------------
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
            fp.write("\\textbf{"+c2s_dict.get(cc).replace('_','\_')+"}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("link: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ https://youtube.com/watch?v=" + cc.replace('_','\_') + "}}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("\\hyperref[sec:"+cc_prev.replace('-','_')+"]{< < < PREV SERMON < < <}\n")
            fp.write("~~~\n")
            fp.write("\\hyperlink{toc}{[返主目錄]}\n")
            fp.write("~~~\n")
            fp.write("\\hyperref[ch:preacher"+str(p_id)+"]{[返講員目錄]}\n")
            fp.write("~~~\n")
            fp.write("\\hyperref[sec:"+cc_next.replace('-','_')+"]{> > > NEXT SERMON > > >}\n")
            fp.write("\\newline\n\\newline\n")
        fp.close()
        # _ = os.system(f"cat ../data/JNG/{cc}.txt >> " + sermon_tex_filepath)
        with open(sermon_tex_filepath, "a") as fp:
            the_sermon_text = text_transform_cantonStyle2normalStyle("../data/JNG/"+cc+".txt")
            fp.write(the_sermon_text)
        fp.close()
        with open(sermon_tex_filepath, "a") as fp:
            fp.write("\n\n\\newpage\n\n")
        fp.close()

# --------------------------------------
# print the latex document : postfix
# --------------------------------------
_ = os.system("cat ./postfix >> " + sermon_tex_filepath)

