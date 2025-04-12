#!/bin/bash
set +x

source COMMON_RC

pushd $PROJECT_PATH
  # ------------------------------------------------------
  # execute download sermon audio for each project
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    if test $PROJECT_NAME = DSCCC || test $PROJECT_NAME = HKBC
    then
        continue
    fi
    pushd ./$PROJECT_NAME
      echo download new youtube sermon if any ...     $PROJECT_NAME
      bash download.sh
    popd # back to ./app/projects
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
  # ------------------------------------------------------
popd # back to $CI_PATH
./1.2.d_gen_fs_date_record.sh
