#!/usr/bin/python3
import os
import time
from datetime import datetime
foldername = "JNG"
no_code_cnt = 0
while True:
    codes = [ filename[:-4] for filename in os.listdir("./") if filename[-4:]==".wav" ]
    print(datetime.now(), codes)
    if not len(codes):
        no_code_cnt += 1
        if no_code_cnt > 20:
            print(datetime.now(), cmdstr)
            break
    for code in codes:
        if os.path.isfile(f"./{code}.sttready") \
            and not os.path.isfile(f"./{code}.concatready") \
            and not os.path.isfile(f"../data/{foldername}/{code}.txt"):
            cmdstr = f"python3 -- generate_content.py {code}"
            print(datetime.now(), cmdstr)
            _ = os.system(cmdstr)
            time.sleep(10)
            cmdstr = f"touch ./{code}.concatready"
            print(datetime.now(), cmdstr)
            _ = os.system(cmdstr)
    time.sleep(60)
    if os.path.exists("break_container"):
        _ = os.system("rm -f break_container")
        break
