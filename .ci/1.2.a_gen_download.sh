#!/bin/bash
set +x
pushd ../projects
  echo wget youtube videos / streams files to each project
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG PORCH WWBS YFCX YOS
  do
    pushd ./$PROJECT_NAME
      if [ -f videos ]
      then
          rm -f videos
      fi
      if test $PROJECT_NAME = ACSMHK
      then
          wget https://www.youtube.com/@acsmhk/videos
      fi
      if test $PROJECT_NAME = CBI
      then
          wget -O v1 https://www.youtube.com/@CBI_HK/videos
          wget -O v2 https://www.youtube.com/@CBI_HK/streams
          cat v1 v2 > videos
          rm -f v1 v2
      fi
      if test $PROJECT_NAME = CGST
      then
          wget https://www.youtube.com/@cgstedu/videos
      fi
      if test $PROJECT_NAME = FLWC
      then
          wget https://www.youtube.com/@flowchurchhk/videos
      fi
      if test $PROJECT_NAME = FVC
      then
          wget https://www.youtube.com/@fairviewchurch/videos
      fi
      if test $PROJECT_NAME = JNG
      then
          wget https://www.youtube.com/Johnson_Ng/videos
      fi
      if test $PROJECT_NAME = PORCH
      then
          wget https://www.youtube.com/@ThePorch/videos
      fi
      if test $PROJECT_NAME = WWBS
      then
          wget https://youtube.com/@WorldwideBibleSociety/videos
      fi
      if test $PROJECT_NAME = YFCX
      then
          wget -O streams.yfcy https://www.youtube.com/YanfookYouth/streams
          wget -O streams.yfc https://www.youtube.com/yanfookchurch/streams
          cat streams.yfcy streams.yfc > videos
          rm -f streams.*
      fi
      if test $PROJECT_NAME = YOS
      then
          wget -O videos https://www.youtube.com/@yauoischool/streams
      fi
    popd # back to ./app/projects
  done
  echo make union on rejection_list
  find . -name "rejection_list.txt" -exec cat {} \; > rejection_list_all.txt
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC JNG PORCH WWBS YFCX YOS
  do
    pushd ./$PROJECT_NAME
      if [ -f download.sh ]
      then
          rm -f download.sh
      fi
      python3    ../../.ci/1.2.b_gen_download_from_vid_exl_rjl.py    \
          videos    \
          exlist.txt    \
          ../rejection_list_all.txt
    popd # back to ./app/projects
  done
  if [ -f rejection_list_all.txt ]
  then
      rm -f rejection_list_all.txt
  fi
popd # back to ./app/.ci
