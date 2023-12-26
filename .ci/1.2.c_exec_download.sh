#!/bin/bash
set +x
pushd ../projects
  for PROJECT_NAME in ACSMHK CBI CGST FVC JNG WWBS YFCX
  do
    pushd ./$PROJECT_NAME
      echo download new youtube sermon if any ...     $PROJECT_NAME
      bash download.sh
    popd # back to ./app/projects
  done
popd # back to ./app/.ci
