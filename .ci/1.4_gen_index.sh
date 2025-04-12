#!/bin/bash
set +x

source COMMON_RC

pushd $PROJECT_PATH
  # ------------------------------------------------------
  # generate index for each project
  # START WHILE
  while IFS="" read -r PROJECT_NAME || [ -n "$PROJECT_NAME" ]
  do
    pushd ./$PROJECT_NAME
      python3    ../func_ipynb_2_py.py    generate_index.ipynb
      python3    generate_index.py
    popd # back to $PROJECT_PATH
  done < $CI_PATH/PROJECT_LIST
  # END WHILE
popd # back to $CI_PATH
