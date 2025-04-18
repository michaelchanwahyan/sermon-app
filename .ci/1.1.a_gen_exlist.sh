#!/bin/bash
set +x

source COMMON_RC

pushd $PROJECT_PATH
  # ------------------------------------------------------
  # generate exlist for each project
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    echo $PROJECT_NAME
    pushd ./$PROJECT_NAME
      AUDIO_SRC_PATH=$HOME/TPPHC/SERMON/$PROJECT_NAME
      mkdir -p $AUDIO_SRC_PATH # this is to protect if no audio folder exist during new projection
      echo list out audio source directory of project $PROJECT_NAME
      pushd $AUDIO_SRC_PATH
        ls | grep .mp3 > $CI_PATH/../projects/$PROJECT_NAME/exlist.txt
      popd # back to $PROJECT_PATH/$PROJECT_NAME
      ls | grep .mp3 >> exlist.txt
      echo youtube hashcode retrieval for project $PROJECT_NAME
      python3    $CI_PATH/1.1.b_youtube_hashcode_retrieval.py
    popd # back to $PROJECT_PATH
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
  # ------------------------------------------------------
popd # back to $CI_PATH
