#!/bin/bash
set +x

source COMMON_RC

TIME_FS_FILENAME=sermon_fs_date_record.txt
TIME_FS_FILENAME_BAK=sermon_fs_date_record.txt.bak

pushd $PROJECT_PATH
  echo update audio fs date info to sermon_fs_date_record
  # ------------------------------------------------------
  # generate sermon audio filesystem date
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    if test $PROJECT_NAME = DSCCC || test $PROJECT_NAME = HKBC
    then
        continue
    fi
    pushd ./$PROJECT_NAME
      #INFO=$(ls -logtD '%Y-%m-%d' *.mp3)
      INFO=$(ls -logtD '%Y-%m-%d' *.mp3 | awk '{print $4'' ''$NF}' | sed 's/\[/ /' | sed 's/].mp3//')
      echo "$INFO" >> $PROJECT_PATH/$TIME_FS_FILENAME
    popd # back to $PROJECT_PATH
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
  # ------------------------------------------------------
  mv    $TIME_FS_FILENAME    $TIME_FS_FILENAME_BAK
  cat   $TIME_FS_FILENAME_BAK    |    sort -u    |    sed '/^$/d'    >    $TIME_FS_FILENAME
  rm -f $TIME_FS_FILENAME_BAK
popd # back to $CI_PATH
