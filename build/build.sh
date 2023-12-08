#!/bin/bash
echo build sermon project $1
if [ "$1" == "JNG" ] ; then
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
elif [ "$1" == "DSCCC" ] ; then
    cd $1
    xelatex sermon_$1_2009-present.tex
    xelatex sermon_$1_2009-present.tex
    rm -f sermon_$1_2009-present.mtc*
    mv sermon_$1_2009-present.pdf ../../
    cd ..
elif [ "$1" == "YFCX" ] ; then
    cd $1
    xelatex sermon_$1_2020-present.tex
    xelatex sermon_$1_2020-present.tex
    rm -f sermon_$1_2020-present.mtc*
    mv sermon_$1_2020-present.pdf ../../
    cd ..
fi
