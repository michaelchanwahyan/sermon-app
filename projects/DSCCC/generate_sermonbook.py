#!/usr/local/bin/python3

from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err
from datetime import datetime, timedelta
import time
import json
import os.path
import pandas as pd

import itertools
import collections

import pickle as pkl

import math

import re
from re import compile as recompile

print('done !')
# with open("./index_byd.csv", "r") as fp:
#     lines = fp.readlines()
# fp.close()
df = pd.read_csv("./index_byd.csv")
print(f"total entry count: {df['date'].count()}")
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
def cleanse_special_char(inputText):
    txt2 = inputText \
        .replace("#", "\\#") \
        .replace("$", "\\$") \
        .replace("&amp;", '') \
        .replace("、", ",") \
        .replace("。", ".") \
        .replace("「", "``") \
        .replace("」", "\"") \
        .replace("䌓", "繁") \
        .replace("侫", "妄") \
        .replace("冲", "沖") \
        .replace("卧", "臥") \
        .replace("叠", "疊") \
        .replace("奥", "奧") \
        .replace("矝", "矜") \
        .replace("閲", "閱") \
        .replace("！", "!") \
        .replace("（", "(") \
        .replace("）", ")") \
        .replace("，", ",") \
        .replace("：", ":") \
        .replace("？", "?") \
        .replace("［", "【") \
        .replace("］", "】") \
        .replace(' &divide;', '$\\div$') \
        .replace(' X ', '$\\times$') \
        .replace('!', '!') \
        .replace('&#39;', '\'') \
        .replace('&', ' and ') \
        .replace('&Omicron;', '零') \
        .replace('&alpha;', 'α') \
        .replace('&beta;', 'β') \
        .replace('&delta;', 'δ') \
        .replace('&eacute;', '\\\'e') \
        .replace('&epsilon;', 'ε') \
        .replace('&gamma;', 'γ') \
        .replace('&hellip;', '...') \
        .replace('&iota;', 'ι') \
        .replace('&ldquo;', '``') \
        .replace('&lsquo;', '`') \
        .replace('&mdash;', '─') \
        .replace('&middot;', '$\\,\\cdot\\,$') \
        .replace('&nbsp;', '') \
        .replace('&ndash;', '─') \
        .replace('&nu;', 'ν') \
        .replace('&quot;', '\'') \
        .replace('&rdquo;', '"') \
        .replace('&rsquo;', '\'') \
        .replace('&sigma;', 'σ') \
        .replace('&sigmaf;', 'ς') \
        .replace('-&gt', '$\rightarrow$') \
        .replace('\\cs16', '') \
        .replace('\\tab', ' ') \
        .replace('\u200b', '') \
        .replace('\u3000', '~') \
        .replace('\ue00e', '洶') \
        .replace('\ue010', '憂') \
        .replace('\ue031', '步') \
        .replace('\ue045', '實') \
        .replace('\ue052', '的') \
        .replace('\ue05e', '瑟') \
        .replace('\ue05e', '繫') \
        .replace('\ue05e', '配') \
        .replace('\ue096', '芒') \
        .replace('\ue097', '呔') \
        .replace('\ue0e1', '載') \
        .replace('\ue0f5', '付') \
        .replace('\ue14c', '冤') \
        .replace('\ue17a', '使') \
        .replace('\ue1f5', '') \
        .replace('\ue226', '祐') \
        .replace('\ue233', '身') \
        .replace('\ue2de', '鬮') \
        .replace('\ue2df', '鬥') \
        .replace('\ue313', '涉') \
        .replace('\ue314', '麃') \
        .replace('\ue315', '犁') \
        .replace('\ue339', '草') \
        .replace('שְׁאוֹל&lrm;', '\sblgoodhebrew{שְׁאוֹל}') \
        .replace('ἵ', 'ι') \
        .replace('‐', '-') \
        .replace('∶', ':') \
        .replace('⋯', '...') \
        .replace('①', '(1)') \
        .replace('②', '(2)') \
        .replace('③', '(3)') \
        .replace('④', '(4)') \
        .replace('⑤', '(5)') \
        .replace('⑥', '(6)') \
        .replace('⑦', '(7)') \
        .replace('⻆', '角') \
        .replace('⾃', '自') \
        .replace('〇', '零') \
        .replace('〜', '-') \
        .replace('㖭', '添') \
        .replace('㗎', '架') \
        .replace('㩒', '禁') \
        .replace('㬹', 'zoung ') \
        .replace('㷛', '煲') \
        .replace('㷫', 'hing ') \
        .replace('㾗', '痕') \
        .replace('䌫', '纜') \
        .replace('䘵', '祿') \
        .replace('䡓', '衡') \
        .replace('䧟', '陷') \
        .replace('一', '一') \
        .replace('与', '與') \
        .replace('专', '專') \
        .replace('両', '兩') \
        .replace('两', '兩') \
        .replace('丨', '. ') \
        .replace('个', '個') \
        .replace('丶', '. ') \
        .replace('为', '為') \
        .replace('丿', '. ') \
        .replace('义', '義') \
        .replace('乸', '痴') \
        .replace('亅', '"') \
        .replace('亘', '亙') \
        .replace('亜', '亞') \
        .replace('亠', '一') \
        .replace('亵', '褻') \
        .replace('亿', '億') \
        .replace('仅', '僅') \
        .replace('们', '們') \
        .replace('仼', '任') \
        .replace('会', '會') \
        .replace('伦', '倫') \
        .replace('侓', '律') \
        .replace('侣', '侶') \
        .replace('傈', '僳') \
        .replace('僞', '偽') \
        .replace('儍', 'sor ') \
        .replace('关', '關') \
        .replace('兹', '茲') \
        .replace('内', '內') \
        .replace('冚', 'cum ') \
        .replace('冧', 'lum ') \
        .replace('决', '決') \
        .replace('况', '況') \
        .replace('凖', '準') \
        .replace('凤', '風') \
        .replace('処', '處') \
        .replace('刋', '刊') \
        .replace('刘', '劉') \
        .replace('刧', '劫') \
        .replace('别', '別') \
        .replace('刹', '剎') \
        .replace('剥', '剝') \
        .replace('劏', 'tong ') \
        .replace('劳', '勞') \
        .replace('劵', '券') \
        .replace('効', '效') \
        .replace('勲', '勳') \
        .replace('医', '醫') \
        .replace('华', '華') \
        .replace('卢', '盧') \
        .replace('卧', '臥') \
        .replace('卫', '衛') \
        .replace('却', '卻') \
        .replace('卽', '即') \
        .replace('历', '歷') \
        .replace('厠', '廁') \
        .replace('厡', '原') \
        .replace('厦', '廈') \
        .replace('厨', '廚') \
        .replace('叁', '參') \
        .replace('叄', '參') \
        .replace('发', '發') \
        .replace('叙', '敘') \
        .replace('叧', '另') \
        .replace('叶', '葉') \
        .replace('叹', '嘆') \
        .replace('吓', 'o下') \
        .replace('吔', 'ye ') \
        .replace('吖', '呀') \
        .replace('吗', '嗎') \
        .replace('吡', '悲') \
        .replace('呑', '吞') \
        .replace('呕', '') \
        .replace('咔', 'ka ') \
        .replace('咗', 'jor ') \
        .replace('咣', '剛') \
        .replace('咤', 'tak') \
        .replace('哋', '地') \
        .replace('响', '響') \
        .replace('哑', '啞') \
        .replace('哒', '躂') \
        .replace('哣', '逗') \
        .replace('唓', '即係') \
        .replace('唞', '抖') \
        .replace('唥', 'lang ') \
        .replace('唿', '弗') \
        .replace('啓', '啟') \
        .replace('啩', '掛') \
        .replace('啫', 'je ') \
        .replace('啰', 'lor ') \
        .replace('啱', 'arm ') \
        .replace('啲', 'D ') \
        .replace('啸', '嘯') \
        .replace('喆', '. ') \
        .replace('喐', 'yuk ') \
        .replace('喺', '係') \
        .replace('喼', 'gip ') \
        .replace('嗬', '嘛') \
        .replace('嗰', 'gwo ') \
        .replace('嗱', 'la ') \
        .replace('嘅', 'ge ') \
        .replace('嘘', '虛') \
        .replace('嘚', 'dik ') \
        .replace('嘞', '啦') \
        .replace('嘢', 'ye ') \
        .replace('嘣', '崩') \
        .replace('嘥', 'sai ') \
        .replace('嘨', '嘯') \
        .replace('嘭', 'bang ') \
        .replace('噃', 'bor ') \
        .replace('噏', 'up ') \
        .replace('噔', '等') \
        .replace('噜', '嚕') \
        .replace('噼', '啪') \
        .replace('嚒', '麼') \
        .replace('嚟', '黎') \
        .replace('嚿', '舊') \
        .replace('囘', '回') \
        .replace('圣', '聖') \
        .replace('坂', '板') \
        .replace('坚', '堅') \
        .replace('垫', '墊') \
        .replace('埗', 'Po ') \
        .replace('堃', '坤') \
        .replace('墻', '牆') \
        .replace('売', '殼') \
        .replace('壳', '殼') \
        .replace('够', '夠') \
        .replace('奬', '獎') \
        .replace('嫲', '麻') \
        .replace('孙', '孫') \
        .replace('学', '學') \
        .replace('孭', 'meh ') \
        .replace('宫', '宮') \
        .replace('寃', '冤') \
        .replace('寛', '寬') \
        .replace('寳', '寶') \
        .replace('尅', '剋') \
        .replace('尔', '爾') \
        .replace('属', '屬') \
        .replace('岀', '出') \
        .replace('峯', '峰') \
        .replace('巣', '巢') \
        .replace('帋', '紙') \
        .replace('带', '帶') \
        .replace('帮', '幫') \
        .replace('帺', '旗') \
        .replace('庙', '廟') \
        .replace('废', '廢') \
        .replace('廸', 'dik ') \
        .replace('廻', '迴') \
        .replace('弃', '棄') \
        .replace('弥', '彌') \
        .replace('强', '強') \
        .replace('归', '歸') \
        .replace('徧', '偏') \
        .replace('徴', '徵') \
        .replace('忆', '憶') \
        .replace('忟', 'mung ') \
        .replace('忧', '懮') \
        .replace('怱', '匆') \
        .replace('恋', '戀') \
        .replace('恒', '恆') \
        .replace('恼', '惱') \
        .replace('悏', '愜') \
        .replace('惩', '懲') \
        .replace('愛', '愛') \
        .replace('慽', '戚') \
        .replace('憇', '憩') \
        .replace('懐', '懷') \
        .replace('扩', '擴') \
        .replace('扫', '掃') \
        .replace('抛', '拋') \
        .replace('护', '護') \
        .replace('抺', '抹') \
        .replace('担', '擔') \
        .replace('拦', '攔') \
        .replace('拨', '撥') \
        .replace('捜', '搜') \
        .replace('换', '換') \
        .replace('掕', '連') \
        .replace('掦', '剔') \
        .replace('掳', '擄') \
        .replace('掹', 'mung ') \
        .replace('掺', '摻') \
        .replace('掿', '搭') \
        .replace('揑', '捏') \
        .replace('揦', 'la ') \
        .replace('揸', 'zar ') \
        .replace('揼', 'dump ') \
        .replace('揾', '搵') \
        .replace('搅', '攪') \
        .replace('搲', '掘') \
        .replace('携', '攜') \
        .replace('撃', '擊') \
        .replace('撑', '掌') \
        .replace('撵', '攆') \
        .replace('撸', 'louk') \
        .replace('擀', '幹') \
        .replace('擡', '抬') \
        .replace('擵', '摩') \
        .replace('攞', 'lor ') \
        .replace('攰', 'gui ') \
        .replace('敍', '敘') \
        .replace('敎', '教') \
        .replace('无', '無') \
        .replace('时', '時') \
        .replace('昩', '昧') \
        .replace('昻', '昂') \
        .replace('昼', '晝') \
        .replace('显', '顯') \
        .replace('晓', '曉') \
        .replace('晗', '含') \
        .replace('晩', '晚') \
        .replace('曓', '畢') \
        .replace('曱甴', '小強') \
        .replace('曺', '嘈') \
        .replace('术', '術') \
        .replace('来', '來') \
        .replace('枱', '台') \
        .replace('栅', '柵') \
        .replace('栢', '柏') \
        .replace('样', '樣') \
        .replace('梘', 'gang ') \
        .replace('榄', '欖') \
        .replace('様', '樣') \
        .replace('槪', '概') \
        .replace('横', '橫') \
        .replace('櫈', '凳') \
        .replace('歩', '步') \
        .replace('歳', '歲') \
        .replace('歴', '歷') \
        .replace('残', '殘') \
        .replace('毁', '毀') \
        .replace('毎', '每') \
        .replace('氷', '冰') \
        .replace('氹', 'tum ') \
        .replace('汚', '污') \
        .replace('汹', '洶') \
        .replace('沟', '溝') \
        .replace('没', '沒') \
        .replace('泪', '淚') \
        .replace('泼', '潑') \
        .replace('济', '濟') \
        .replace('浛', '含') \
        .replace('涙', '淚') \
        .replace('涟', '漣') \
        .replace('涨', '漲') \
        .replace('涶', '唾') \
        .replace('淸', '清') \
        .replace('渊', '淵') \
        .replace('温', '溫') \
        .replace('溇', 'x') \
        .replace('滙', '匯') \
        .replace('滞', '淨') \
        .replace('满', '滿') \
        .replace('滥', '濫') \
        .replace('濶', '闊') \
        .replace('瀞', '靜') \
        .replace('灯', '燈') \
        .replace('焔', '焰') \
        .replace('煊', '宣') \
        .replace('煑', '煮') \
        .replace('燶', 'lone ') \
        .replace('爱', '愛') \
        .replace('爲', '為') \
        .replace('牀', '床') \
        .replace('犂', '犁') \
        .replace('犠', '犧') \
        .replace('犹', '猶') \
        .replace('猪', '豬') \
        .replace('猫', '貓') \
        .replace('猬', '蝟') \
        .replace('献', '獻') \
        .replace('玮', '瑋') \
        .replace('珏', '玉') \
        .replace('産', '產') \
        .replace('畀', '比') \
        .replace('畧', '略') \
        .replace('疗', '療') \
        .replace('疮', '瘡') \
        .replace('痪', '瘓') \
        .replace('瘆', '慘') \
        .replace('瘪', '癟') \
        .replace('瘫', '癱') \
        .replace('瘮', '慘') \
        .replace('瘾', '癮') \
        .replace('癎', '癇') \
        .replace('眞', '真') \
        .replace('着', '著') \
        .replace('睺', 'hau ') \
        .replace('瞓', '訓') \
        .replace('码', '碼') \
        .replace('硏', '研') \
        .replace('磫', '蹤') \
        .replace('礴', 'bok') \
        .replace('礼', '禮') \
        .replace('祎', '禕') \
        .replace('祢', '你') \
        .replace('祯', '禎') \
        .replace('祷', '禱') \
        .replace('祸', '禍') \
        .replace('禄', '祿') \
        .replace('稣', '穌') \
        .replace('稳', '穩') \
        .replace('穏', '穩') \
        .replace('窍', '竊') \
        .replace('窑', 'yiu') \
        .replace('窦', '竇') \
        .replace('窰', 'yiu ') \
        .replace('竈', '灶') \
        .replace('竉', '寵') \
        .replace('竪', '豎') \
        .replace('笔', '筆') \
        .replace('等', '等') \
        .replace('筹', '籌') \
        .replace('箓', '籙') \
        .replace('粃', '秕') \
        .replace('粧', '裝') \
        .replace('糉', '粽') \
        .replace('糍', 'chi ') \
        .replace('糭', '粽') \
        .replace('紥', 'zhak ') \
        .replace('絶', '絕') \
        .replace('綉', '繡') \
        .replace('綫', '線') \
        .replace('緃', '縱') \
        .replace('緍', '婚') \
        .replace('纎', '纖') \
        .replace('纒', '纏') \
        .replace('约', '約') \
        .replace('级', '級') \
        .replace('纪', '記') \
        .replace('纳', '納') \
        .replace('纹', '紋') \
        .replace('细', '細') \
        .replace('终', '終') \
        .replace('结', '結') \
        .replace('给', '給') \
        .replace('统', '統') \
        .replace('维', '維') \
        .replace('罗', '羅') \
        .replace('羣', '群') \
        .replace('耻', '恥') \
        .replace('聴', '聽') \
        .replace('聼', '聽') \
        .replace('肠', '腸') \
        .replace('肤', '膚') \
        .replace('肶', '脾') \
        .replace('胆', '膽') \
        .replace('胧', '朧') \
        .replace('胶', '交') \
        .replace('脚', '腳') \
        .replace('脷', '利') \
        .replace('腭', 'ngok ') \
        .replace('腻', '膩') \
        .replace('舎', '舍') \
        .replace('苏', '蘇') \
        .replace('荣', '榮') \
        .replace('荧', '螢') \
        .replace('药', '藥') \
        .replace('莱', '萊') \
        .replace('菓', 'gwo ') \
        .replace('葱', '蔥') \
        .replace('藴', '蘊') \
        .replace('虚', '虛') \
        .replace('虽', '雖') \
        .replace('蚁', '蟻') \
        .replace('蛊', '蠱') \
        .replace('蝇', '蠅') \
        .replace('蟎', '蜢') \
        .replace('衆', '眾') \
        .replace('衞', '衛') \
        .replace('衠', '衡') \
        .replace('袐', '秘') \
        .replace('袮', '你') \
        .replace('裇', 'seuk ') \
        .replace('裏', '裡') \
        .replace('见', '見') \
        .replace('誉', '譽') \
        .replace('誔', '誕') \
        .replace('説', '說') \
        .replace('譲', '讓') \
        .replace('讃', '讚') \
        .replace('讉', '譴') \
        .replace('订', '訂') \
        .replace('记', '記') \
        .replace('讽', '諷') \
        .replace('设', '設') \
        .replace('识', '識') \
        .replace('诗', '詩') \
        .replace('诚', '誠') \
        .replace('话', '話') \
        .replace('说', '說') \
        .replace('请', '請') \
        .replace('课', '課') \
        .replace('谢', '謝') \
        .replace('貎', '貌') \
        .replace('败', '敗') \
        .replace('费', '費') \
        .replace('赋', '賦') \
        .replace('赐', '賜') \
        .replace('踎', 'mau ') \
        .replace('踨', '蹤') \
        .replace('踪', '蹤') \
        .replace('踭', 'zoung ') \
        .replace('躭', '耽') \
        .replace('軚', 'tie ') \
        .replace('輭', '軟') \
        .replace('辅', '輔') \
        .replace('辈', '輩') \
        .replace('辧', '辦') \
        .replace('边', '邊') \
        .replace('这', '這') \
        .replace('远', '遠') \
        .replace('迹', '跡') \
        .replace('逊', '遜') \
        .replace('递', '遞') \
        .replace('逹', '達') \
        .replace('逻', '邏') \
        .replace('邓', '鄧') \
        .replace('邨', '村') \
        .replace('邮', '郵') \
        .replace('鄕', '鄉') \
        .replace('酙', '酌') \
        .replace('酦', '. ') \
        .replace('酶', '酉每') \
        .replace('释', '釋') \
        .replace('鈎', '勾') \
        .replace('鉄', '鐵') \
        .replace('鉢', '缽') \
        .replace('銹', '鏽') \
        .replace('錬', '鏈') \
        .replace('鍁', '欣') \
        .replace('鍳', '鑒') \
        .replace('鎅', 'gai ') \
        .replace('鐡', '鐵') \
        .replace('鐧', '簡') \
        .replace('鑬', '纜') \
        .replace('镕', 'yeun ') \
        .replace('閙', '鬧') \
        .replace('関', '關') \
        .replace('閲', '閱') \
        .replace('闻', '聞') \
        .replace('阳', '陽') \
        .replace('険', '險') \
        .replace('随', '隨') \
        .replace('隐', '隱') \
        .replace('隠', '隱') \
        .replace('隣', '鄰') \
        .replace('雑', '雜') \
        .replace('雳', '靂') \
        .replace('靑', '青') \
        .replace('靱', '韌') \
        .replace('顔', '顏') \
        .replace('顶', '頂') \
        .replace('顺', '順') \
        .replace('顿', '頓') \
        .replace('领', '領') \
        .replace('频', '頻') \
        .replace('餸', 'sung ') \
        .replace('饭', '飯') \
        .replace('饿', '餓') \
        .replace('駄', '馱') \
        .replace('駡', '罵') \
        .replace('験', '驗') \
        .replace('髗', '髏') \
        .replace('髪', '髮') \
        .replace('鯭', 'mank') \
        .replace('鰂', '魚則') \
        .replace('鰐', '鱷') \
        .replace('鱲', 'Lap ') \
        .replace('鲁', '魯') \
        .replace('鷄', '雞') \
        .replace('鹷', '齡') \
        .replace('麪', '麵') \
        .replace('麽', '麼') \
        .replace('黒', '黑') \
        .replace('스', 'x') \
        .replace('트', '') \
        .replace('풀', '阿門') \
        .replace('﹑', '、') \
        .replace('﹟', '\#') \
        .replace('﹣', '-') \
        .replace('＂', '"') \
        .replace('０', '0') \
        .replace('１', '1') \
        .replace('２', '2') \
        .replace('３', '3') \
        .replace('４', '4') \
        .replace('５', '5') \
        .replace('６', '6') \
        .replace('７', '7') \
        .replace('８', '8') \
        .replace('９', '9') \
        .replace('～', '-') \
        .replace('｢', '「') \
        .replace('｣', '」') \
        .strip()
    return txt2
