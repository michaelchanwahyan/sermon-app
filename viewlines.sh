#!/bin/bash
FILE=stat_cnt_file_temp

echo remove existing stat record
rm $FILE
touch $FILE

for FOLDER in build data projects whisper
do
    echo $FOLDER
    for fileType in tex txt py ipynb csv
    do
        echo "    working on $fileType"
        find $FOLDER -name "*.$fileType"   -exec wc -l {} \; >> $FILE
    done
    find $FOLDER -name "*0"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*1"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*2"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*3"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*4"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*5"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*6"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*7"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*8"    -exec wc -l {} \; >> $FILE
    find $FOLDER -name "*9"    -exec wc -l {} \; >> $FILE
done

rowCntTotal=0
for rowCntCurr in $(awk '{print $1}' $FILE)
do
    rowCntTotal=$((rowCntTotal + $rowCntCurr))
done
echo total number of text and source lines: $rowCntTotal

rm $FILE

