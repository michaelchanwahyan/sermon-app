#!/bin/bash
echo build sermon project $1
if   [ "$1" == "genall" ] ; then
    cd ../whisper
    python3 convert_srt2txt.py CBI
    python3 convert_srt2txt.py CGST
    python3 convert_srt2txt.py JNG
    python3 convert_srt2txt.py WWBS
    python3 convert_srt2txt.py YFCX
    cd ../projects
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
    ./build.sh CBI
    ./build.sh CGST
    ./build.sh DSCCC
    ./build.sh HKBC
    ./build.sh JNG
    ./build.sh WWBS
    ./build.sh YFCX
elif [ "$1" == "CBI" ] ; then
    cd $1
    xelatex sermon_$1.tex
    xelatex sermon_$1.tex
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../
    cd ..
elif [ "$1" == "CGST" ] ; then
    cd $1
    xelatex sermon_$1.tex
    xelatex sermon_$1.tex
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../
    cd ..
elif [ "$1" == "DSCCC" ] ; then
    cd $1
    xelatex sermon_$1_2009-present.tex
    xelatex sermon_$1_2009-present.tex
    rm -f sermon_$1_2009-present.mtc*
    mv sermon_$1_2009-present.pdf ../../
    cd ..
elif [ "$1" == "HKBC" ] ; then
    cd $1
    xelatex sermon_$1_1928-2007.tex
    xelatex sermon_$1_1928-2007.tex
    rm -f sermon_$1_1928-2007.mtc*
    mv sermon_$1_1928-2007.pdf ../../
    cd ..
    cd $1
    xelatex sermon_$1_2008-present.tex
    xelatex sermon_$1_2008-present.tex
    rm -f sermon_$1_2008-present.mtc*
    mv sermon_$1_2008-present.pdf ../../
    cd ..
elif [ "$1" == "JNG" ] ; then
    cd $1
    xelatex sermon_$1_2012-18.tex
    xelatex sermon_$1_2012-18.tex
    rm -f sermon_$1_2012-18.mtc*
    mv sermon_$1_2012-18.pdf ../../
    cd ..
    cd $1
    xelatex sermon_$1_2019-20.tex
    xelatex sermon_$1_2019-20.tex
    rm -f sermon_$1_2019-20.mtc*
    mv sermon_$1_2019-20.pdf ../../
    cd ..
    cd $1
    xelatex sermon_$1_2021-22.tex
    xelatex sermon_$1_2021-22.tex
    rm -f sermon_$1_2021-22.mtc*
    mv sermon_$1_2021-22.pdf ../../
    cd ..
    cd $1
    xelatex sermon_$1_2023-24.tex
    xelatex sermon_$1_2023-24.tex
    rm -f sermon_$1_2023-24.mtc*
    mv sermon_$1_2023-24.pdf ../../
    cd ..
elif [ "$1" == "WWBS" ] ; then
    cd $1
    xelatex sermon_$1.tex
    xelatex sermon_$1.tex
    rm -f sermon_$1.mtc*
    mv sermon_$1.pdf ../../
    cd ..
elif [ "$1" == "YFCX" ] ; then
    cd $1
    xelatex sermon_$1_2020-present.tex
    xelatex sermon_$1_2020-present.tex
    rm -f sermon_$1_2020-present.mtc*
    mv sermon_$1_2020-present.pdf ../../
    cd ..
fi
