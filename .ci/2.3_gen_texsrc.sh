#!/bin/bash
set +x
pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST DSCCC FVC HKBC JNG WWBS YFCX
  do
    pushd ./$PROJECT_NAME
      python3    generate_sermonbook.py
    popd # back to ./app/projects
  done
popd # back to ./app/.ci