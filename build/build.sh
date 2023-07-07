#!/bin/bash
echo build sermon project $1
xelatex $1/sermon_$1_2012-18.tex ; xelatex $1/sermon_$1_2012-18.tex ; mv sermon_$1_2012-18.mtc* $1/ ; mv sermon_$1_2012-18.pdf ../
xelatex $1/sermon_$1_2019-20.tex ; xelatex $1/sermon_$1_2019-20.tex ; mv sermon_$1_2019-20.mtc* $1/ ; mv sermon_$1_2019-20.pdf ../
xelatex $1/sermon_$1_2021-22.tex ; xelatex $1/sermon_$1_2021-22.tex ; mv sermon_$1_2021-22.mtc* $1/ ; mv sermon_$1_2021-22.pdf ../
