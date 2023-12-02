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
    txt2 = inputText
    txt2 = txt2.replace('&nbsp;', '')
    txt2 = txt2.replace('&quot;', '\'')
    txt2 = txt2.replace('&#39;', '\'')
    txt2 = txt2.replace('&ldquo;', '``')
    txt2 = txt2.replace('&rdquo;', '"')
    txt2 = txt2.replace('&lsquo;', '`')
    txt2 = txt2.replace('&rsquo;', '\'')
    txt2 = txt2.replace('&hellip;', '...')
    txt2 = txt2.replace('&Omicron;', '零')
    txt2 = txt2.replace('&mdash;', '─')
    txt2 = txt2.replace('&ndash;', '─')
    txt2 = txt2.replace('\\tab', ' ')
    txt2 = txt2.replace('\\cs16', '')
    txt2 = txt2.replace(' &divide;', '$\\div$')
    txt2 = txt2.replace(' X ', '$\\times$')
    txt2 = txt2.replace('&eacute;', '\\\'e')
    txt2 = txt2.replace('ἵ', 'ι')
    txt2 = txt2.replace('&nu;', 'ν')
    txt2 = txt2.replace('&alpha;', 'α')
    txt2 = txt2.replace('&beta;', 'β')
    txt2 = txt2.replace('&gamma;', 'γ')
    txt2 = txt2.replace('&delta;', 'δ')
    txt2 = txt2.replace('&epsilon;', 'ε')
    txt2 = txt2.replace('&sigma;', 'σ')
    txt2 = txt2.replace('&iota;', 'ι')
    txt2 = txt2.replace('&sigmaf;', 'ς')
    txt2 = txt2.replace('-&gt', '$\rightarrow$')
    txt2 = txt2.replace('שְׁאוֹל&lrm;', '\sblgoodhebrew{שְׁאוֹל}')
    txt2 = txt2.replace('&middot;', '$\\,\\cdot\\,$')
    txt2 = txt2.replace('哋', '地')
    txt2 = txt2.replace('嚟', '黎')
    txt2 = txt2.replace('嘅', 'ge ')
    txt2 = txt2.replace('喺', '係')
    txt2 = txt2.replace('㗎', '架')
    txt2 = txt2.replace('咗', 'jor ')
    txt2 = txt2.replace('嗰', 'gwo ')
    txt2 = txt2.replace('啲', 'D ')
    txt2 = txt2.replace('嗱', 'la ')
    txt2 = txt2.replace('嘢', 'ye ')
    txt2 = txt2.replace('裏', '裡')
    txt2 = txt2.replace('産', '產')
    txt2 = txt2.replace('啱', 'arm ')
    txt2 = txt2.replace('唞', '抖')
    txt2 = txt2.replace('啓', '啟')
    txt2 = txt2.replace('攞', 'lor ')
    txt2 = txt2.replace('啫', 'je ')
    txt2 = txt2.replace('噃', 'bor ')
    txt2 = txt2.replace('吖', '呀')
    txt2 = txt2.replace('噏', 'up ')
    txt2 = txt2.replace('爲', '為')
    txt2 = txt2.replace('揾', '搵')
    txt2 = txt2.replace('揸', 'zar ')
    txt2 = txt2.replace('揼', 'dump ')
    txt2 = txt2.replace('圣', '聖')
    txt2 = txt2.replace('冚', 'cum ')
    txt2 = txt2.replace('絶', '絕')
    txt2 = txt2.replace('衞', '衛')
    txt2 = txt2.replace('誔', '誕')
    txt2 = txt2.replace('歴', '歷')
    txt2 = txt2.replace('亜', '亞')
    txt2 = txt2.replace('様', '樣')
    txt2 = txt2.replace('祢', '你')
    txt2 = txt2.replace('窰', 'yiu ')
    txt2 = txt2.replace('纪', '記')
    txt2 = txt2.replace('緃', '縱')
    txt2 = txt2.replace('约', '約')
    txt2 = txt2.replace('櫈', '凳')
    txt2 = txt2.replace('枱', '台')
    txt2 = txt2.replace('喐', 'yuk ')
    txt2 = txt2.replace('氹', 'tum ')
    txt2 = txt2.replace('着', '著')
    txt2 = txt2.replace('孭', 'meh ')
    txt2 = txt2.replace('瞓', '訓')
    txt2 = txt2.replace('嫲', '麻')
    txt2 = txt2.replace('嘥', 'sai ')
    txt2 = txt2.replace('嘭', 'bang ')
    txt2 = txt2.replace('軚', 'tie ')
    txt2 = txt2.replace('揦', 'la ')
    txt2 = txt2.replace('恒', '恆')
    txt2 = txt2.replace('滙', '匯')
    txt2 = txt2.replace('啩', '掛')
    txt2 = txt2.replace('肶', '脾')
    txt2 = txt2.replace('糭', '粽')
    txt2 = txt2.replace('糉', '粽')
    txt2 = txt2.replace('邨', '村')
    txt2 = txt2.replace('冧', 'lum ')
    txt2 = txt2.replace('㖭', '添')
    txt2 = txt2.replace('攰', 'gui ')
    txt2 = txt2.replace('埗', 'Po ')
    txt2 = txt2.replace('燶', 'lone ')
    txt2 = txt2.replace('峯', '峰')
    txt2 = txt2.replace('餸', 'sung ')
    txt2 = txt2.replace('忟', 'mung ')
    txt2 = txt2.replace('両', '兩')
    txt2 = txt2.replace('掹', 'mung ')
    txt2 = txt2.replace('吔', 'ye ')
    txt2 = txt2.replace('綫', '線')
    txt2 = txt2.replace('乸', '痴')
    txt2 = txt2.replace('菓', 'gwo ')
    txt2 = txt2.replace('嘞', '啦')
    txt2 = txt2.replace('吡', '悲')
    txt2 = txt2.replace('劏', 'tong ')
    txt2 = txt2.replace('喼', 'gip ')
    txt2 = txt2.replace('睺', 'hau ')
    txt2 = txt2.replace('脷', '利')
    txt2 = txt2.replace('濶', '闊')
    txt2 = txt2.replace('紥', 'zhak ')
    txt2 = txt2.replace('踎', 'mau ')
    txt2 = txt2.replace('鈎', '勾')
    txt2 = txt2.replace('廸', 'dik ')
    txt2 = txt2.replace('噔', '等')
    txt2 = txt2.replace('梘', 'gang ')
    txt2 = txt2.replace('厠', '廁')
    txt2 = txt2.replace('糍', 'chi ')
    txt2 = txt2.replace('搲', '掘')
    txt2 = txt2.replace('㷫', 'hing ')
    txt2 = txt2.replace('㷫', 'hing ')
    txt2 = txt2.replace('丶', '. ')
    txt2 = txt2.replace('晩', '晚')
    txt2 = txt2.replace('㷛', '煲')
    txt2 = txt2.replace('眞', '真')
    txt2 = txt2.replace('等', '等')
    txt2 = txt2.replace('丿', '. ')
    txt2 = txt2.replace('銹', '鏽')
    txt2 = txt2.replace('曱甴', '小強')
    txt2 = txt2.replace('鎅', 'gai ')
    txt2 = txt2.replace('踭', 'zoung ')
    txt2 = txt2.replace('牀', '床')
    txt2 = txt2.replace('唥', 'lang ')
    txt2 = txt2.replace('曺', '嘈')
    txt2 = txt2.replace('㩒', '禁')
    txt2 = txt2.replace('抺', '抹')
    txt2 = txt2.replace('敍', '敘')
    txt2 = txt2.replace('叙', '敘')
    txt2 = txt2.replace('腭', 'ngok ')
    txt2 = txt2.replace('衆', '眾')
    txt2 = txt2.replace('哣', '逗')
    txt2 = txt2.replace('刧', '劫')
    txt2 = txt2.replace('鱲', 'Lap ')
    txt2 = txt2.replace('儍', 'sor ')
    txt2 = txt2.replace('丨', '. ')
    txt2 = txt2.replace('錬', '鏈')
    txt2 = txt2.replace('畀', '比')
    txt2 = txt2.replace('喆', '. ')
    txt2 = txt2.replace('裇', 'seuk ')
    txt2 = txt2.replace('镕', 'yeun ')
    txt2 = txt2.replace('効', '效')
    txt2 = txt2.replace('酦', '. ')
    txt2 = txt2.replace('劵', '券')
    txt2 = txt2.replace('粧', '裝')
    txt2 = txt2.replace('卽', '即')
    txt2 = txt2.replace('㬹', 'zoung ')
    txt2 = txt2.replace('啰', 'lor ')
    txt2 = txt2.replace('栢', '柏')
    txt2 = txt2.replace('鰂', '魚則')
    txt2 = txt2.replace('逹', '達')
    txt2 = txt2.replace('堃', '坤')
    txt2 = txt2.replace('讃', '讚')
    txt2 = txt2.replace('⾃', '自')
    txt2 = txt2.replace('频', '頻')
    txt2 = txt2.replace('记', '記')
    txt2 = txt2.replace('话', '話')
    txt2 = txt2.replace('竉', '寵')
    txt2 = txt2.replace('呑', '吞')
    txt2 = txt2.replace('傈', '僳')
    txt2 = txt2.replace('淸', '清')
    txt2 = txt2.replace('寛', '寬')
    txt2 = txt2.replace('唿', '弗')
    txt2 = txt2.replace('叁', '參')
    txt2 = txt2.replace('唓', '即係')
    txt2 = txt2.replace('嘣', '崩')
    txt2 = txt2.replace('廻', '迴')
    txt2 = txt2.replace('麽', '麼')
    txt2 = txt2.replace('猬', '蝟')
    txt2 = txt2.replace('綉', '繡')
    txt2 = txt2.replace('箓', '籙')
    txt2 = txt2.replace('氷', '冰')
    txt2 = txt2.replace('祎', '禕')
    txt2 = txt2.replace('咔', 'ka ')
    txt2 = txt2.replace('&', ' and ')
    txt2 = txt2.replace('羣', '群')
    txt2 = txt2.replace('鍳', '鑒')
    txt2 = txt2.replace('僞', '偽')
    txt2 = txt2.replace('\ue226', '祐')
    txt2 = txt2.replace('隣', '鄰')
    txt2 = txt2.replace('\u200b', '')
    txt2 = txt2.replace('\u3000', '~')
    txt2 = txt2.replace('\ue233', '身')
    txt2 = txt2.replace('\ue313', '涉')
    txt2 = txt2.replace('\ue314', '麃')
    txt2 = txt2.replace('\ue2de', '鬮')
    txt2 = txt2.replace('\ue2df', '鬥')
    txt2 = txt2.replace('\ue096', '芒')
    txt2 = txt2.replace('\ue0e1', '載')
    txt2 = txt2.replace('\ue05e', '瑟')
    txt2 = txt2.replace('\ue05e', '繫')
    txt2 = txt2.replace('\ue052', '的')
    txt2 = txt2.replace('\ue05e', '配')
    txt2 = txt2.replace('\ue010', '憂')
    txt2 = txt2.replace('\ue0f5', '付')
    txt2 = txt2.replace('\ue17a', '使')
    txt2 = txt2.replace('\ue031', '步')
    txt2 = txt2.replace('\ue315', '犁')
    txt2 = txt2.replace('\ue339', '草')
    txt2 = txt2.replace('\ue14c', '冤')
    txt2 = txt2.replace('释', '釋')
    txt2 = txt2.replace('义', '義')
    txt2 = txt2.replace('请', '請')
    txt2 = txt2.replace('没', '沒')
    txt2 = txt2.replace('赋', '賦')
    txt2 = txt2.replace('诗', '詩')
    txt2 = txt2.replace('稣', '穌')
    txt2 = txt2.replace('细', '細')
    txt2 = txt2.replace('随', '隨')
    txt2 = txt2.replace('细', '細')
    txt2 = txt2.replace('终', '終')
    txt2 = txt2.replace('残', '殘')
    txt2 = txt2.replace('结', '結')
    txt2 = txt2.replace('给', '給')
    txt2 = txt2.replace('内', '內')
    txt2 = txt2.replace('统', '統')
    txt2 = txt2.replace('强', '強')
    txt2 = txt2.replace('课', '課')
    txt2 = txt2.replace('别', '別')
    txt2 = txt2.replace('专', '專')
    txt2 = txt2.replace('却', '卻')
    txt2 = txt2.replace('\ue1f5', '')
    txt2 = txt2.replace('\ue1f5', '')
    txt2 = txt2.replace('\ue045', '實')
    txt2 = txt2.replace('\ue00e', '洶')
    txt2 = txt2.replace('窑', 'yiu')
    txt2 = txt2.replace('躭', '耽')
    txt2 = txt2.replace('\ue097', '呔')
    txt2 = txt2.replace('亘', '亙')
    txt2 = txt2.replace('‐', '-')
    txt2 = txt2.replace('犠', '犧')
    txt2 = txt2.replace('怱', '匆')
    txt2 = txt2.replace('｣', '」')
    txt2 = txt2.replace('｢', '「')
    txt2 = txt2.replace('﹑', '、')
    txt2 = txt2.replace('寃', '冤')
    txt2 = txt2.replace('閙', '鬧')
    txt2 = txt2.replace('虚', '虛')
    txt2 = txt2.replace('温', '溫')
    txt2 = txt2.replace('凖', '準')
    txt2 = txt2.replace('墻', '牆')
    txt2 = txt2.replace('侓', '律')
    txt2 = txt2.replace('﹣', '-')
    txt2 = txt2.replace('踪', '蹤')
    txt2 = txt2.replace('鐧', '簡')
    txt2 = txt2.replace('袮', '你')
    txt2 = txt2.replace('涶', '唾')
    txt2 = txt2.replace('説', '說')
    txt2 = txt2.replace('駡', '罵')
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
        str_year_end = 'latest'
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








