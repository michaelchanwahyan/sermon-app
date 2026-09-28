#!/bin/bash
xelatex sermon_CHURCHK_vol001.tex &
xelatex sermon_CHURCHK_vol002.tex &
xelatex sermon_CHURCHK_vol003.tex &
xelatex sermon_CHURCHK_vol004.tex &
xelatex sermon_CHURCHK_vol005.tex &
xelatex sermon_CHURCHK_vol006.tex

xelatex sermon_CHURCHK_vol007.tex &
xelatex sermon_CHURCHK_vol008.tex &
xelatex sermon_CHURCHK_vol009.tex &
xelatex sermon_CHURCHK_vol010.tex &
xelatex sermon_CHURCHK_vol011.tex &
xelatex sermon_CHURCHK_vol012.tex

xelatex sermon_CHURCHK_vol013.tex &
xelatex sermon_CHURCHK_vol014.tex &
xelatex sermon_CHURCHK_vol015.tex &
xelatex sermon_CHURCHK_vol016.tex &
xelatex sermon_CHURCHK_vol017.tex &
xelatex sermon_CHURCHK_vol018.tex

xelatex sermon_CHURCHK_vol019.tex
xelatex sermon_CHURCHK_vol020.tex

xelatex sermon_CHURCHK_vol001.tex &
xelatex sermon_CHURCHK_vol002.tex &
xelatex sermon_CHURCHK_vol003.tex &
xelatex sermon_CHURCHK_vol004.tex &
xelatex sermon_CHURCHK_vol005.tex &
xelatex sermon_CHURCHK_vol006.tex

xelatex sermon_CHURCHK_vol007.tex &
xelatex sermon_CHURCHK_vol008.tex &
xelatex sermon_CHURCHK_vol009.tex &
xelatex sermon_CHURCHK_vol010.tex &
xelatex sermon_CHURCHK_vol011.tex &
xelatex sermon_CHURCHK_vol012.tex

xelatex sermon_CHURCHK_vol013.tex &
xelatex sermon_CHURCHK_vol014.tex &
xelatex sermon_CHURCHK_vol015.tex &
xelatex sermon_CHURCHK_vol016.tex &
xelatex sermon_CHURCHK_vol017.tex &
xelatex sermon_CHURCHK_vol018.tex

xelatex sermon_CHURCHK_vol019.tex
xelatex sermon_CHURCHK_vol020.tex

yes | mv ./sermon_CHURCHK_*.pdf ../../pdf/
rm -f ./sermon_CHURCHK_*.mtc*

