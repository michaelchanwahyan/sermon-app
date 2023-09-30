#!/bin/bash
cd ~/SOURCE/sermon-app/whisper
find . -name ".DS_Store" -exec rm -rf {} \;
# =========================================================
# merge the updates from sermon-srt_whisper branch
# =========================================================
git merge sermon-srt_whisper --no-commit --no-ff

# =========================================================
# undo the 'git-add' operations from merge process
# =========================================================
git reset ./JNG/*.srt
git reset ./JNG/*.whisper.log
#git reset ../srt
#rm -rf ../srt

# =========================================================
# conversion from whisper srt file into ../data/JNG txt
# =========================================================
python3 ./convert_srt2txt.py

# =========================================================
# remove the merged .srt and .whisper.log files
# =========================================================
rm -f ./JNG/*.srt
rm -f ./JNG/*.whisper.log

