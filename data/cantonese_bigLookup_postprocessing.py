#!/bin/python3
import os

filename = 'gb2ROs2pM84.txt'
with open(filename, 'r') as fp:
    lines = fp.readlines()
fp.close()

#mapping table
mt = {
    '誒，': '，',
    '誒': '，',
    '咧，': '，',
    '咧': '',
    '嗱，': '，',
    '好壞處一個': '好懷住一個',
    '方溫仔': 'form one 仔',
    '爆會員': '鮑會園',
    '八會員': '鮑會園',
    '羅馬輸': '羅馬書',
    '有少少嘅氣息': '有少少嘅喜色',
    '還皮': '頑皮',
    '出外及技': '出埃及記',
    '感其實': '咁其實',
    '暗春': '鵪鶉',
    '縣民': '原文',
    '雷軍': '雷轟',
    '西大山': '西乃山',
    '道理嗰排': '到你嗰排',
    '渡輪': '導論',
    '英話': '應允',
    '一雪': '一說',
    '雪咗': '說咗',
    '最以色列': '對以色列',
}
mt_keys = list(mt.keys())

for line in lines:
    line = line.strip()
    for key in mt_keys:
        if key in line:
            line = line.replace(key, mt.get(key))
    if line[0:1] in ['，', '？']:
        line = line[2:]
    if len(line) == 0:
        continue
    else:
        print(line)
