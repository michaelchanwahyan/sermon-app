#!/bin/bash
set +x
pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC GFC JNG KFC PORCH STBC VINE WWBS YFCX YOS
  do
    pushd ./$PROJECT_NAME
      echo download new youtube sermon if any ...     $PROJECT_NAME
      bash download.sh
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
./1.2.d_gen_fs_date_record.sh
