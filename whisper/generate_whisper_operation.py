#!/usr/bin/python3


import sys
import re


if len(sys.argv) > 1:
    PROJECT_NAME = sys.argv[1]
else:
    print("PROJECT_NAME is not provided !")
    print("EXIT !")
    exit()

if len(sys.argv) > 2:
    LANG = sys.argv[2]
else:
    print("LANG is not provided !")
    print("EXIT !")
    exit()

if len(sys.argv) > 3:
    NEW_SRC_LIST = sys.argv[3]
else:
    print("NEW_SRC_LIST is not provided !")
    print("EXIT !")
    exit()


w_text = ""

w_text += "#!/bin/bash"
w_text += "\n"

w_text += "PROJ_NAME=%s    ;" % PROJECT_NAME
w_text += " LANG=%s    ;" % LANG
w_text += " source ~/SOURCE/sermon-app/.venv/bin/activate"
w_text += "\n"

w_text += "#if [ -f stop.txt ] ; then exit ; fi ;"
w_text += " FN=...........; THREAD_NUM=$(cat threadnum.txt) ;"
w_text += " yes | ffmpeg -i ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3 -ar 16000 -ac 1 -c:a pcm_s16le ./$FN.wav ;"
w_text += " ~/SOURCE/whisper.cpp/main --model ~/SOURCE/whisper.cpp/models/ggml-large.bin"
w_text += " --output-srt --language $LANG --threads $THREAD_NUM --processors 1"
w_text += " --file ./$FN.wav > ./$FN.whisper.log ;"
w_text += " mv ./$FN.wav.srt ./$FN.srt ; rm -f ./$FN.wav ;"
w_text += " rm -f ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3"
w_text += "\n"


with open(NEW_SRC_LIST, 'r') as fp:
    lines = [ _.strip() for _ in fp.readlines() ]
fp.close()

if len(lines) == 0:
    print("Project %s has empty NEW_SRC_LIST !!!" % PROJECT_NAME)
    print("Clean up content , preserve only default content !!!")
    with open('i', 'w') as fp:
        fp.write(w_text)
    fp.close()
    print("EXIT !")
    exit()

for ytcode, line in zip([ line[-16:-5] for line in lines ], lines):
    if len(ytcode) == 11:
        w_text += " if [ -f stop.txt ] ; then exit ; fi ;"
        w_text += " FN=%s; THREAD_NUM=$(cat threadnum.txt) ;" % ytcode
        w_text += " yes | ffmpeg -i ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3 -ar 16000 -ac 1 -c:a pcm_s16le ./$FN.wav ;"
        w_text += " ~/SOURCE/whisper.cpp/main --model ~/SOURCE/whisper.cpp/models/ggml-large.bin"
        w_text += " --output-srt --threads $THREAD_NUM --processors 1"
        if len(re.findall(r'[A-Za-z]', line)): # in case file name contains a lot of Eng char
            w_text += " --language en"
        else:
            w_text += " --language $LANG"
        w_text += " --file ./$FN.wav > ./$FN.whisper.log ;"
        w_text += " mv ./$FN.wav.srt ./$FN.srt ; rm -f ./$FN.wav ;"
        w_text += " rm -f ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3"
        w_text += "\n"


with open('i', 'w') as fp:
    fp.write(w_text)
fp.close()