# the bible books
book_list = [
    '創世記','出埃及記','利未記','民數記','申命記',
    '約書亞記','士師記','路得記','撒母耳記上','撒母耳記下','列王記上','列王記下',
    '歷代志上','歷代志下','以斯拉記','尼希米記','以斯帖記',
    '約伯記','詩篇','箴言','傳道書','雅歌',
    '以賽亞書','耶利米書','耶利米哀歌','以西結書','但以理書',
    '何西阿書','約珥書','阿摩司書','俄巴底亞書','約拿書','彌迦書',
    '那鴻書','哈巴谷書','西番雅書','哈該書','撒迦利亞書','瑪拉基書',
    '馬太福音','馬可福音','路加福音','約翰福音','使徒行傳',
    '羅馬書','哥林多前書','哥林多後書','加拉太書','以弗所書',
    '腓立比書','歌羅西書','帖撒羅尼迦前書','帖撒羅尼迦後書',
    '提摩太前書','提摩太後書','提多書','腓利門書','希伯來書',
    '雅各書','彼得前書','彼得後書','約翰一書','約翰二書',
    '約翰三書','猶大書','啟示錄']
bible_srcpath = '../../data/bible_src/cuv2/'
book_list_engsymbol = [
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

'''## Start of sermon tex generation'''
# def sermon_tex_generation():
progressStepCnt = 0
sermon_tex_filepath = '../../build/DSCCC/sermon_DSCCC.tex'
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/崇基神學院 崇拜講章/' | sed 's/Youtube Channel:/Chaplaincy, Div. Scl. of CCC/' > " + sermon_tex_filepath)

# --------------------------------------
# index table
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC")

# year-month integer for comparison
ym_prev = -1
ym_curr = -1
with open(sermon_tex_filepath, "a") as fp:
    fp.write("\\section{目錄}\\label{sec:toc}\n")
    fp.write("{ \\scriptsize\n")
    fp.write("\n\n\\begin{xltabular}{\\textwidth}" + \
             "{|p{0.15\\textwidth}|p{0.15\\textwidth}|p{0.4\\textwidth}|p{0.3\\textwidth}|}\n")
    # lllr: |Date | Preacher | Title | Coverage |
    #        0.15   0.15    0.3        0.4
    fp.write("\\hline\n")
    fp.write("日期 & 講員 & 經課 & 講題 \\\\\n")
    for index, row in df.iterrows():
        dt = row['date']
        ym_curr = int(dt / 100) # obtain current sermon's year-month integer
        sermondt = str(dt)
        titlestr = row['title']
        preacher = row['preacher']
        if is_float(row['coverage']):
            bv = ''
        else:
            bv = row['coverage']
        # ---------------------------------------------
        # start of tex string content
        # preparation for current item
        # ---------------------------------------------
        toc_tex_str = ""
        # if year-month is changed, add double hline for spacing
        if ym_prev != ym_curr:
            toc_tex_str += "\\hline\n\\hline\n"
            ym_prev = ym_curr
        dt_ = ''
        dt_ += sermondt[0:4] + '年'
        if sermondt[4] != '0':
            dt_ += sermondt[4]
        dt_ += sermondt[5] + '月'
        if sermondt[6] != '0':
            dt_ += sermondt[6]
        dt_ += sermondt[7] + '日'
        toc_tex_str += dt_ + " & "
        toc_tex_str += cleanse_special_char(preacher) + " & "
        toc_tex_str += bv + " & "
        toc_tex_str += "\hyperref[sec:"+str(index)+"]{"+cleanse_special_char(titlestr)+"} \\\\\n"
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
dsccc_path = '../../data/DSCCC/'
index_prev = '' # previous sermon dataframe index
index_curr = '' # current sermon dataframe index
index_next = '' # next sermon dataframe index

# to regex search url pattern
url_pattern_regexp = re.compile(r'[A-Za-z0-9/_\-?.=&:]')

for index, row in df.iterrows():
    # if index == 512:
    #     break
    if (index+1) % 100 == 0:
        print(f"{index+1} / {df['date'].count()}")
    # index for latex cross reference
    index_curr = index
    index_prev = max(index_curr-1, 0)
    index_next = index_curr+1
    # get ready the dictionary info
    sermondt = str(row['date'])
    titlestr = row['title']
    titlestr = cleanse_special_char(titlestr)
    preacher = row['preacher']
    preacher = cleanse_special_char(preacher)
    if is_float(row['coverage']):
        bv = ''
    else:
        bv = row['coverage']
    dsccc_sermon_pathfilename = f'{dsccc_path}{sermondt}_{titlestr}.txt'
    if os.path.isfile(dsccc_sermon_pathfilename):
        # --------------------------------------
        # read in sermon
        # --------------------------------------
        with open(dsccc_sermon_pathfilename, 'r') as fp_dsccc_src:
            sermon_lines = fp_dsccc_src.readlines()
            sermon_lines = [ sermon_line.strip() for sermon_line in sermon_lines if '_sermon' not in sermon_line]
            sermon_lines = [ sermon_line for sermon_line in sermon_lines if len(sermon_line) ]
        fp_dsccc_src.close()
        with open(sermon_tex_filepath, "a") as fp:
            # --------------------------------------
            # print out sermon headers
            # --------------------------------------
            fp.write("\n\n\\newpage\n\n\\section{" + titlestr + "}\n")
            fp.write("\\label{sec:" + str(index_curr) + "}\n")
            fp.write("\\textbf{" + cleanse_special_char(sermon_lines[0]) + "}\n")
            fp.write("\\newline\n\\newline\n")
            fp.write("\\hyperref[sec:"+str(index_prev)+"]{< < < PREV SERMON < < <}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:toc]{[返目錄]}\n")
            fp.write("~\n")
            fp.write("\\hyperref[sec:"+str(index_next)+"]{> > > NEXT SERMON > > >}\n")
            fp.write("\n\n")
            # --------------------------------------
            # print out sermon bible verse coverage (if any)
            # --------------------------------------
            #print(f"bible coverage: {bv}")
            bkCnt = bv.count(';')+1
            if bv == '':
                bkCnt = 0
            #print(f"number of books: {bkCnt}")
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
            if bkCnt > 0:
                chisymbol_list = []
                engsymbol_list = []
                cv_list = []
                bkFound = False
                if bkCnt == 1:
                    for (chisymbol, engsymbol) in zip(book_list, book_list_engsymbol):
                        if chisymbol in bv:
                            chisymbol_list.append(chisymbol)
                            engsymbol_list.append(engsymbol)
                            bkFound = True
                    for char_idx in range(len(bv)):
                        char_curr = bv[char_idx]
                        if char_curr not in '0123456789:-,':
                            continue
                        else:
                            cv_list.append(bv[char_idx:])
                            break
                else: # i.e. if there are more books,
                    # then we need to capture bv in sequential order
                    bv_segments = bv.split(';')
                    for bv_seg in bv_segments:
                        for (chisymbol, engsymbol) in zip(book_list, book_list_engsymbol):
                            if chisymbol in bv_seg:
                                chisymbol_list.append(chisymbol)
                                engsymbol_list.append(engsymbol)
                                bkFound = True
                        cv_curr = ''
                        for char_idx in range(len(bv_seg)):
                            char_curr = bv_seg[char_idx]
                            if char_curr not in '0123456789:-,':
                                continue
                            elif char_curr == ';':
                                break
                            else:
                                cv_curr += char_curr
                        cv_list.append(cv_curr)
                # print(f'book found ! {chisymbol_list} {engsymbol_list}')
                # print(cv_list)
                # print()
                bvc = []
                for (chisymbol, engsymbol, v) in zip(chisymbol_list, engsymbol_list, cv_list):
                    # print(f" to cater{chisymbol} {v}")
                    bvc_curr = ''
                    srcfname = bible_srcpath + engsymbol + ".txt"
                    with open(srcfname, 'r') as fp_bible:
                        bktxtlines = fp_bible.readlines()
                    fp_bible.close()
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
                        if ',' in vn1:
                            vn1 = vn1.split(',')[0]
                        elif ',' in vn2:
                            vn2 = vn2.split(',')[-1]
                    # case 2 -> A:B-C-D-...-X
                    elif v.count(':') == 1 and v.count('-') > 1:
                        vs = v.split(':')
                        cn1 = vs[0]
                        cn2 = cn1
                        vn1 = vs[1].split('-')[0]
                        vn2 = vs[1].split('-')[-1]
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
                            bvc_curr += bktxtline
                        if not h2_reached:
                            h2_reached = header2 in bktxtline[:len(header2)]
                        if h2_reached:
                            break
                    bvc.append(chisymbol + ' ' + v + '\n\n' + bvc_curr)
                # END OF for (chisymbol, engsymbol, v) in zip(chisymbol_list, engsymbol_list, cv_list):
                # print(bvc)
                # if len(bvc) == 0:
                #     print(bv)
                #     print(bvc)
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
                # ----------------------
                # add the scripture part
                for bvc_curr in bvc:
                    # bvc is the list of scripture.
                    # often there contains 3 to 4 books
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
            # --------------------------------------
            # print out sermon main content
            # --------------------------------------
            for sermon_line in sermon_lines[1:]: # the first line is already textbf above
                # --------------------------------------
                # tex url handling multiple number of http in the same line
                # --------------------------------------
                urlidx_start = 0
                urlidx_end = 0
                while urlidx_start != -1:
                    urlidx_start = sermon_line.find('http', urlidx_end) # find 'http' pattern
                    urlidx_end = urlidx_start
                    for char_curr in sermon_line[urlidx_start:]:
                        if url_pattern_regexp.search(char_curr):
                            urlidx_end += 1
                        else:
                            break
                    if urlidx_start != -1: # if 'http' pattern is never found, it is -1
                        sermon_line = sermon_line[:urlidx_start] + "\\url{" + sermon_line[urlidx_start:urlidx_end] + "}" + sermon_line[urlidx_end:]
                fp.write(cleanse_special_char(sermon_line) + "\n\n")
        fp.close() # close of with open(sermon_tex_filepath, "a") as fp:
    else:
        print(f"{dsccc_sermon_pathfilename} is not found !")
        continue
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


