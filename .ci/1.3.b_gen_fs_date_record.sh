#!/bin/bash
set +x
TIME_FS_FILENAME=sermon_fs_date_record.txt
pushd ../projects
  echo update audio fs date info to sermon_fs_date_record
  rm -f tmp_sermon_fs_date_record
  # projects that require lslogt.txt
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG KFC PORCH STBC VINE WWBS YFCX YOS
  do
    pushd ./$PROJECT_NAME
      #INFO=$(ls -logtD '%Y-%m-%d' *.mp3)
      INFO=$(ls -logtD '%Y-%m-%d' *.mp3 | awk '{print $4'' ''$NF}' | sed 's/\[/ /' | sed 's/].mp3//')
      echo "$INFO" >> ../$TIME_FS_FILENAME
    popd # back to ./app/projects
  done
  mv $TIME_FS_FILENAME $TIME_FSS_FILENAME.bak
  cat $TIME_FS_FILENAME.bak | sort -u | sed '/^$/d' > $TIME_FS_FILENAME
  rm -f $TIME_FS_FILENAME.bak
popd # back to ./app/.ci
