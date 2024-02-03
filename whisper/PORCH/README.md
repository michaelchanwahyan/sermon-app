this is the directory path of whisper for PORCH project

reference whisper cpp execution be like
```bash
#!/bin/bash
PROJ_NAME=PORCH    ; LANG=en    ; source ~/SOURCE/sermon-app/.venv/bin/activate
#if [ -f stop.txt ] ; then exit ; fi ; FN=...........; THREAD_NUM=$(cat threadnum.txt) ; yes | ffmpeg -i ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3 -ar 16000 -ac 1 -c:a pcm_s16le ./$FN.wav ; ~/SOURCE/whisper.cpp/main --model ~/SOURCE/whisper.cpp/models/ggml-large.bin --output-srt --language $LANG --threads $THREAD_NUM --processors 1 --file ./$FN.wav > ./$FN.whisper.log ; mv ./$FN.wav.srt ./$FN.srt ; rm -f ./$FN.wav ; rm -f ~/TPPHC/SERMON/$PROJ_NAME/*$FN*.mp3
```
where ```...........``` shall be replaced by the corresponding youtube hash code

