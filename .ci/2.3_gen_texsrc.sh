#!/bin/bash
set +x
echo
echo TeX source generation takes roughly 15 minutes ...
echo
sleep 10

pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST DSCCC FLWC FVC GFC HKBC JNG KFC PORCH STBC VINE WWBS YFCX YOS
  do
    pushd ./$PROJECT_NAME
      python3    ../func_ipynb_2_py.py    generate_sermonbook.ipynb
      python3    generate_sermonbook.py
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
