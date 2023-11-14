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
# sermon book for YFCX shall be arranged in chronicle order
# compile regular expression rgx to cater math symbol '^'
rgx = re.compile(r'([A-Za-z0-9=]+)\^([A-Za-z0-9\-]+)')
print('checking of "rgx.sub(r\'$\\1^\\2$\', \'E=MC^2\')" :', rgx.sub(r'$\1^\2$', 'E=MC^-2'))

'''### print the latex document : sermon content'''
def text_transform_cantonStyle2normalStyle(cantonText):
    cantonText = rgx.sub(r'$\1^\2$', cantonText)
    cantonText = re.sub(r'&', ' and ', cantonText)
    cantonText = re.sub(r'⾃', '自', cantonText)
    cantonText = re.sub(r'㖭', '添', cantonText)
    cantonText = re.sub(r'㗎', '架', cantonText)
    cantonText = re.sub(r'㩒', '禁', cantonText)
    cantonText = re.sub(r'㬹', 'zoung ', cantonText)
    cantonText = re.sub(r'㷛', '煲', cantonText)
    cantonText = re.sub(r'㷫', 'hing ', cantonText)
    cantonText = re.sub(r'专', '專', cantonText)
    cantonText = re.sub(r'両', '兩', cantonText)
    cantonText = re.sub(r'丨', '. ', cantonText)
    cantonText = re.sub(r'丶', '. ', cantonText)
    cantonText = re.sub(r'为', '為', cantonText)
    cantonText = re.sub(r'丿', '. ', cantonText)
    cantonText = re.sub(r'义', '義', cantonText)
    cantonText = re.sub(r'乸', '痴', cantonText)
    cantonText = re.sub(r'亘', '亙', cantonText)
    cantonText = re.sub(r'亜', '亞', cantonText)
    cantonText = re.sub(r'仅', '僅', cantonText)
    cantonText = re.sub(r'们', '們', cantonText)
    cantonText = re.sub(r'侓', '律', cantonText)
    cantonText = re.sub(r'傈', '僳', cantonText)
    cantonText = re.sub(r'僞', '偽', cantonText)
    cantonText = re.sub(r'儍', 'sor ', cantonText)
    cantonText = re.sub(r'关', '關', cantonText)
    cantonText = re.sub(r'内', '內', cantonText)
    cantonText = re.sub(r'冚', 'cum ', cantonText)
    cantonText = re.sub(r'冧', 'lum ', cantonText)
    cantonText = re.sub(r'凖', '準', cantonText)
    cantonText = re.sub(r'凤', '風', cantonText)
    cantonText = re.sub(r'刘', '劉', cantonText)
    cantonText = re.sub(r'刧', '劫', cantonText)
    cantonText = re.sub(r'别', '別', cantonText)
    cantonText = re.sub(r'刹', '剎', cantonText)
    cantonText = re.sub(r'劏', 'tong ', cantonText)
    cantonText = re.sub(r'劳', '勞', cantonText)
    cantonText = re.sub(r'劵', '券', cantonText)
    cantonText = re.sub(r'効', '效', cantonText)
    cantonText = re.sub(r'医', '醫', cantonText)
    cantonText = re.sub(r'华', '華', cantonText)
    cantonText = re.sub(r'卢', '盧', cantonText)
    cantonText = re.sub(r'卧', '臥', cantonText)
    cantonText = re.sub(r'却', '卻', cantonText)
    cantonText = re.sub(r'卽', '即', cantonText)
    cantonText = re.sub(r'厠', '廁', cantonText)
    cantonText = re.sub(r'叁', '參', cantonText)
    cantonText = re.sub(r'叙', '敘', cantonText)
    cantonText = re.sub(r'吓', 'o下', cantonText)
    cantonText = re.sub(r'吔', 'ye ', cantonText)
    cantonText = re.sub(r'吖', '呀', cantonText)
    cantonText = re.sub(r'吗', '嗎', cantonText)
    cantonText = re.sub(r'吡', '悲', cantonText)
    cantonText = re.sub(r'呑', '吞', cantonText)
    cantonText = re.sub(r'呕', '', cantonText)
    cantonText = re.sub(r'咔', 'ka ', cantonText)
    cantonText = re.sub(r'咗', 'jor ', cantonText)
    cantonText = re.sub(r'咤', 'tak', cantonText)
    cantonText = re.sub(r'哋', '地', cantonText)
    cantonText = re.sub(r'响', '響', cantonText)
    cantonText = re.sub(r'哑', '啞', cantonText)
    cantonText = re.sub(r'哒', '躂', cantonText)
    cantonText = re.sub(r'哣', '逗', cantonText)
    cantonText = re.sub(r'唓', '即係', cantonText)
    cantonText = re.sub(r'唞', '抖', cantonText)
    cantonText = re.sub(r'唥', 'lang ', cantonText)
    cantonText = re.sub(r'唿', '弗', cantonText)
    cantonText = re.sub(r'啓', '啟', cantonText)
    cantonText = re.sub(r'啩', '掛', cantonText)
    cantonText = re.sub(r'啫', 'je ', cantonText)
    cantonText = re.sub(r'啰', 'lor ', cantonText)
    cantonText = re.sub(r'啱', 'arm ', cantonText)
    cantonText = re.sub(r'啲', 'D ', cantonText)
    cantonText = re.sub(r'喆', '. ', cantonText)
    cantonText = re.sub(r'喐', 'yuk ', cantonText)
    cantonText = re.sub(r'喺', '係', cantonText)
    cantonText = re.sub(r'喼', 'gip ', cantonText)
    cantonText = re.sub(r'嗰', 'gwo ', cantonText)
    cantonText = re.sub(r'嗱', 'la ', cantonText)
    cantonText = re.sub(r'嘅', 'ge ', cantonText)
    cantonText = re.sub(r'嘚', 'dik ', cantonText)
    cantonText = re.sub(r'嘞', '啦', cantonText)
    cantonText = re.sub(r'嘢', 'ye ', cantonText)
    cantonText = re.sub(r'嘣', '崩', cantonText)
    cantonText = re.sub(r'嘥', 'sai ', cantonText)
    cantonText = re.sub(r'嘭', 'bang ', cantonText)
    cantonText = re.sub(r'噃', 'bor ', cantonText)
    cantonText = re.sub(r'噏', 'up ', cantonText)
    cantonText = re.sub(r'噔', '等', cantonText)
    cantonText = re.sub(r'噼', '啪', cantonText)
    cantonText = re.sub(r'嚟', '黎', cantonText)
    cantonText = re.sub(r'嚿', '舊', cantonText)
    cantonText = re.sub(r'圣', '聖', cantonText)
    cantonText = re.sub(r'坂', '板', cantonText)
    cantonText = re.sub(r'垫', '墊', cantonText)
    cantonText = re.sub(r'埗', 'Po ', cantonText)
    cantonText = re.sub(r'堃', '坤', cantonText)
    cantonText = re.sub(r'墻', '牆', cantonText)
    cantonText = re.sub(r'壳', '殼', cantonText)
    cantonText = re.sub(r'嫲', '麻', cantonText)
    cantonText = re.sub(r'孭', 'meh ', cantonText)
    cantonText = re.sub(r'宫', '宮', cantonText)
    cantonText = re.sub(r'寃', '冤', cantonText)
    cantonText = re.sub(r'寛', '寬', cantonText)
    cantonText = re.sub(r'峯', '峰', cantonText)
    cantonText = re.sub(r'巣', '巢', cantonText)
    cantonText = re.sub(r'帮', '幫', cantonText)
    cantonText = re.sub(r'庙', '廟', cantonText)
    cantonText = re.sub(r'废', '廢', cantonText)
    cantonText = re.sub(r'廸', 'dik ', cantonText)
    cantonText = re.sub(r'廻', '迴', cantonText)
    cantonText = re.sub(r'弃', '棄', cantonText)
    cantonText = re.sub(r'弥', '彌', cantonText)
    cantonText = re.sub(r'强', '強', cantonText)
    cantonText = re.sub(r'忆', '憶', cantonText)
    cantonText = re.sub(r'忟', 'mung ', cantonText)
    cantonText = re.sub(r'忧', '懮', cantonText)
    cantonText = re.sub(r'怱', '匆', cantonText)
    cantonText = re.sub(r'恒', '恆', cantonText)
    cantonText = re.sub(r'恼', '惱', cantonText)
    cantonText = re.sub(r'愛', '愛', cantonText)
    cantonText = re.sub(r'扩', '擴', cantonText)
    cantonText = re.sub(r'抛', '拋', cantonText)
    cantonText = re.sub(r'抺', '抹', cantonText)
    cantonText = re.sub(r'拦', '攔', cantonText)
    cantonText = re.sub(r'拨', '撥', cantonText)
    cantonText = re.sub(r'换', '換', cantonText)
    cantonText = re.sub(r'掳', '擄', cantonText)
    cantonText = re.sub(r'掹', 'mung ', cantonText)
    cantonText = re.sub(r'揦', 'la ', cantonText)
    cantonText = re.sub(r'揸', 'zar ', cantonText)
    cantonText = re.sub(r'揼', 'dump ', cantonText)
    cantonText = re.sub(r'揾', '搵', cantonText)
    cantonText = re.sub(r'搅', '攪', cantonText)
    cantonText = re.sub(r'搲', '掘', cantonText)
    cantonText = re.sub(r'携', '攜', cantonText)
    cantonText = re.sub(r'撑', '掌', cantonText)
    cantonText = re.sub(r'撸', 'louk', cantonText)
    cantonText = re.sub(r'擡', '抬', cantonText)
    cantonText = re.sub(r'攞', 'lor ', cantonText)
    cantonText = re.sub(r'攰', 'gui ', cantonText)
    cantonText = re.sub(r'敍', '敘', cantonText)
    cantonText = re.sub(r'昼', '晝', cantonText)
    cantonText = re.sub(r'晩', '晚', cantonText)
    cantonText = re.sub(r'曱甴', '小強', cantonText)
    cantonText = re.sub(r'曺', '嘈', cantonText)
    cantonText = re.sub(r'术', '術', cantonText)
    cantonText = re.sub(r'枱', '台', cantonText)
    cantonText = re.sub(r'栢', '柏', cantonText)
    cantonText = re.sub(r'样', '樣', cantonText)
    cantonText = re.sub(r'梘', 'gang ', cantonText)
    cantonText = re.sub(r'様', '樣', cantonText)
    cantonText = re.sub(r'櫈', '凳', cantonText)
    cantonText = re.sub(r'歴', '歷', cantonText)
    cantonText = re.sub(r'残', '殘', cantonText)
    cantonText = re.sub(r'氷', '冰', cantonText)
    cantonText = re.sub(r'氹', 'tum ', cantonText)
    cantonText = re.sub(r'没', '沒', cantonText)
    cantonText = re.sub(r'泼', '潑', cantonText)
    cantonText = re.sub(r'涶', '唾', cantonText)
    cantonText = re.sub(r'淸', '清', cantonText)
    cantonText = re.sub(r'温', '溫', cantonText)
    cantonText = re.sub(r'溇', 'x', cantonText)
    cantonText = re.sub(r'滙', '匯', cantonText)
    cantonText = re.sub(r'滥', '濫', cantonText)
    cantonText = re.sub(r'濶', '闊', cantonText)
    cantonText = re.sub(r'焔', '焰', cantonText)
    cantonText = re.sub(r'燶', 'lone ', cantonText)
    cantonText = re.sub(r'爲', '為', cantonText)
    cantonText = re.sub(r'牀', '床', cantonText)
    cantonText = re.sub(r'犠', '犧', cantonText)
    cantonText = re.sub(r'猪', '豬', cantonText)
    cantonText = re.sub(r'猬', '蝟', cantonText)
    cantonText = re.sub(r'玮', '瑋', cantonText)
    cantonText = re.sub(r'産', '產', cantonText)
    cantonText = re.sub(r'畀', '比', cantonText)
    cantonText = re.sub(r'瘆', '慘', cantonText)
    cantonText = re.sub(r'瘪', '癟', cantonText)
    cantonText = re.sub(r'瘫', '癱', cantonText)
    cantonText = re.sub(r'瘮', '慘', cantonText)
    cantonText = re.sub(r'瘾', '癮', cantonText)
    cantonText = re.sub(r'眞', '真', cantonText)
    cantonText = re.sub(r'着', '著', cantonText)
    cantonText = re.sub(r'睺', 'hau ', cantonText)
    cantonText = re.sub(r'瞓', '訓', cantonText)
    cantonText = re.sub(r'祎', '禕', cantonText)
    cantonText = re.sub(r'祢', '你', cantonText)
    cantonText = re.sub(r'祯', '禎', cantonText)
    cantonText = re.sub(r'祷', '禱', cantonText)
    cantonText = re.sub(r'禄', '祿', cantonText)
    cantonText = re.sub(r'稣', '穌', cantonText)
    cantonText = re.sub(r'窑', 'yiu', cantonText)
    cantonText = re.sub(r'窰', 'yiu ', cantonText)
    cantonText = re.sub(r'竉', '寵', cantonText)
    cantonText = re.sub(r'笔', '筆', cantonText)
    cantonText = re.sub(r'等', '等', cantonText)
    cantonText = re.sub(r'筹', '籌', cantonText)
    cantonText = re.sub(r'箓', '籙', cantonText)
    cantonText = re.sub(r'粧', '裝', cantonText)
    cantonText = re.sub(r'糉', '粽', cantonText)
    cantonText = re.sub(r'糍', 'chi ', cantonText)
    cantonText = re.sub(r'糭', '粽', cantonText)
    cantonText = re.sub(r'紥', 'zhak ', cantonText)
    cantonText = re.sub(r'絶', '絕', cantonText)
    cantonText = re.sub(r'綉', '繡', cantonText)
    cantonText = re.sub(r'綫', '線', cantonText)
    cantonText = re.sub(r'緃', '縱', cantonText)
    cantonText = re.sub(r'约', '約', cantonText)
    cantonText = re.sub(r'纪', '記', cantonText)
    cantonText = re.sub(r'纳', '納', cantonText)
    cantonText = re.sub(r'细', '細', cantonText)
    cantonText = re.sub(r'终', '終', cantonText)
    cantonText = re.sub(r'结', '結', cantonText)
    cantonText = re.sub(r'给', '給', cantonText)
    cantonText = re.sub(r'统', '統', cantonText)
    cantonText = re.sub(r'维', '維', cantonText)
    cantonText = re.sub(r'羣', '群', cantonText)
    cantonText = re.sub(r'肤', '膚', cantonText)
    cantonText = re.sub(r'肶', '脾', cantonText)
    cantonText = re.sub(r'脚', '腳', cantonText)
    cantonText = re.sub(r'脷', '利', cantonText)
    cantonText = re.sub(r'腭', 'ngok ', cantonText)
    cantonText = re.sub(r'腻', '膩', cantonText)
    cantonText = re.sub(r'药', '藥', cantonText)
    cantonText = re.sub(r'菓', 'gwo ', cantonText)
    cantonText = re.sub(r'虚', '虛', cantonText)
    cantonText = re.sub(r'虽', '雖', cantonText)
    cantonText = re.sub(r'蚁', '蟻', cantonText)
    cantonText = re.sub(r'蛊', '蠱', cantonText)
    cantonText = re.sub(r'蝇', '蠅', cantonText)
    cantonText = re.sub(r'蟎', '蜢', cantonText)
    cantonText = re.sub(r'衆', '眾', cantonText)
    cantonText = re.sub(r'衞', '衛', cantonText)
    cantonText = re.sub(r'袮', '你', cantonText)
    cantonText = re.sub(r'裇', 'seuk ', cantonText)
    cantonText = re.sub(r'裏', '裡', cantonText)
    cantonText = re.sub(r'见', '見', cantonText)
    cantonText = re.sub(r'誉', '譽', cantonText)
    cantonText = re.sub(r'誔', '誕', cantonText)
    cantonText = re.sub(r'説', '說', cantonText)
    cantonText = re.sub(r'讃', '讚', cantonText)
    cantonText = re.sub(r'记', '記', cantonText)
    cantonText = re.sub(r'讽', '諷', cantonText)
    cantonText = re.sub(r'诗', '詩', cantonText)
    cantonText = re.sub(r'话', '話', cantonText)
    cantonText = re.sub(r'说', '說', cantonText)
    cantonText = re.sub(r'请', '請', cantonText)
    cantonText = re.sub(r'课', '課', cantonText)
    cantonText = re.sub(r'谢', '謝', cantonText)
    cantonText = re.sub(r'赋', '賦', cantonText)
    cantonText = re.sub(r'踎', 'mau ', cantonText)
    cantonText = re.sub(r'踪', '蹤', cantonText)
    cantonText = re.sub(r'踭', 'zoung ', cantonText)
    cantonText = re.sub(r'躭', '耽', cantonText)
    cantonText = re.sub(r'軚', 'tie ', cantonText)
    cantonText = re.sub(r'边', '邊', cantonText)
    cantonText = re.sub(r'逹', '達', cantonText)
    cantonText = re.sub(r'逻', '邏', cantonText)
    cantonText = re.sub(r'邓', '鄧', cantonText)
    cantonText = re.sub(r'邨', '村', cantonText)
    cantonText = re.sub(r'酦', '. ', cantonText)
    cantonText = re.sub(r'酶', '酉每', cantonText)
    cantonText = re.sub(r'释', '釋', cantonText)
    cantonText = re.sub(r'鈎', '勾', cantonText)
    cantonText = re.sub(r'鉢', '缽', cantonText)
    cantonText = re.sub(r'銹', '鏽', cantonText)
    cantonText = re.sub(r'錬', '鏈', cantonText)
    cantonText = re.sub(r'鍁', '欣', cantonText)
    cantonText = re.sub(r'鍳', '鑒', cantonText)
    cantonText = re.sub(r'鎅', 'gai ', cantonText)
    cantonText = re.sub(r'鐧', '簡', cantonText)
    cantonText = re.sub(r'镕', 'yeun ', cantonText)
    cantonText = re.sub(r'閙', '鬧', cantonText)
    cantonText = re.sub(r'閲', '閱', cantonText)
    cantonText = re.sub(r'闻', '聞', cantonText)
    cantonText = re.sub(r'随', '隨', cantonText)
    cantonText = re.sub(r'隣', '鄰', cantonText)
    cantonText = re.sub(r'雳', '靂', cantonText)
    cantonText = re.sub(r'频', '頻', cantonText)
    cantonText = re.sub(r'餸', 'sung ', cantonText)
    cantonText = re.sub(r'饭', '飯', cantonText)
    cantonText = re.sub(r'駡', '罵', cantonText)
    cantonText = re.sub(r'験', '驗', cantonText)
    cantonText = re.sub(r'鯭', 'mank', cantonText)
    cantonText = re.sub(r'鰂', '魚則', cantonText)
    cantonText = re.sub(r'鰐', '鱷', cantonText)
    cantonText = re.sub(r'鱲', 'Lap ', cantonText)
    cantonText = re.sub(r'麽', '麼', cantonText)
    cantonText = re.sub(r'스', 'x', cantonText)
    cantonText = re.sub(r'트', '', cantonText)
    cantonText = re.sub(r'풀', '阿門', cantonText)
    cantonText = re.sub(r'�', '', cantonText)
    return cantonText
