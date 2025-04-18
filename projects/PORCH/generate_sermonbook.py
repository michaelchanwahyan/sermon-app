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
    bk2bkorder_dict, c2b_dict, c2ch_dict, c2v_dict, c2s_dict, c2t_dict, c2bvc_dict = pkl.load(fp)
fp.close()


with open("x2code_dictionary.pkl", "rb") as fp:
    b2c_dict = pkl.load(fp)
fp.close()



'''### print the latex document : sermon content'''


with open('../rep_whisper_trailing.txt', 'r') as fp:
    whisper_trailing_rep_list = fp.readlines()
fp.close()


with open("./index_byt.csv", "r") as fp:
    lines = fp.readlines()
fp.close()


print('sermon count:', len(lines))


def print_prefix(sermon_tex_filepath, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: printing out prefixing")
    _ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/Sermon Transcription 2014-present/' | sed 's/Youtube Channel:/Youtube Channel: The Porch/' > " + sermon_tex_filepath)
    return progressStepCnt


def generate_toc(sermon_tex_filepath, index_file, toc_type, progressStepCnt):
    progressStepCnt += 1
    print(f"Step {progressStepCnt}: reading in full index file")
    with open(index_file, 'r') as fp:
        lines = fp.readlines()

    progressStepCnt += 1
    print(f"Step {progressStepCnt}: writing TOC in {toc_type} order")
    with open(sermon_tex_filepath, "a") as fp:
        fp.write(f"\\section{{Index\\small{{({toc_type})}}}}\n")
        fp.write(f"\\label{{sec:index_{toc_type}}}\n")
        fp.write("{ \\scriptsize\n")
        # --------------------------------------
        # start of TOC table
        # --------------------------------------
        fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
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
            if os.path.isfile(f'../../data/PORCH/{cc}.txt'):
                bstr = c2b_dict.get(cc, ' ')
                vstr = c2v_dict.get(cc, ' ')
                sstr = c2s_dict.get(cc, ' ').replace('_','\_').replace('&','\&').replace('#','\#')
                tstr = c2t_dict.get(cc, ' ')
                ystr = "\\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{" + cc.replace('_','\_') + "}}"
                fp.write(bstr + ' ' + vstr + " & " \
                        + "\\hyperref[sec:"+cc.replace('-','_')+"]{"+sstr+"}" + " & " \
                        + tstr + " & " \
                        + ystr \
                        + " \\\\\n")
        fp.write("\\end{xltabular}\n")
        fp.write("}\n")
        fp.write("\\newpage\n\n")
        # --------------------------------------
        # end of table sorted by toc_type order
        # --------------------------------------
    return progressStepCnt


def write_scripture_part(fp, cc):
    return


def write_sermon_text(fp, cc):
    with open("../../data/PORCH/"+cc+".txt", "r") as fp_:
        the_sermon_text = fp_.read()
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
        # if the text line contains dollar sign '$',
        # it would probably bring up error
        textline = textline.replace('_','\_').replace('&','\&').replace('#','\#').replace('$', '\$')
        fp.write(textline + "\n")
        if _textrow_cnt % 40 == 0:
            fp.write("\n")
    fp.write("\\newpage\n\n")


def write_sermon_section(sermon_tex_filepath, cc, cc_prev, cc_next):
    with open(sermon_tex_filepath, "a") as fp:
        sectionNameStr = f"{c2b_dict.get(cc, '')}".strip()
        fp.write(f"\n\n\\section{{{sectionNameStr}}}\n")
        fp.write(f"\\label{{sec:{cc.replace('-','_')}}}\n")
        sstr = c2s_dict.get(cc, ' ').replace('_','\_').replace('&','\&').replace('#','\#')
        fp.write("\\textbf{"+sstr+"}\n")
        fp.write("\\newline\n\\newline\n")
        fp.write("link: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{https://youtube.com/watch?v=" + cc.replace('_','\_') + "}} ~~~~ recording date: " + c2t_dict.get(cc) + "\n")
        fp.write("\\newline\n\\newline\n")
        fp.write("\\hyperref[sec:"+cc_prev.replace('-','_')+"]{\\small{< < < PREV SERMON < < <}}\n")
        fp.write("~\n")
        fp.write("\\hyperref[sec:index_chronic]{\\small{[back to index]}}\n")
        fp.write("~\n")
        fp.write("\\hyperref[sec:"+cc_next.replace('-','_')+"]{\\small{> > > NEXT SERMON > > >}}\n")
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
            print(f"{lineId+1} of {len(lines)}")
        cc = line.split(",")[0]
        cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
        cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
        if os.path.isfile(f'../../data/PORCH/{cc}.txt'):
            write_sermon_section(sermon_tex_filepath, cc, cc_prev, cc_next)
    return progressStepCnt


def generate_afterword_and_postfix(sermon_tex_filepath):
    _ = os.system("cat ../afterword.tex >> " + sermon_tex_filepath)
    _ = os.system("cat ../postfix.tex >> " + sermon_tex_filepath)


def sermon_tex():
    progressStepCnt = 0
    sermon_tex_filepath = f"../../build/PORCH/sermon_PORCH_2014-present.tex"
    # --------------------------------------
    # print the latex document : prefix
    # --------------------------------------
    progressStepCnt = print_prefix(sermon_tex_filepath, progressStepCnt)
    # --------------------------------------
    # --------------------------------------
    progressStepCnt = generate_toc(sermon_tex_filepath, './index_byt.csv', 'chronic', progressStepCnt)
    progressStepCnt = generate_main_content(sermon_tex_filepath, './index_byt.csv', progressStepCnt)
    # --------------------------------------
    # print the latex document : afterword and postfix
    # --------------------------------------
    generate_afterword_and_postfix(sermon_tex_filepath)

    print("done !")






'''## generate main content'''


sermon_tex()








