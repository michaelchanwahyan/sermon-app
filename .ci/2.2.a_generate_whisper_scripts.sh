#!/bin/bash
set -x

source COMMON_RC

echo $MP3_SRC_PATH
ls -1 $MP3_SRC_PATH
# the reason for using    MP3_SRC_PATH    instead of    PROJECT_LIST
# is that MP3_SRC_PATH contains folder where sermon sources are audio
# while PROJECT_LIST contains other sermons that are from textual source
for PROJECT_NAME in $(ls -1 $MP3_SRC_PATH)
do
  DESTINATE_TMP_FOLDER=$WHISPER_PATH/$PROJECT_NAME
  NEW_SRC_LIST_FILENAME=new_src_list.txt
  rm -f $DESTINATE_TMP_FOLDER/$NEW_SRC_LIST_FILENAME
  ls $MP3_SRC_PATH/$PROJECT_NAME > $DESTINATE_TMP_FOLDER/$NEW_SRC_LIST_FILENAME
  pushd $DESTINATE_TMP_FOLDER
    rm -f i i1 i2 i3 i4 j j1 j2 j3 j4 ij ijk
    LANG=zh
    if [ "$PROJECT_NAME" == "PORCH" ] ; then
      LANG=en
    fi
    if [ "$PROJECT_NAME" == "VINE" ] ; then
      LANG=en
    fi
    echo $LANG
    pushd $WHISPER_PATH
      python3  generate_whisper_operation.py  $PROJECT_NAME  $LANG  $DESTINATE_TMP_FOLDER/$NEW_SRC_LIST_FILENAME
    popd
    rm -f $NEW_SRC_LIST_FILENAME
  popd # back to $CI_PATH
done
find $WHISPER_PATH -name "stop.txt" -exec rm -f {} \;

