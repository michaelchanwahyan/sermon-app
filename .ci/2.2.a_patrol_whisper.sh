#!/bin/bash
set +x
for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG PORCH WWBS YFCX YOS
do
  pushd ../whisper/$PROJECT_NAME
  bash i
  popd # back to ./app/.ci
  sleep 240
done
