#!/bin/bash
set -x
MP3_SRC_PATH=$HOME/TPPHC/SERMON
echo $MP3_SRC_PATH
ls -1 $MP3_SRC_PATH
for PROJECT_NAME in $(ls -1 $MP3_SRC_PATH)
do
  DESTINATE_TMP_FOLDER=../whisper/$PROJECT_NAME
  NEW_SRC_LIST_FILENAME=new_src_list.txt
  rm -f $DESTINATE_TMP_FOLDER/$NEW_SRC_LIST_FILENAME
  ls $MP3_SRC_PATH/$PROJECT_NAME > $DESTINATE_TMP_FOLDER/$NEW_SRC_LIST_FILENAME
  pushd $DESTINATE_TMP_FOLDER
    LANG=zh
    if [ "$PROJECT_NAME" == "PORCH" ] ; then
      LANG=en
    fi
    echo $LANG
    python3  ../generate_whisper_operation.py  $PROJECT_NAME  $LANG  $NEW_SRC_LIST_FILENAME
    rm -f $NEW_SRC_LIST_FILENAME
  popd # back to ./app/.ci
done

