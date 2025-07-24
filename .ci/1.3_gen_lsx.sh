#!/bin/bash
set +x

source COMMON_RC

pushd $PROJECT_PATH
  echo create ls.txt or lslogt.txt for each project
  # ------------------------------------------------------
  # generate ls info for each project
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    if test $PROJECT_NAME = DSCCC || test $PROJECT_NAME = HKBC
    then
        continue
    fi
    pushd ./$PROJECT_NAME
      ORI_DIR=$(pwd)
      pushd $HOME/TPPHC/SERMON/$PROJECT_NAME
      # # projects that require lslogt.txt
      # if \
      #
      # then
      #   ls -logtD '%b %d  %Y' *.mp3 | awk '{print substr($0,index($0,$4))}' > $ORI_DIR/lslogt.txt
      # fi
      # projects that require ls.txt
        ls *.mp3 > $ORI_DIR/ls.txt
      popd # back to $PROJECT_PATH/$PROJECT_NAME
    popd # back to $PROJECT_PATH
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
  # ------------------------------------------------------
popd # back to $CI_PATH
