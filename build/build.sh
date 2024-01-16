#!/bin/bash
echo build sermon project $1
if   [ "$1" == "" ] ; then
    echo "NAME                                                                "
    echo "     build.sh - build sermon LaTeX source,                          "
    echo "                or generate them from raw textual format files      "
    echo "                                                                    "
    echo "SYNOPSIS                                                            "
    echo "     build.sh    [action]    [optional argument]                    "
    echo "                                                                    "
    echo "DESCRIPTION                                                         "
    echo "     The build.sh majorly executes three categories of actions.     "
    echo "     1st: convert textual files from whisper <srt> typical <txt>.   "
    echo "     2nd: generate LaTeX source files from sermon txt source files. "
    echo "     3rd: compile LaTeX source files for each sermon project.       "
    echo "                                                                    "
    echo "     The actions are as follows:                                    "
    echo "                                                                    "
    echo "     genall   Perform srt-to-txt transformation, sourcing from srt  "
    echo "              files pathed under ./app/whisper/<PROJECT_NAME>.      "
    echo "              The output txt files are pathed under                 "
    echo "              ./app/data/<PROJECT_NAME>.                            "
    echo "              This action requires the system equipped with python3."
    echo "                                                                    "
    echo "     buildall Compile the LaTeX source files of all sermon projects."
    echo "              Available sermon projects include:                    "
    echo "               -  ACSMHK                                            "
    echo "               -  CBI                                               "
    echo "               -  CGST                                              "
    echo "               -  DSCCC                                             "
    echo "               -  FLWC                                              "
    echo "               -  FVC                                               "
    echo "               -  HKBC                                              "
    echo "               -  JNG                                               "
    echo "               -  WWBS                                              "
    echo "               -  YFCX                                              "
    echo "              A common practice on every LaTeX build action in this "
    echo "              script is that every time the tex file is to be       "
    echo "              compiled twice, in order to get LaTeX toc files to    "
    echo "              converge. An explicit option 'once' could be provided "
    echo "              if the second compilation is intended to be skipped.  "
    echo "                                                                    "
    echo "     ACSMHK   Compile ACSMHK sermon book.                           "
    echo "              ACSMHK := Alliance Communications Ministry            "
    echo "              宣道傳意及出版事工                                    "
    echo "                                                                    "
    echo "     CBI      Compile CBI sermon book.                              "
    echo "              CBI := Chinese Bible International                    "
    echo "              漢語聖經協會                                          "
    echo "                                                                    "
    echo "     CGST     Compile CGST sermon book.                             "
    echo "              CGST := China Graduate School of Theology             "
    echo "              中國神學研究院                                        "
    echo "                                                                    "
    echo "     DSCCC    Compile DSCCC sermon book.                            "
    echo "              DSCCC := Divinity School of Chung Chi College, CUHK   "
    echo "              香港中文大學崇基學院神學院                            "
    echo "                                                                    "
    echo "     FLWC     Compile FLWC sermon book.                             "
    echo "              FLWC := Flow Church                                   "
    echo "              流堂                                                  "
    echo "                                                                    "
    echo "     FVC      Compile FVC sermon book.                              "
    echo "              FVC := Fairview Church                                "
    echo "              宣道會錦繡堂                                          "
    echo "                                                                    "
    echo "     HKBC     Compile HKBC sermon book.                             "
    echo "              HKBC := Hong Kong Bible Conference                    "
    echo "              港九培靈研經會                                        "
    echo "                                                                    "
    echo "     JNG      Compile JNG sermon book.                              "
    echo "              JNG := Channel of Johnson Ng                          "
    echo "              Johnson Ng 我愛聽主道                                 "
    echo "                                                                    "
    echo "     WWBS     Compile WWBS sermon book.                             "
    echo "              WWBS := Worldwide Bible Society                       "
    echo "              環球聖經公會                                          "
    echo "                                                                    "
    echo "     YFCX     Compile YFCX sermon book.                             "
    echo "              YFCX := Yan Fook Church & Yan Fook Church Youth       "
    echo "              播道會恩福堂 & 播道會恩福堂青年團                     "
    echo "                                                                    "
    echo "     The optional arguments are as follows:                         "
    echo "                                                                    "
    echo "     once     The explicit option used in 'buildall' or any         "
    echo "              individual '<PROJECT_NAME>' so that the tex source    "
    echo "              compilation only executes once.                       "
    echo "              This option does not take effect with 'genall'        "
