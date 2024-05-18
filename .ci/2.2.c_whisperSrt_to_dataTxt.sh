#!/bin/bash
set +x
pushd ../whisper
  echo convert each project / srt source to data / project / txt
  # even there are data / project / txt files that were converted in the past
  # there is no harm to re-perform such action, as long as it does not
  # bring out data / project / txt file change
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG KFC PORCH STBC VINE WWBS YFCX YOS
  do
    python3    convert_srt2txt.py    $PROJECT_NAME
  done
popd # back to ./app/.ci
