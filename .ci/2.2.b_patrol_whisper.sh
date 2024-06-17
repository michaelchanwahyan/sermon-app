#!/bin/bash
set +x
for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG KFC PORCH STBC VINE WWBS YFCX YOS
do
  pushd ../whisper/$PROJECT_NAME
  bash i
  popd # back to ./app/.ci
  sleep 10
done
