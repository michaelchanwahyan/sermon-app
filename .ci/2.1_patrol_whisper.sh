#!/bin/bash
set +x
for PROJECT_NAME in ACSMHK CBI CGST FVC JNG WWBS YFCX
do
  pushd ../whisper/$PROJECT_NAME
  bash i
  popd # back to ./app/.ci
  sleep 240
done