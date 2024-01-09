#!/bin/bash
set +x
for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG WWBS YFCX
do
  pushd ../projects/$PROJECT_NAME
    # -----------------------------------------------------
    #     list out existing audio mp3 files
    # -----------------------------------------------------
    pushd ~/TPPHC/SERMON/$PROJECT_NAME
      ls > mp3list.txt
    popd # back to ./projects/$PROJECT_NAME
    MP3_AUDIO_PATH=~/TPPHC/SERMON/$PROJECT_NAME
    mv $MP3_AUDIO_PATH/mp3list.txt ./
    # -----------------------------------------------------
    #     loop through existing audio files,
    #     check if exists its data/txt and whisper/srt
    # -----------------------------------------------------
    while read YTCODE; do
      echo "$PROJECT_NAME    $YTCODE"
      DATA_TXT_PATHFILENAME=../data/$PROJECT_NAME/$YTCODE.txt
      WHISPER_SRT_PATHFILENAME=../whisper/$PROJECT_NAME/$YTCODE.srt
      # -----------------------------------------------------
      #     if data/txt and whisper/srt unfound,
      #     scp audio to transcription server
      # -----------------------------------------------------
      if [ ! -f $DATA_TXT_PATHFILENAME ] -a [ ! -f $WHISPER_SRT_PATHFILENAME ]; then
        scp  $MP3_AUDIO_PATH/*$YTCODE*.mp3  $(cat transcription_server_ip.txt):$MP3_AUDIO_PATH/
      fi
    done <mp3list.txt
    rm -f mp3list.txt
  popd # back to ./app/.ci
  sleep 10
done
