#!/bin/bash
set +x

source COMMON_RC

pushd $WHISPER_PATH
  echo convert each project / srt source to data / project / txt
  # even there are data / project / txt files that were converted in the past
  # there is no harm to re-perform such action, as long as it does not
  # bring out data / project / txt file change
  # ------------------------------------------------------
  # execute srt-to-txt conversion for each project
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    if test $PROJECT_NAME = DSCCC || test $PROJECT_NAME = HKBC
    then
        continue
    fi
    python3    convert_srt2txt.py    $PROJECT_NAME
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
  # ------------------------------------------------------
popd # back to ./app/.ci
