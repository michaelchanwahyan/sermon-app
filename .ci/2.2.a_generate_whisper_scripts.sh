#!/bin/bash
set -x

source COMMON_RC

echo $MP3_SRC_PATH
ls -1 $MP3_SRC_PATH
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
    python3  $WHISPER_PATH/generate_whisper_operation.py  $PROJECT_NAME  $LANG  $NEW_SRC_LIST_FILENAME
    rm -f $NEW_SRC_LIST_FILENAME
  popd # back to $CI_PATH
done
find $WHISPER_PATH -name "stop.txt" -exec rm -f {} \;

