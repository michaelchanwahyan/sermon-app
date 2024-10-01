#!/bin/bash
if   [ "$1" == "" ] ; then
    echo NAME
    echo      set_threadnum.sh - set the number of thread the transcription
    echo                         server uses in the whisper process
    echo
    echo SYNOPSIS
    echo      build.sh    [thread_number]
    echo
    echo DESCRIPTION
    echo      The default value of thread_num in the original whisper design is 4.
    echo      However subject to transcription engine capability the number could
    echo      be any value smaller than or equal to the core number of the
    echo      processor.  Practical experience is that 8 is good enough.
    exit
fi

# check if input argument is number
re='^[0-9]+$'
if ! [[ $yournumber =~ $re ]] ; then
   echo "Error: input argument is not a number !" >&2; exit 1
fi

for PROJ_NAME in $(find . -name "threadnum.txt")
do
    echo assign $1 to $PROJ_NAME ...
    echo $1 > $PROJ_NAME
    echo done !
    echo
done

