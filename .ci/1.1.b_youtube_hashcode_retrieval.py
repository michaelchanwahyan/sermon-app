#!/usr/bin/python3
with open('exlist.txt', 'r') as fp:
    ex_list = [_.strip() for _ in fp.readlines()]
ex_list_2 = []
for ex in ex_list:
    ex = ex[-16:-5] if ex[-5] == ']' else ex[-15:-4]
    ex_list_2.append(ex)
with open('exlist.txt', 'w') as fp:
    for ex in ex_list_2:
        fp.write(ex)
        fp.write('\n')

