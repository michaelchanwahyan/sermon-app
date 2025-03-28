#!/bin/bash
set +x
pushd ../projects
  echo create ls.txt or lslogt.txt for each project
  # projects that require lslogt.txt
  for PROJECT_NAME in ACSMHK CBI CGST FVC JNG PORCH STBC WWBS YOS
  do
    pushd ./$PROJECT_NAME
      ORI_DIR=$(pwd)
      pushd ~/TPPHC/SERMON/$PROJECT_NAME
        ls -logtD '%b %d  %Y' *.mp3 | awk '{print substr($0,index($0,$4))}' > $ORI_DIR/lslogt.txt
      popd # back to ./app/projects/$PROJECT_NAME
    popd # back to ./app/projects
  done
  # projects that require ls.txt
  for PROJECT_NAME in FLWC GFC KFC VINE YFCX
  do
    pushd ./$PROJECT_NAME
      ORI_DIR=$(pwd)
      pushd ~/TPPHC/SERMON/$PROJECT_NAME
        ls *.mp3 > $ORI_DIR/ls.txt
      popd # back to ./app/projects/$PROJECT_NAME
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