p_list = list(p2c_dict.keys())
print(sorted(p_list))
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
    sstr = sstr.replace('網上直播', '')
    sstr = text_transform_cantonStyle2normalStyle(
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

sermon_tex_filepath = f"../../build/YFCX/sermon_YFCX.tex"
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/Youtube Channel:/Youtube Channel: 播道會恩福堂 Yan Fook Church/' > " + sermon_tex_filepath)

# --------------------------------------
# index table partitioned by preachers
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC in chronicle order")
with open(sermon_tex_filepath, "a") as fp:
    sermonCnt = 0
    # p_prev = ''
    # p_curr = ''
    # p_id = 0
    fp.write("{ \\scriptsize\n")
    # --------------------------------------
    # start of TOC table
    # --------------------------------------
    fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
    fp.write("\\hline\n")
    # --------------------------------------
    # lines is the line content in index_byt
    # --------------------------------------
    for lineId in range(len(lines)):
        line = lines[lineId]
        cc = line.split(",")[0]
        # --------------------------------------
        # only include this code cc if it is
        # ready in the transcription folder
        # --------------------------------------
        if os.path.isfile(f'../../data/YFCX/{cc}.txt'):
            sermonCnt += 1
            # p_prev = p_curr
            # p_curr = c2p_dict.get(cc)
            # if p_prev != p_curr:
            #     p_id += 1
            #     fp.write("\\multicolumn{4}{c}{} \\\\\n")
            #     fp.write("\\multicolumn{4}{c}{\\hyperref[ch:preacher"+str(p_id)+"]{"+p_curr+"}} \\\\\n") # <----------- this defines the column num
            #     fp.write("\\multicolumn{4}{c}{} \\\\\n")
            #     fp.write("\\hline\n")
            pstr = c2p_dict.get(cc, ' ')
            bstr = c2b_dict.get(cc, ' ')
            vstr = c2v_dict.get(cc, ' ')
            sstr = c2s_dict.get(cc, ' ')
            sstr = yfcx_sermon_title_processing(cc)
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
# p_prev = ''
# p_curr = ''
# p_id = 0
cc_prev = ''
cc_next = ''
# --------------------------------------
# lines is the line content in index_byt
# --------------------------------------
for lineId in range(len(lines)):
    line = lines[lineId]
    cc = line.split(",")[0]
    cc_prev = lines[(lineId-1)%len(lines)].split(",")[0]
    cc_next = lines[(lineId+1)%len(lines)].split(",")[0]
    if os.path.isfile(f'../../data/YFCX/{cc}.txt'):
        # p_prev = p_curr
        # p_curr = c2p_dict.get(cc)
        # if p_prev != p_curr:
        #     progressStepCnt += 1
        #     print(f"Step {progressStepCnt}: a new preacher {p_curr} is reached !")
        #     p_id += 1
        #     with open(sermon_tex_filepath, "a") as fp:
        #         # ------------------------------------
        #         # chapter toc
        #         fp.write("\n\n\\chapter{"+p_curr+"}")
        #         fp.write("\label{ch:preacher"+str(p_id)+"}\n")
        #         fp.write("\\begin{multicols}{3}\n")
        #         fp.write("\\minitoc\n")
        #         fp.write("\\end{multicols}\n")
        #         # END OF chapter toc
        #         # ------------------------------------
        #         # ------------------------------------
        #         # chapter tabular-toc with sermon title
        #         fp.write("{ \\scriptsize\n")
        #         fp.write("\n\n\\begin{xltabular}{\\textwidth}{|p{0.15\\textwidth} p{0.6\\textwidth}|p{0.07\\textwidth} p{0.1\\textwidth}|}\n") # lllr: bk+v/ch, theme, date, youtube-code
        #         fp.write("\\hline\n")
        #         for lineId_ in range(len(lines)):
        #             line_ = lines[lineId_]
        #             cc_ = line_.split(",")[0]
        #             if os.path.isfile(f'../../data/JNG/{cc_}.txt') and p_curr == c2p_dict.get(cc_):
        #                 bstr = c2b_dict.get(cc_, ' ')
        #                 vstr = c2v_dict.get(cc_, ' ')
        #                 sstr = text_transform_cantonStyle2normalStyle(
        #                     c2s_dict.get(cc_, ' ').replace('_','\_').replace('&','\&')
        #                 )
        #                 tstr = c2t_dict.get(cc_, ' ')
        #                 ystr = "\\href{https://youtube.com/watch?v=" + cc_ +"}{\\texttt{ " + cc_.replace('_','\_') + "}}"
        #                 fp.write(bstr + ' ' + vstr + " & " \
        #                          + "\\hyperref[sec:"+cc_.replace('-','_')+"]{"+sstr+"}" + " & " \
        #                          + tstr + " & " \
        #                          + ystr \
        #                          + " \\\\\n")
        #         fp.write("\\hline\n")
        #         fp.write("\\end{xltabular}\n")
        #         fp.write("}\n")
        #         # END OF chapter tabular-toc with sermon title
        #         # ------------------------------------
        #         fp.write("\\newpage\n\n")
        #     fp.close()
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
            fp.write("\\textbf{"+sstr+"}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("連結: \\href{https://youtube.com/watch?v=" + cc +"}{\\texttt{ https://youtube.com/watch?v=" + cc.replace('_','\_') + "}} ~~~~ 語音日期: " + c2t_dict.get(cc) + " \n")
            fp.write("\\newline\n\\newline\n")
            fp.write("\\hyperref[sec:"+cc_prev.replace('-','_')+"]{< < < PREV SERMON < < <}\n")
            fp.write("~\n")
            fp.write("\\hyperlink{toc}{[返主目錄]}\n")
            fp.write("~\n")
            # fp.write("\\hyperref[ch:preacher"+str(p_id)+"]{[返講員目錄]}\n")
            # fp.write("~\n")
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
            with open("../../data/YFCX/"+cc+".txt", "r") as fp_:
                the_sermon_text = fp_.read()
            fp_.close()
            the_sermon_text = text_transform_cantonStyle2normalStyle(the_sermon_text)
            the_sermon_text = the_sermon_text.replace("\\n\\n","\\n")
            textlines = the_sermon_text.split("\n")
            _textrow_cnt = 0
            textline_prev = ''
            for textline in textlines:
                if textline == textline_prev:
                    textline_prev = textline
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