fi
if   [ "$1" == "genall" ] ; then
    cd ../whisper
    python3 convert_srt2txt.py ACSMHK
    python3 convert_srt2txt.py CBI
    python3 convert_srt2txt.py CGST
    python3 convert_srt2txt.py FLWC
    python3 convert_srt2txt.py FVC
    python3 convert_srt2txt.py JNG
    python3 convert_srt2txt.py WWBS
    python3 convert_srt2txt.py YFCX
    cd ../projects
    cd ./ACSMHK
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./CBI
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./CGST
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./DSCCC
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./FLWC
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./FVC
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./HKBC
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./JNG
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./WWBS
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ./YFCX
    python3 ../func_ipynb_2_py.py generate_sermonbook.ipynb
    python3 generate_sermonbook.py
    cd ..
    cd ../build
elif [ "$1" == "buildall" ] ; then
    if [ "$2" != "once" ] ; then
    ./build.sh ACSMHK
    ./build.sh CBI
    ./build.sh CGST
    ./build.sh DSCCC
    ./build.sh FLWC
    ./build.sh FVC
    ./build.sh HKBC
    ./build.sh JNG
    ./build.sh WWBS
    ./build.sh YFCX
    else
    ./build.sh ACSMHK  once
    ./build.sh CBI     once
    ./build.sh CGST    once
    ./build.sh DSCCC   once
    ./build.sh FLWC    once
    ./build.sh FVC     once
    ./build.sh HKBC    once
    ./build.sh JNG     once
    ./build.sh WWBS    once
    ./build.sh YFCX    once
    fi
elif [ "$1" == "ACSMHK" ] ; then
    cd $1
    xelatex sermon_$1.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1.tex
    fi
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../pdf/
    cd ..
elif [ "$1" == "CBI" ] ; then
    cd $1
    xelatex sermon_$1.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1.tex
    fi
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../pdf/
    cd ..
elif [ "$1" == "CGST" ] ; then
    cd $1
    xelatex sermon_$1.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1.tex
    fi
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../pdf/
    cd ..
elif [ "$1" == "DSCCC" ] ; then
    cd $1
    xelatex sermon_$1_2009-present.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2009-present.tex
    fi
    rm -f sermon_$1_2009-present.mtc*
    mv sermon_$1_2009-present.pdf ../../pdf/
    cd ..
elif [ "$1" == "FLWC" ] ; then
    cd $1
    xelatex sermon_$1_2020-present.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2020-present.tex
    fi
    rm -f sermon_$1_2020-present.mtc*
    mv sermon_$1_2020-present.pdf ../../pdf/
    cd ..
elif [ "$1" == "FVC" ] ; then
    cd $1
    xelatex sermon_$1_2017-present.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2017-present.tex
    fi
    rm -f sermon_$1_2017-present.mtc*
    mv sermon_$1_2017-present.pdf ../../pdf/
    cd ..
elif [ "$1" == "HKBC" ] ; then
    cd $1
    xelatex sermon_$1_1928-2007.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_1928-2007.tex
    fi
    rm -f sermon_$1_1928-2007.mtc*
    mv sermon_$1_1928-2007.pdf ../../pdf/
    cd ..
    cd $1
    xelatex sermon_$1_2008-present.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2008-present.tex
    fi
    rm -f sermon_$1_2008-present.mtc*
    mv sermon_$1_2008-present.pdf ../../pdf/
    cd ..
elif [ "$1" == "JNG" ] ; then
    cd $1
    xelatex sermon_$1_2012-18.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2012-18.tex
    fi
    rm -f sermon_$1_2012-18.mtc*
    mv sermon_$1_2012-18.pdf ../../pdf/
    cd ..
    cd $1
    xelatex sermon_$1_2019-20.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2019-20.tex
    fi
    rm -f sermon_$1_2019-20.mtc*
    mv sermon_$1_2019-20.pdf ../../pdf/
    cd ..
    cd $1
    xelatex sermon_$1_2021-22.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2021-22.tex
    fi
    rm -f sermon_$1_2021-22.mtc*
    mv sermon_$1_2021-22.pdf ../../pdf/
    cd ..
    cd $1
    xelatex sermon_$1_2023-24.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2023-24.tex
    fi
    rm -f sermon_$1_2023-24.mtc*
    mv sermon_$1_2023-24.pdf ../../pdf/
    cd ..
elif [ "$1" == "WWBS" ] ; then
    cd $1
    xelatex sermon_$1.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1.tex
    fi
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../pdf/
    cd ..
elif [ "$1" == "YFCX" ] ; then
    cd $1
    xelatex sermon_$1_2020-present.tex
    if [ "$2" != "once" ] ; then
    xelatex sermon_$1_2020-present.tex
    fi
    rm -f sermon_$1_2020-present.mtc*
    mv sermon_$1_2020-present.pdf ../../pdf/
    cd ..
fi
