#!/bin/bash
set +x
pushd ../projects
  echo wget youtube videos / streams files to each project
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC GFC JNG KFC PORCH STBC VINE WWBS YFCX YOS
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
          rm -f cbi.videos
          wget -O cbi.videos https://www.youtube.com/@CBI_HK/videos
          rm -f cbi.streams
          wget -O cbi.streams https://www.youtube.com/@CBI_HK/streams
          cat cbi.videos cbi.streams > videos
          rm -f cbi.*
      fi
      if test $PROJECT_NAME = CGST
      then
          rm -f cgst.videos
          wget -O cgst.videos https://www.youtube.com/@cgstedu/videos
          rm -f cgst.streams
          wget -O cgst.streams https://www.youtube.com/@cgstedu/streams
          cat cgst.videos cgst.streams > videos
          rm -f cgst.*
      fi
      if test $PROJECT_NAME = FLWC
      then
          rm -f flwc.videos
          wget -O flwc.videos https://www.youtube.com/@flowchurchhk/videos
          rm -f flwc.streams
          wget -O flwc.streams https://www.youtube.com/@flowchurchhk/streams
          cat flwc.videos flwc.streams > videos
          rm -f flwc.*
      fi
      if test $PROJECT_NAME = FVC
      then
          wget https://www.youtube.com/@fairviewchurch/videos
      fi
      if test $PROJECT_NAME = GFC
      then
          wget https://www.youtube.com/@graceflowchurch6874/videos
      fi
      if test $PROJECT_NAME = JNG
      then
          wget https://www.youtube.com/Johnson_Ng/videos
      fi
      if test $PROJECT_NAME = KFC
      then
          rm -f kfc.discipleship
          wget -O kfc.discipleship    https://www.youtube.com/playlist?list=PLMn1FowxfKJef1i_XtERUXp9nORakIb2-
          rm -f kfc.youth
          wget -O kfc.youth           https://www.youtube.com/playlist?list=PLMn1FowxfKJdv90VS5x2WPkFSluO0M5zk
          rm -f kfc.mandarin
          wget -O kfc.mandarin        https://www.youtube.com/playlist?list=PLMn1FowxfKJeJsIgrm8FiD6nKK8H9pd7x
          rm -f kfc.english
          wget -O kfc.english         https://www.youtube.com/playlist?list=PLMn1FowxfKJfJWaNUNgz8eiO8a1RpJlzI
          cat kfc.discipleship  kfc.youth  kfc.mandarin  kfc.english > videos
          rm -f kfc.*
      fi
      if test $PROJECT_NAME = PORCH
      then
          wget https://www.youtube.com/@ThePorch/videos
      fi
      if test $PROJECT_NAME = STBC
      then
          rm -f stbc.streams
          wget -O stbc.streams https://www.youtube.com/@stbc1977/streams
          rm -f stbc.videos
          wget -O stbc.videos https://www.youtube.com/@stbc1977/videos
          cat stbc.streams stbc.videos > videos
          rm -f stbc.*
      fi
      if test $PROJECT_NAME = VINE
      then
          rm -f vinehk.videos
          wget -O vinehk.videos https://www.youtube.com/@thevinehk/videos
          rm -f vinehk.streams
          wget -O vinehk.streams https://www.youtube.com/@thevinehk/streams
          rm -f vineyl.videos
          wget -O vineyl.videos https://www.youtube.com/@thevine_yl/videos
          rm -f vineyl.streams
          wget -O vineyl.streams https://www.youtube.com/@thevine_yl/streams
          cat vinehk.videos vinehk.streams vineyl.videos vineyl.streams > videos
          rm -f vine*.*
      fi
      if test $PROJECT_NAME = WWBS
      then
          wget https://youtube.com/@WorldwideBibleSociety/videos
      fi
      if test $PROJECT_NAME = YFCX
      then
          rm -f yfcy.streams
          wget -O yfcy.streams https://www.youtube.com/YanfookYouth/streams
          rm -f yfc.streams
          wget -O yfc.streams https://www.youtube.com/yanfookchurch/streams
          cat yfcy.streams yfc.streams > videos
          rm -f yfc*.*
      fi
      if test $PROJECT_NAME = YOS
      then
          wget -O videos https://www.youtube.com/@yauoischool/streams
      fi
    popd # back to ./app/projects
  done
  echo make union on rejection_list
  find . -name "rejection_list.txt" -exec cat {} \; > rejection_list_all.txt
  for PROJECT_NAME in ACSMHK CBI CGST FLWC FVC GFC JNG KFC PORCH STBC VINE WWBS YFCX YOS
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
