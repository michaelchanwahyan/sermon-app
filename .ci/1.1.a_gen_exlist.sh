#!/bin/bash
set +x
pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST FVC JNG WWBS YFCX
  do
    pushd ./$PROJECT_NAME
      echo list out audio source directory of project $PROJECT_NAME
      pushd /Users/pikachu/One*/TPPHC/SERMON/$PROJECT_NAME
        ls | grep .mp3 > /Users/pikachu/SOURCE/sermon-app/projects/$PROJECT_NAME/exlist.txt
      popd # back to ./app/projects/$PROJECT_NAME
      echo youtube hashcode retrieval for project $PROJECT_NAME
      python3    ../../.ci/1.1.b_youtube_hashcode_retrieval.py
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
