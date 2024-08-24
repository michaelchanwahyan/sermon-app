#!/usr/local/bin/python3

with open("results1.txt", "r") as fp1:
    lines1 = [ _.strip() for _ in fp1.readlines() ]
fp1.close()

with open("results2.txt", "r") as fp2:
    lines2 = [ _.strip() for _ in fp2.readlines() ]
fp2.close()

l1_list = []
for l1 in lines1:
    l1_list.append(l1.split(":")[0])
l1_list = sorted(list(set(l1_list)))

l2_list = []
for l2 in lines2:
    l2_list.append(l2.split(":")[0])
l2_list = sorted(list(set(l2_list)))

# print(l1_list)
# print(l2_list)
l_comm = [ (l1, l2) for l1 in l1_list for l2 in l2_list ]
# print(l_comm)
for l_pair in l_comm:
    if l_pair[0] == l_pair[1]:
        print(l_pair[0])
