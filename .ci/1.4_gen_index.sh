#!/bin/bash
set +x
pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST FVC JNG WWBS
  do
    pushd ./$PROJECT_NAME
      python3 generate_index.py
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
