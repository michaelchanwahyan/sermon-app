#!/bin/bash
set +x
if   [ "$1" == "" ] ; then
    echo
    echo generate sermon tex source: ALL
    echo
    echo TeX source generation takes roughly 15 minutes ...
    echo
    sleep 10

    pushd ../projects
      TEX_SRC_PROJ_NAME_ARR=()
      TEX_LINE_NUM_PREV_ARR=()
      TEX_LINE_NUM_CURR_ARR=()
      for PROJECT_NAME in ACSMHK CBI CGST DSCCC FLWC FVC GFC HKBC JNG KFC PORCH STBC VINE WWBS YFCX YOS
      do
        TEX_SRC_PROJ_NAME_ARR+=($PROJECT_NAME)
        TEX_LINE_NUM_PREV=$(wc -l ../build/$PROJECT_NAME/sermon_*.tex | tail -1 | awk '{print $1}')
        TEX_LINE_NUM_PREV_ARR+=($TEX_LINE_NUM_PREV)
        pushd ./$PROJECT_NAME
          python3    ../func_ipynb_2_py.py    generate_sermonbook.ipynb
          python3    generate_sermonbook.py
        popd # back to ./app/projects
        TEX_LINE_NUM_CURR=$(wc -l ../build/$PROJECT_NAME/sermon_*.tex | tail -1 | awk '{print $1}')
        TEX_LINE_NUM_CURR_ARR+=($TEX_LINE_NUM_CURR)
      done
    popd # back to ./app/.ci

    echo
    echo '-------------------------------------'
    echo 'LaTeX source file changes:'
    echo '-------------------------------------'
    echo
    for projIdx in "${!TEX_SRC_PROJ_NAME_ARR[@]}"    # ! : to loop through the array index
                                                     # # : to loop through the array value
                                                     # @ : the indices
    do
        echo project $projIdx : ${TEX_SRC_PROJ_NAME_ARR[$projIdx]}
        LN_b4=${TEX_LINE_NUM_PREV_ARR[$projIdx]}
        LN_af=${TEX_LINE_NUM_CURR_ARR[$projIdx]}
        echo tex src line num change: $(expr $LN_af - $LN_b4) lines more "( $LN_b4 '->' $LN_af )"
    done
else
    PROJECT_NAME=$1
    echo
    echo generate sermon tex source: $PROJECT_NAME
    echo
    sleep 10

    pushd ../projects
      TEX_LINE_NUM_PREV=$(wc -l ../build/$PROJECT_NAME/sermon_*.tex | tail -1 | awk '{print $1}')
      pushd ./$PROJECT_NAME
        python3    ../func_ipynb_2_py.py    generate_sermonbook.ipynb
        python3    generate_sermonbook.py
      popd # back to ./app/projects
      TEX_LINE_NUM_CURR=$(wc -l ../build/$PROJECT_NAME/sermon_*.tex | tail -1 | awk '{print $1}')
    popd # back to ./app/.ci

    echo
    echo '-------------------------------------'
    echo 'LaTeX source file changes:'
    echo '-------------------------------------'
    echo
    echo project $PROJECT_NAME
    LN_b4=$TEX_LINE_NUM_PREV
    LN_af=$TEX_LINE_NUM_CURR
    echo tex src line num change: $(expr $LN_af - $LN_b4) lines more "( $LN_b4 '->' $LN_af )"
fi

