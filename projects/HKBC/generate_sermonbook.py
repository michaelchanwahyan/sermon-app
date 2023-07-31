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
def cleanse_special_char(inputText):
    txt2 = inputText \
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


progressStepCnt = 0
# --------------------------------------
# read the index table and only take
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: reading in full index file")
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
sermon_tex_filepath = '../../build/HKBC/hkbc_sermon.tex'
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(
    "cat ../prefix.tex | sed 's/粵語講道逐字稿/港九培靈研經會 講道/'" \
    + " | sed 's/Youtube Channel:/Hong Kong Bible Conference 1928-Present/' > " \
    + sermon_tex_filepath
)

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
for lineId in range(len(lines)):
    if (lineId+1) % 100 == 0:
        print(f"{lineId+1} of {len(lines)}")
    line = lines[lineId]
    line_contents = line.split(",")
    s_curr = line_contents[0]
    s_prev = lines[(lineId-1)%len(lines)].split(",")[0]
    s_next = lines[(lineId+1)%len(lines)].split(",")[0]
    if os.path.isfile(f'../../data/HKBC/{s_curr}'):
        # --------------------------------------
        # print out lecture title and misc. info
        # --------------------------------------
        with open(sermon_tex_filepath, "a") as fp:
            sectionNameStr = ''
            p_curr = line_contents[1].strip() # preacher name
            cn_curr = line_contents[2].strip() # conference no.
            ln_curr = line_contents[3].strip() # lecture no.
            t_curr = cleanse_special_char(line_contents[4]) # full title
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


