#!/bin/python3
import os
import time
from datetime import datetime
foldername = "JNG"
mp3filelist = os.listdir(f"/Users/pikachu/Library/CloudStorage/OneDrive-TheChineseUniversityofHongKong/TPPHC/SERMON/{foldername}/")
codes = list(set([ mp3file[-15:-4] for mp3file in mp3filelist ]))
codes = [ code for code in codes \
        if not os.path.isfile(f"/Users/pikachu/SOURCE/sermon-app/data/{foldername}/{code}.txt") ]
print(f"total no. of codes: {len(codes)}")
for code in codes:
    cmdstr = f"ffmpeg -i /Users/pikachu/Library/CloudStorage/OneDrive-TheChineseUniversityofHongKong/TPPHC/SERMON/{foldername}/*{code}.mp3 /Users/pikachu/SOURCE/sermon-app/projects/{code}.wav"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    # SEE HERE
    # CODE.SSTREADY is a signal for container to perform generate_content
    # END OF SEE HERE
    cmdstr = f"touch ~/SOURCE/sermon-app/projects/{code}.sttready"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    # SEE HERE
    # CODE.CONCATREADY is a signal for host to perform concat
    # END OF SEE HERE
    while not os.path.isfile(f"/Users/pikachu/SOURCE/sermon-app/projects/{code}.concatready"):
        print(datetime.now(), f"{code}.concatready not yet exists")
        time.sleep(60)
    print(datetime.now(), "generate concat shell script !")
    with open(f"concat_{code}.sh", "w") as fp:
        fp.write("#!/bin/bash\n")
        cmdstr = f"python3 concat_{code}.py > ../data/{foldername}/{code}.txt\n"
        fp.write(cmdstr)
    fp.close()
    cmdstr = f"/bin/bash concat_{code}.sh"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    print(f"{code} done !")
    time.sleep(3)
    cmdstr = f"rm -f -- {code}.wav"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    cmdstr = f"rm -f -- {code}.sttready"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    cmdstr = f"rm -f -- {code}.concatready"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    cmdstr = f"rm -f concat_{code}.py"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    cmdstr = f"rm -f concat_{code}.sh"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    cmdstr = f"rm -f -- {code}/{code}_*.wav"
    print(datetime.now(), cmdstr)
    _ = os.system(cmdstr)
    if os.path.exists("break_host"):
        _ = os.system("rm -f break_host")
        break
