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
    txt2 = inputText
    txt2 = txt2.replace("#", "\\#")
    txt2 = txt2.replace("$", "\\$")
    txt2 = txt2.replace("&amp;", '')
    txt2 = txt2.replace("、", ",")
    txt2 = txt2.replace("。", ".")
    txt2 = txt2.replace("「", "``")
    txt2 = txt2.replace("」", "\"")
    txt2 = txt2.replace("䌓", "繁")
    txt2 = txt2.replace("侫", "妄")
    txt2 = txt2.replace("冲", "沖")
    txt2 = txt2.replace("卧", "臥")
    txt2 = txt2.replace("叠", "疊")
    txt2 = txt2.replace("奥", "奧")
    txt2 = txt2.replace("矝", "矜")
    txt2 = txt2.replace("閲", "閱")
    txt2 = txt2.replace("！", "!")
    txt2 = txt2.replace("（", "(")
    txt2 = txt2.replace("）", ")")
    txt2 = txt2.replace("，", ",")
    txt2 = txt2.replace("：", ":")
    txt2 = txt2.replace("？", "?")
    txt2 = txt2.replace("［", "【")
    txt2 = txt2.replace("］", "】")
    txt2 = txt2.replace(' &divide;', '$\\div$')
    txt2 = txt2.replace(' X ', '$\\times$')
    txt2 = txt2.replace('!', '!')
    txt2 = txt2.replace('&#39;', '\'')
    txt2 = txt2.replace('&', ' and ')
    txt2 = txt2.replace('&Omicron;', '零')
    txt2 = txt2.replace('&alpha;', 'α')
    txt2 = txt2.replace('&beta;', 'β')
    txt2 = txt2.replace('&delta;', 'δ')
    txt2 = txt2.replace('&eacute;', '\\\'e')
    txt2 = txt2.replace('&epsilon;', 'ε')
    txt2 = txt2.replace('&gamma;', 'γ')
    txt2 = txt2.replace('&hellip;', '...')
    txt2 = txt2.replace('&iota;', 'ι')
    txt2 = txt2.replace('&ldquo;', '``')
    txt2 = txt2.replace('&lsquo;', '`')
    txt2 = txt2.replace('&mdash;', '─')
    txt2 = txt2.replace('&middot;', '$\\,\\cdot\\,$')
    txt2 = txt2.replace('&nbsp;', '')
    txt2 = txt2.replace('&ndash;', '─')
    txt2 = txt2.replace('&nu;', 'ν')
    txt2 = txt2.replace('&quot;', '\'')
    txt2 = txt2.replace('&rdquo;', '"')
    txt2 = txt2.replace('&rsquo;', '\'')
    txt2 = txt2.replace('&sigma;', 'σ')
    txt2 = txt2.replace('&sigmaf;', 'ς')
    txt2 = txt2.replace('-&gt', '$\rightarrow$')
    txt2 = txt2.replace('\\cs16', '')
    txt2 = txt2.replace('\\tab', ' ')
    txt2 = txt2.replace('\u200b', '')
    txt2 = txt2.replace('\u3000', '~')
    txt2 = txt2.replace('\ue00e', '洶')
    txt2 = txt2.replace('\ue010', '憂')
    txt2 = txt2.replace('\ue031', '步')
    txt2 = txt2.replace('\ue045', '實')
    txt2 = txt2.replace('\ue052', '的')
    txt2 = txt2.replace('\ue05e', '瑟')
    txt2 = txt2.replace('\ue05e', '繫')
    txt2 = txt2.replace('\ue05e', '配')
    txt2 = txt2.replace('\ue096', '芒')
    txt2 = txt2.replace('\ue097', '呔')
    txt2 = txt2.replace('\ue0e1', '載')
    txt2 = txt2.replace('\ue0f5', '付')
    txt2 = txt2.replace('\ue14c', '冤')
    txt2 = txt2.replace('\ue17a', '使')
    txt2 = txt2.replace('\ue1f5', '')
    txt2 = txt2.replace('\ue226', '祐')
    txt2 = txt2.replace('\ue233', '身')
    txt2 = txt2.replace('\ue2de', '鬮')
    txt2 = txt2.replace('\ue2df', '鬥')
    txt2 = txt2.replace('\ue313', '涉')
    txt2 = txt2.replace('\ue314', '麃')
    txt2 = txt2.replace('\ue315', '犁')
    txt2 = txt2.replace('\ue339', '草')
    txt2 = txt2.replace('שְׁאוֹל&lrm;', '\sblgoodhebrew{שְׁאוֹל}')
    txt2 = txt2.replace('ἵ', 'ι')
    txt2 = txt2.replace('‐', '-')
    txt2 = txt2.replace('∶', ':')
    txt2 = txt2.replace('⋯', '...')
    txt2 = txt2.replace('①', '(1)')
    txt2 = txt2.replace('②', '(2)')
    txt2 = txt2.replace('③', '(3)')
    txt2 = txt2.replace('④', '(4)')
    txt2 = txt2.replace('⑤', '(5)')
    txt2 = txt2.replace('⑥', '(6)')
    txt2 = txt2.replace('⑦', '(7)')
    txt2 = txt2.replace('╱', '/')
    txt2 = txt2.replace('⻆', '角')
    txt2 = txt2.replace('⾃', '自')
    txt2 = txt2.replace('〇', '零')
    txt2 = txt2.replace('〜', '-')
    txt2 = txt2.replace('㖭', '添')
    txt2 = txt2.replace('㗎', '架')
    txt2 = txt2.replace('㩒', '禁')
    txt2 = txt2.replace('㬹', 'zoung ')
    txt2 = txt2.replace('㷛', '煲')
    txt2 = txt2.replace('㷫', 'hing ')
    txt2 = txt2.replace('㾗', '痕')
    txt2 = txt2.replace('䌫', '纜')
    txt2 = txt2.replace('䘵', '祿')
    txt2 = txt2.replace('䡓', '衡')
    txt2 = txt2.replace('䧟', '陷')
    txt2 = txt2.replace('一', '一')
    txt2 = txt2.replace('与', '與')
    txt2 = txt2.replace('专', '專')
    txt2 = txt2.replace('両', '兩')
    txt2 = txt2.replace('两', '兩')
    txt2 = txt2.replace('丨', '. ')
    txt2 = txt2.replace('个', '個')
    txt2 = txt2.replace('丶', '. ')
    txt2 = txt2.replace('为', '為')
    txt2 = txt2.replace('丿', '. ')
    txt2 = txt2.replace('义', '義')
    txt2 = txt2.replace('乸', '痴')
    txt2 = txt2.replace('亅', '"')
    txt2 = txt2.replace('争', '爭')
    txt2 = txt2.replace('亘', '亙')
    txt2 = txt2.replace('亜', '亞')
    txt2 = txt2.replace('亠', '一')
    txt2 = txt2.replace('亵', '褻')
    txt2 = txt2.replace('亿', '億')
    txt2 = txt2.replace('仅', '僅')
    txt2 = txt2.replace('们', '們')
    txt2 = txt2.replace('仭', '仞')
    txt2 = txt2.replace('仼', '任')
    txt2 = txt2.replace('会', '會')
    txt2 = txt2.replace('伦', '倫')
    txt2 = txt2.replace('侓', '律')
    txt2 = txt2.replace('侣', '侶')
    txt2 = txt2.replace('傈', '僳')
    txt2 = txt2.replace('僞', '偽')
    txt2 = txt2.replace('儍', 'sor ')
    txt2 = txt2.replace('关', '關')
    txt2 = txt2.replace('兹', '茲')
    txt2 = txt2.replace('内', '內')
    txt2 = txt2.replace('冚', 'cum ')
    txt2 = txt2.replace('冧', 'lum ')
    txt2 = txt2.replace('决', '決')
    txt2 = txt2.replace('况', '況')
    txt2 = txt2.replace('凖', '準')
    txt2 = txt2.replace('凤', '風')
    txt2 = txt2.replace('処', '處')
    txt2 = txt2.replace('凴', '憑')
    txt2 = txt2.replace('刋', '刊')
    txt2 = txt2.replace('刘', '劉')
    txt2 = txt2.replace('刧', '劫')
    txt2 = txt2.replace('别', '別')
    txt2 = txt2.replace('刹', '剎')
    txt2 = txt2.replace('剥', '剝')
    txt2 = txt2.replace('劏', 'tong ')
    txt2 = txt2.replace('劳', '勞')
    txt2 = txt2.replace('劵', '券')
    txt2 = txt2.replace('効', '效')
    txt2 = txt2.replace('勲', '勳')
    txt2 = txt2.replace('医', '醫')
    txt2 = txt2.replace('华', '華')
    txt2 = txt2.replace('卢', '盧')
    txt2 = txt2.replace('卧', '臥')
    txt2 = txt2.replace('卫', '衛')
    txt2 = txt2.replace('却', '卻')
    txt2 = txt2.replace('卽', '即')
    txt2 = txt2.replace('历', '歷')
    txt2 = txt2.replace('厠', '廁')
    txt2 = txt2.replace('厡', '原')
    txt2 = txt2.replace('厦', '廈')
    txt2 = txt2.replace('厨', '廚')
    txt2 = txt2.replace('叁', '參')
    txt2 = txt2.replace('叄', '參')
    txt2 = txt2.replace('发', '發')
    txt2 = txt2.replace('叙', '敘')
    txt2 = txt2.replace('叧', '另')
    txt2 = txt2.replace('叶', '葉')
    txt2 = txt2.replace('叹', '嘆')
    txt2 = txt2.replace('吓', 'o下')
    txt2 = txt2.replace('吔', 'ye ')
    txt2 = txt2.replace('吖', '呀')
    txt2 = txt2.replace('吗', '嗎')
    txt2 = txt2.replace('吡', '悲')
    txt2 = txt2.replace('呑', '吞')
    txt2 = txt2.replace('呕', '')
    txt2 = txt2.replace('咔', 'ka ')
    txt2 = txt2.replace('咗', 'jor ')
    txt2 = txt2.replace('咣', '剛')
    txt2 = txt2.replace('咤', 'tak')
    txt2 = txt2.replace('哋', '地')
    txt2 = txt2.replace('响', '響')
    txt2 = txt2.replace('哑', '啞')
    txt2 = txt2.replace('哒', '躂')
    txt2 = txt2.replace('哣', '逗')
    txt2 = txt2.replace('唓', '即係')
    txt2 = txt2.replace('唞', '抖')
    txt2 = txt2.replace('唥', 'lang ')
    txt2 = txt2.replace('唿', '弗')
    txt2 = txt2.replace('啓', '啟')
    txt2 = txt2.replace('啩', '掛')
    txt2 = txt2.replace('啫', 'je ')
    txt2 = txt2.replace('啰', 'lor ')
    txt2 = txt2.replace('啱', 'arm ')
    txt2 = txt2.replace('啲', 'D ')
    txt2 = txt2.replace('啸', '嘯')
    txt2 = txt2.replace('喆', '. ')
    txt2 = txt2.replace('喐', 'yuk ')
    txt2 = txt2.replace('喺', '係')
    txt2 = txt2.replace('喼', 'gip ')
    txt2 = txt2.replace('嗬', '嘛')
    txt2 = txt2.replace('嗰', 'gwo ')
    txt2 = txt2.replace('嗱', 'la ')
    txt2 = txt2.replace('嘅', 'ge ')
    txt2 = txt2.replace('嘘', '虛')
    txt2 = txt2.replace('嘚', 'dik ')
    txt2 = txt2.replace('嘞', '啦')
    txt2 = txt2.replace('嘢', 'ye ')
    txt2 = txt2.replace('嘣', '崩')
    txt2 = txt2.replace('嘥', 'sai ')
    txt2 = txt2.replace('嘨', '嘯')
    txt2 = txt2.replace('嘭', 'bang ')
    txt2 = txt2.replace('噃', 'bor ')
    txt2 = txt2.replace('噏', 'up ')
    txt2 = txt2.replace('噔', '等')
    txt2 = txt2.replace('噜', '嚕')
    txt2 = txt2.replace('噼', '啪')
    txt2 = txt2.replace('嚒', '麼')
    txt2 = txt2.replace('嚟', '黎')
    txt2 = txt2.replace('嚿', '舊')
    txt2 = txt2.replace('囘', '回')
    txt2 = txt2.replace('囯', '國')
    txt2 = txt2.replace('国', '國')
    txt2 = txt2.replace('圣', '聖')
    txt2 = txt2.replace('坂', '板')
    txt2 = txt2.replace('坚', '堅')
    txt2 = txt2.replace('垫', '墊')
    txt2 = txt2.replace('埗', 'Po ')
    txt2 = txt2.replace('堃', '坤')
    txt2 = txt2.replace('墻', '牆')
    txt2 = txt2.replace('売', '殼')
    txt2 = txt2.replace('壳', '殼')
    txt2 = txt2.replace('够', '夠')
    txt2 = txt2.replace('奬', '獎')
    txt2 = txt2.replace('嫲', '麻')
    txt2 = txt2.replace('孙', '孫')
    txt2 = txt2.replace('学', '學')
    txt2 = txt2.replace('孭', 'meh ')
    txt2 = txt2.replace('宫', '宮')
    txt2 = txt2.replace('寃', '冤')
    txt2 = txt2.replace('寛', '寬')
    txt2 = txt2.replace('寳', '寶')
    txt2 = txt2.replace('尅', '剋')
    txt2 = txt2.replace('尔', '爾')
    txt2 = txt2.replace('属', '屬')
    txt2 = txt2.replace('岀', '出')
    txt2 = txt2.replace('峯', '峰')
    txt2 = txt2.replace('嵗', '歲')
    txt2 = txt2.replace('巣', '巢')
    txt2 = txt2.replace('帋', '紙')
    txt2 = txt2.replace('带', '帶')
    txt2 = txt2.replace('帮', '幫')
    txt2 = txt2.replace('帺', '旗')
    txt2 = txt2.replace('幷', '並')
    txt2 = txt2.replace('庙', '廟')
    txt2 = txt2.replace('废', '廢')
    txt2 = txt2.replace('廸', 'dik ')
    txt2 = txt2.replace('廻', '迴')
    txt2 = txt2.replace('弃', '棄')
    txt2 = txt2.replace('弥', '彌')
    txt2 = txt2.replace('强', '強')
    txt2 = txt2.replace('归', '歸')
    txt2 = txt2.replace('徧', '偏')
    txt2 = txt2.replace('徴', '徵')
    txt2 = txt2.replace('忆', '憶')
    txt2 = txt2.replace('忟', 'mung ')
    txt2 = txt2.replace('忧', '懮')
    txt2 = txt2.replace('怱', '匆')
    txt2 = txt2.replace('恋', '戀')
    txt2 = txt2.replace('恒', '恆')
    txt2 = txt2.replace('恼', '惱')
    txt2 = txt2.replace('悏', '愜')
    txt2 = txt2.replace('惩', '懲')
    txt2 = txt2.replace('愛', '愛')
    txt2 = txt2.replace('慽', '戚')
    txt2 = txt2.replace('憇', '憩')
    txt2 = txt2.replace('懐', '懷')
    txt2 = txt2.replace('扩', '擴')
    txt2 = txt2.replace('扫', '掃')
    txt2 = txt2.replace('抛', '拋')
    txt2 = txt2.replace('护', '護')
    txt2 = txt2.replace('抺', '抹')
    txt2 = txt2.replace('担', '擔')
    txt2 = txt2.replace('拦', '攔')
    txt2 = txt2.replace('拨', '撥')
    txt2 = txt2.replace('捜', '搜')
    txt2 = txt2.replace('换', '換')
    txt2 = txt2.replace('掕', '連')
    txt2 = txt2.replace('掦', '剔')
    txt2 = txt2.replace('掳', '擄')
    txt2 = txt2.replace('掹', 'mung ')
    txt2 = txt2.replace('掺', '摻')
    txt2 = txt2.replace('掿', '搭')
    txt2 = txt2.replace('揑', '捏')
    txt2 = txt2.replace('揦', 'la ')
    txt2 = txt2.replace('揸', 'zar ')
    txt2 = txt2.replace('揼', 'dump ')
    txt2 = txt2.replace('揾', '搵')
    txt2 = txt2.replace('搅', '攪')
    txt2 = txt2.replace('搲', '掘')
    txt2 = txt2.replace('携', '攜')
    txt2 = txt2.replace('撃', '擊')
    txt2 = txt2.replace('撑', '掌')
    txt2 = txt2.replace('撵', '攆')
    txt2 = txt2.replace('撸', 'louk')
    txt2 = txt2.replace('擀', '幹')
    txt2 = txt2.replace('擡', '抬')
    txt2 = txt2.replace('擵', '摩')
    txt2 = txt2.replace('攞', 'lor ')
    txt2 = txt2.replace('攰', 'gui ')
    txt2 = txt2.replace('敍', '敘')
    txt2 = txt2.replace('敎', '教')
    txt2 = txt2.replace('无', '無')
    txt2 = txt2.replace('旣', '既')
    txt2 = txt2.replace('时', '時')
    txt2 = txt2.replace('昩', '昧')
    txt2 = txt2.replace('昻', '昂')
    txt2 = txt2.replace('昼', '晝')
    txt2 = txt2.replace('显', '顯')
    txt2 = txt2.replace('晓', '曉')
    txt2 = txt2.replace('晗', '含')
    txt2 = txt2.replace('晩', '晚')
    txt2 = txt2.replace('曓', '畢')
    txt2 = txt2.replace('曱甴', '小強')
    txt2 = txt2.replace('曺', '嘈')
    txt2 = txt2.replace('朌', '盼')
    txt2 = txt2.replace('术', '術')
    txt2 = txt2.replace('朶', '朵')
    txt2 = txt2.replace('机', '機')
    txt2 = txt2.replace('来', '來')
    txt2 = txt2.replace('枱', '台')
    txt2 = txt2.replace('栅', '柵')
    txt2 = txt2.replace('栢', '柏')
    txt2 = txt2.replace('样', '樣')
    txt2 = txt2.replace('梘', 'gang ')
    txt2 = txt2.replace('榄', '欖')
    txt2 = txt2.replace('様', '樣')
    txt2 = txt2.replace('槪', '概')
    txt2 = txt2.replace('横', '橫')
    txt2 = txt2.replace('櫈', '凳')
    txt2 = txt2.replace('欅', '櫸')
    txt2 = txt2.replace('歩', '步')
    txt2 = txt2.replace('歳', '歲')
    txt2 = txt2.replace('歴', '歷')
    txt2 = txt2.replace('残', '殘')
    txt2 = txt2.replace('毁', '毀')
    txt2 = txt2.replace('毎', '每')
    txt2 = txt2.replace('氷', '冰')
    txt2 = txt2.replace('氹', 'tum ')
    txt2 = txt2.replace('汚', '污')
    txt2 = txt2.replace('汹', '洶')
    txt2 = txt2.replace('沟', '溝')
    txt2 = txt2.replace('没', '沒')
    txt2 = txt2.replace('泪', '淚')
    txt2 = txt2.replace('泼', '潑')
    txt2 = txt2.replace('济', '濟')
    txt2 = txt2.replace('浛', '含')
    txt2 = txt2.replace('涙', '淚')
    txt2 = txt2.replace('涟', '漣')
    txt2 = txt2.replace('涨', '漲')
    txt2 = txt2.replace('涶', '唾')
    txt2 = txt2.replace('淸', '清')
    txt2 = txt2.replace('渊', '淵')
    txt2 = txt2.replace('温', '溫')
    txt2 = txt2.replace('溇', 'x')
    txt2 = txt2.replace('滙', '匯')
    txt2 = txt2.replace('滞', '淨')
    txt2 = txt2.replace('满', '滿')
    txt2 = txt2.replace('滥', '濫')
    txt2 = txt2.replace('濶', '闊')
    txt2 = txt2.replace('瀞', '靜')
    txt2 = txt2.replace('灯', '燈')
    txt2 = txt2.replace('焔', '焰')
    txt2 = txt2.replace('煅', '鍛')
    txt2 = txt2.replace('煊', '宣')
    txt2 = txt2.replace('煑', '煮')
    txt2 = txt2.replace('燶', 'lone ')
    txt2 = txt2.replace('爱', '愛')
    txt2 = txt2.replace('爲', '為')
    txt2 = txt2.replace('牀', '床')
    txt2 = txt2.replace('犂', '犁')
    txt2 = txt2.replace('犠', '犧')
    txt2 = txt2.replace('犹', '猶')
    txt2 = txt2.replace('猪', '豬')
    txt2 = txt2.replace('猫', '貓')
    txt2 = txt2.replace('猬', '蝟')
    txt2 = txt2.replace('献', '獻')
    txt2 = txt2.replace('玮', '瑋')
    txt2 = txt2.replace('珏', '玉')
    txt2 = txt2.replace('産', '產')
    txt2 = txt2.replace('电', '電')
    txt2 = txt2.replace('畀', '比')
    txt2 = txt2.replace('畧', '略')
    txt2 = txt2.replace('疗', '療')
    txt2 = txt2.replace('疮', '瘡')
    txt2 = txt2.replace('痪', '瘓')
    txt2 = txt2.replace('瘆', '慘')
    txt2 = txt2.replace('瘪', '癟')
    txt2 = txt2.replace('瘫', '癱')
    txt2 = txt2.replace('瘮', '慘')
    txt2 = txt2.replace('瘾', '癮')
    txt2 = txt2.replace('癎', '癇')
    txt2 = txt2.replace('盗', '盜')
    txt2 = txt2.replace('眞', '真')
    txt2 = txt2.replace('着', '著')
    txt2 = txt2.replace('睺', 'hau ')
    txt2 = txt2.replace('瞓', '訓')
    txt2 = txt2.replace('瞔', '睛')
    txt2 = txt2.replace('码', '碼')
    txt2 = txt2.replace('硏', '研')
    txt2 = txt2.replace('磒', '隕')
    txt2 = txt2.replace('磫', '蹤')
    txt2 = txt2.replace('礳', '磨')
    txt2 = txt2.replace('礴', 'bok')
    txt2 = txt2.replace('礼', '禮')
    txt2 = txt2.replace('祎', '禕')
    txt2 = txt2.replace('祢', '你')
    txt2 = txt2.replace('祯', '禎')
    txt2 = txt2.replace('祷', '禱')
    txt2 = txt2.replace('祸', '禍')
    txt2 = txt2.replace('禄', '祿')
    txt2 = txt2.replace('稣', '穌')
    txt2 = txt2.replace('稳', '穩')
    txt2 = txt2.replace('穏', '穩')
    txt2 = txt2.replace('窂', '牢')
    txt2 = txt2.replace('窍', '竊')
    txt2 = txt2.replace('窑', 'yiu')
    txt2 = txt2.replace('窦', '竇')
    txt2 = txt2.replace('窰', 'yiu ')
    txt2 = txt2.replace('竈', '灶')
    txt2 = txt2.replace('竉', '寵')
    txt2 = txt2.replace('竪', '豎')
    txt2 = txt2.replace('笔', '筆')
    txt2 = txt2.replace('等', '等')
    txt2 = txt2.replace('筹', '籌')
    txt2 = txt2.replace('箓', '籙')
    txt2 = txt2.replace('粃', '秕')
    txt2 = txt2.replace('粧', '裝')
    txt2 = txt2.replace('糉', '粽')
    txt2 = txt2.replace('糍', 'chi ')
    txt2 = txt2.replace('糭', '粽')
    txt2 = txt2.replace('紥', 'zhak ')
    txt2 = txt2.replace('絶', '絕')
    txt2 = txt2.replace('綉', '繡')
    txt2 = txt2.replace('綫', '線')
    txt2 = txt2.replace('緃', '縱')
    txt2 = txt2.replace('緍', '婚')
    txt2 = txt2.replace('縂', '總')
    txt2 = txt2.replace('繋', '繫')
    txt2 = txt2.replace('纎', '纖')
    txt2 = txt2.replace('纒', '纏')
    txt2 = txt2.replace('约', '約')
    txt2 = txt2.replace('级', '級')
    txt2 = txt2.replace('纪', '記')
    txt2 = txt2.replace('纳', '納')
    txt2 = txt2.replace('纸', '紙')
    txt2 = txt2.replace('纹', '紋')
    txt2 = txt2.replace('细', '細')
    txt2 = txt2.replace('终', '終')
    txt2 = txt2.replace('结', '結')
    txt2 = txt2.replace('给', '給')
    txt2 = txt2.replace('统', '統')
    txt2 = txt2.replace('维', '維')
    txt2 = txt2.replace('缼', '缺')
    txt2 = txt2.replace('罗', '羅')
    txt2 = txt2.replace('羣', '群')
    txt2 = txt2.replace('耻', '恥')
    txt2 = txt2.replace('联', '聯')
    txt2 = txt2.replace('聴', '聽')
    txt2 = txt2.replace('聼', '聽')
    txt2 = txt2.replace('肠', '腸')
    txt2 = txt2.replace('肤', '膚')
    txt2 = txt2.replace('肶', '脾')
    txt2 = txt2.replace('胆', '膽')
    txt2 = txt2.replace('胧', '朧')
    txt2 = txt2.replace('胶', '交')
    txt2 = txt2.replace('脚', '腳')
    txt2 = txt2.replace('脷', '利')
    txt2 = txt2.replace('腭', 'ngok ')
    txt2 = txt2.replace('腻', '膩')
    txt2 = txt2.replace('舎', '舍')
    txt2 = txt2.replace('苏', '蘇')
    txt2 = txt2.replace('荣', '榮')
    txt2 = txt2.replace('荧', '螢')
    txt2 = txt2.replace('药', '藥')
    txt2 = txt2.replace('莱', '萊')
    txt2 = txt2.replace('菓', 'gwo ')
    txt2 = txt2.replace('著', '著')
    txt2 = txt2.replace('葱', '蔥')
    txt2 = txt2.replace('藴', '蘊')
    txt2 = txt2.replace('蘯', '蕩')
    txt2 = txt2.replace('虚', '虛')
    txt2 = txt2.replace('虽', '雖')
    txt2 = txt2.replace('蚁', '蟻')
    txt2 = txt2.replace('蛊', '蠱')
    txt2 = txt2.replace('蝇', '蠅')
    txt2 = txt2.replace('蟎', '蜢')
    txt2 = txt2.replace('衆', '眾')
    txt2 = txt2.replace('衞', '衛')
    txt2 = txt2.replace('衠', '衡')
    txt2 = txt2.replace('袐', '秘')
    txt2 = txt2.replace('袮', '你')
    txt2 = txt2.replace('裇', 'seuk ')
    txt2 = txt2.replace('裏', '裡')
    txt2 = txt2.replace('覊', '羈')
    txt2 = txt2.replace('见', '見')
    txt2 = txt2.replace('誉', '譽')
    txt2 = txt2.replace('誔', '誕')
    txt2 = txt2.replace('説', '說')
    txt2 = txt2.replace('譲', '讓')
    txt2 = txt2.replace('讃', '讚')
    txt2 = txt2.replace('讉', '譴')
    txt2 = txt2.replace('订', '訂')
    txt2 = txt2.replace('记', '記')
    txt2 = txt2.replace('讽', '諷')
    txt2 = txt2.replace('设', '設')
    txt2 = txt2.replace('识', '識')
    txt2 = txt2.replace('诗', '詩')
    txt2 = txt2.replace('诚', '誠')
    txt2 = txt2.replace('话', '話')
    txt2 = txt2.replace('说', '說')
    txt2 = txt2.replace('请', '請')
    txt2 = txt2.replace('课', '課')
    txt2 = txt2.replace('谢', '謝')
    txt2 = txt2.replace('谱', '譜')
    txt2 = txt2.replace('貎', '貌')
    txt2 = txt2.replace('败', '敗')
    txt2 = txt2.replace('费', '費')
    txt2 = txt2.replace('赋', '賦')
    txt2 = txt2.replace('赐', '賜')
    txt2 = txt2.replace('踎', 'mau ')
    txt2 = txt2.replace('踨', '蹤')
    txt2 = txt2.replace('踪', '蹤')
    txt2 = txt2.replace('踭', 'zoung ')
    txt2 = txt2.replace('躭', '耽')
    txt2 = txt2.replace('躱', '躲')
    txt2 = txt2.replace('軚', 'tie ')
    txt2 = txt2.replace('輭', '軟')
    txt2 = txt2.replace('辅', '輔')
    txt2 = txt2.replace('辈', '輩')
    txt2 = txt2.replace('辧', '辦')
    txt2 = txt2.replace('边', '邊')
    txt2 = txt2.replace('这', '這')
    txt2 = txt2.replace('远', '遠')
    txt2 = txt2.replace('迹', '跡')
    txt2 = txt2.replace('逊', '遜')
    txt2 = txt2.replace('递', '遞')
    txt2 = txt2.replace('逹', '達')
    txt2 = txt2.replace('逻', '邏')
    txt2 = txt2.replace('邓', '鄧')
    txt2 = txt2.replace('邨', '村')
    txt2 = txt2.replace('邮', '郵')
    txt2 = txt2.replace('鄕', '鄉')
    txt2 = txt2.replace('酙', '酌')
    txt2 = txt2.replace('酦', '. ')
    txt2 = txt2.replace('酶', '酉每')
    txt2 = txt2.replace('释', '釋')
    txt2 = txt2.replace('鈎', '勾')
    txt2 = txt2.replace('鉄', '鐵')
    txt2 = txt2.replace('鉢', '缽')
    txt2 = txt2.replace('銹', '鏽')
    txt2 = txt2.replace('錬', '鏈')
    txt2 = txt2.replace('鍁', '欣')
    txt2 = txt2.replace('鍳', '鑒')
    txt2 = txt2.replace('鎅', 'gai ')
    txt2 = txt2.replace('鐡', '鐵')
    txt2 = txt2.replace('鐧', '簡')
    txt2 = txt2.replace('鑬', '纜')
    txt2 = txt2.replace('镕', 'yeun ')
    txt2 = txt2.replace('閙', '鬧')
    txt2 = txt2.replace('関', '關')
    txt2 = txt2.replace('閲', '閱')
    txt2 = txt2.replace('闻', '聞')
    txt2 = txt2.replace('阳', '陽')
    txt2 = txt2.replace('陥', '陷')
    txt2 = txt2.replace('険', '險')
    txt2 = txt2.replace('随', '隨')
    txt2 = txt2.replace('隐', '隱')
    txt2 = txt2.replace('隠', '隱')
    txt2 = txt2.replace('隣', '鄰')
    txt2 = txt2.replace('雑', '雜')
    txt2 = txt2.replace('雳', '靂')
    txt2 = txt2.replace('靑', '青')
    txt2 = txt2.replace('靱', '韌')
    txt2 = txt2.replace('顔', '顏')
    txt2 = txt2.replace('顕', '顯')
    txt2 = txt2.replace('顶', '頂')
    txt2 = txt2.replace('顺', '順')
    txt2 = txt2.replace('顿', '頓')
    txt2 = txt2.replace('领', '領')
    txt2 = txt2.replace('频', '頻')
    txt2 = txt2.replace('颗', '顆')
    txt2 = txt2.replace('餸', 'sung ')
    txt2 = txt2.replace('饭', '飯')
    txt2 = txt2.replace('饿', '餓')
    txt2 = txt2.replace('駄', '馱')
    txt2 = txt2.replace('駡', '罵')
    txt2 = txt2.replace('験', '驗')
    txt2 = txt2.replace('髗', '髏')
    txt2 = txt2.replace('髪', '髮')
    txt2 = txt2.replace('鬬', '鬥')
    txt2 = txt2.replace('鯭', 'mank')
    txt2 = txt2.replace('鰂', '魚則')
    txt2 = txt2.replace('鰐', '鱷')
    txt2 = txt2.replace('鱲', 'Lap ')
    txt2 = txt2.replace('鲁', '魯')
    txt2 = txt2.replace('鷄', '雞')
    txt2 = txt2.replace('鹷', '齡')
    txt2 = txt2.replace('麪', '麵')
    txt2 = txt2.replace('麫', '麵')
    txt2 = txt2.replace('麽', '麼')
    txt2 = txt2.replace('黒', '黑')
    txt2 = txt2.replace('스', 'x')
    txt2 = txt2.replace('트', '')
    txt2 = txt2.replace('풀', '阿門')
    txt2 = txt2.replace('﹑', '、')
    txt2 = txt2.replace('﹟', '\#')
    txt2 = txt2.replace('﹣', '-')
    txt2 = txt2.replace('＂', '"')
    txt2 = txt2.replace('０', '0')
    txt2 = txt2.replace('１', '1')
    txt2 = txt2.replace('２', '2')
    txt2 = txt2.replace('３', '3')
    txt2 = txt2.replace('４', '4')
    txt2 = txt2.replace('５', '5')
    txt2 = txt2.replace('６', '6')
    txt2 = txt2.replace('７', '7')
    txt2 = txt2.replace('８', '8')
    txt2 = txt2.replace('９', '9')
    txt2 = txt2.replace('～', '-')
    txt2 = txt2.replace('｢', '「')
    txt2 = txt2.replace('｣', '」')
    txt2 = txt2.strip()
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
sermon_tex_filepath = '../../build/DSCCC/sermon_DSCCC_2009-present.tex'
# --------------------------------------
# print the latex document : prefix
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: printing out prefixing")
_ = os.system(f"cat ../prefix.tex | sed 's/粵語講道逐字稿/香港中文大學崇基神學院~~校牧主日崇拜講章~~2009-present/' | sed 's/Youtube Channel:/Chaplaincy, Divinity School of Chung Chi College, CUHK/' > " + sermon_tex_filepath)

# --------------------------------------
# index table
# --------------------------------------
progressStepCnt += 1
print(f"Step {progressStepCnt}: writing TOC")

# year integer for comparison
y_prev = -1
y_curr = -1
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
    fp.write("日期 & 講員 & 經課 & 講題 \\\\ \\hline \\hline\n")
    for index, row in df.iterrows():
        dt = row['date']
        y_curr = int(dt / 10000) # obtain current sermon's year integer
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
        # if year is progressed, add a hline
        if y_prev != y_curr:
            toc_tex_str += "\\hline "
            y_prev = y_curr
        # if year-month is progressed, add a hline
        if ym_prev != ym_curr:
            toc_tex_str += "\\hline\n"
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
                        ch_desired = cn2 #c2ch_dict.get(c)
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








