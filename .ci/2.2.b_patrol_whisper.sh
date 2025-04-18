#!/bin/bash
set +x

source COMMON_RC

# ------------------------------------------------------
# execute whisper speech-to-text for each project
# START WHILE
while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
do
  if test $PROJECT_NAME = DSCCC || test $PROJECT_NAME = HKBC
  then
      continue
  fi
  pushd $WHISPER_PATH/$PROJECT_NAME
  bash i
  popd # back to ./app/.ci
  sleep 10
done < $CI_PATH/PROJECT_LIST
# END WHILE
# ------------------------------------------------------
