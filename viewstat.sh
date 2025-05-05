#!/bin/bash
echo FILE COUNT STATISTICS:

FN_ABSCC=$(  ls -1 ./data/ABSCC/*.txt   | wc -l)
FN_ACSMHK=$( ls -1 ./data/ACSMHK/*.txt  | wc -l)
FN_CBI=$(    ls -1 ./data/CBI/*.txt     | wc -l)
FN_CGST=$(   ls -1 ./data/CGST/*.txt    | wc -l)
FN_DSCCC=$(  ls -1 ./data/DSCCC/*.txt   | wc -l)
FN_FLWC=$(   ls -1 ./data/FLWC/*.txt    | wc -l)
FN_FVC=$(    ls -1 ./data/FVC/*.txt     | wc -l)
FN_GFC=$(    ls -1 ./data/GFC/*.txt     | wc -l)
FN_HKBC=$(   ls -1 ./data/HKBC/         | wc -l) # HKBC does not count *.txt as it takes raw html file format
FN_JNG=$(    ls -1 ./data/JNG/*.txt     | wc -l)
FN_KFC=$(    ls -1 ./data/KFC/*.txt     | wc -l)
FN_MKBC=$(   ls -1 ./data/MKBC/*.txt    | wc -l)
FN_PORCH=$(  ls -1 ./data/PORCH/*.txt   | wc -l)
FN_STBC=$(   ls -1 ./data/STBC/*.txt    | wc -l)
FN_VINE=$(   ls -1 ./data/VINE/*.txt    | wc -l)
FN_WWBS=$(   ls -1 ./data/WWBS/*.txt    | wc -l)
FN_YFCX=$(   ls -1 ./data/YFCX/*.txt    | wc -l)
FN_YOS=$(    ls -1 ./data/YOS/*.txt     | wc -l)
FN_TOTAL=$(echo $FN_ABSCC + $FN_ACSMHK + $FN_CBI + $FN_CGST + $FN_DSCCC + $FN_FLWC + $FN_FVC + $FN_GFC + $FN_HKBC + $FN_JNG + $FN_KFC + $FN_MKBC + $FN_PORCH + $FN_STBC + $FN_VINE + $FN_WWBS + $FN_YFCX + $FN_YOS | bc)

echo sermon count in ABSCC   : $FN_ABSCC   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_ABSCC   / FN_TOTAL))e-2)% \)
echo sermon count in ACSMHK  : $FN_ACSMHK  / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_ACSMHK  / FN_TOTAL))e-2)% \)
echo sermon count in CBI     : $FN_CBI     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CBI     / FN_TOTAL))e-2)% \)
echo sermon count in CGST    : $FN_CGST    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CGST    / FN_TOTAL))e-2)% \)
echo sermon count in DSCCC   : $FN_DSCCC   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_DSCCC   / FN_TOTAL))e-2)% \)
echo sermon count in FLWC    : $FN_FLWC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_FLWC    / FN_TOTAL))e-2)% \)
echo sermon count in FVC     : $FN_FVC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_FVC     / FN_TOTAL))e-2)% \)
echo sermon count in GFC     : $FN_GFC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_GFC     / FN_TOTAL))e-2)% \)
echo sermon count in HKBC    : $FN_HKBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_HKBC    / FN_TOTAL))e-2)% \)
echo sermon count in JNG     : $FN_JNG     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_JNG     / FN_TOTAL))e-2)% \)
echo sermon count in KFC     : $FN_KFC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_KFC     / FN_TOTAL))e-2)% \)
echo sermon count in MKBC    : $FN_MKBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_MKBC    / FN_TOTAL))e-2)% \)
echo sermon count in PORCH   : $FN_PORCH   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_PORCH   / FN_TOTAL))e-2)% \)
echo sermon count in STBC    : $FN_STBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_STBC    / FN_TOTAL))e-2)% \)
echo sermon count in VINE    : $FN_VINE    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_VINE    / FN_TOTAL))e-2)% \)
echo sermon count in WWBS    : $FN_WWBS    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_WWBS    / FN_TOTAL))e-2)% \)
echo sermon count in YFCX    : $FN_YFCX    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YFCX    / FN_TOTAL))e-2)% \)
echo sermon count in YOS     : $FN_YOS     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YOS     / FN_TOTAL))e-2)% \)

echo
echo COUNT RECENT DEVELOPMENT ACTIVE STATISTICS:
OU=$(git --no-pager log --oneline --since=$(date -v-90d '+%Y-%m-%d') --pretty=format:"%h") # gather the git hash within the past 90 day period
echo on ABSCC ...    ; CHNG_CNT_ABSCC=$(  git --no-pager show --name-only --oneline $OU | grep ABSCC   | wc -l) # for each hash count the file updates in specified sermon source
echo on ACSMHK ...   ; CHNG_CNT_ACSMHK=$( git --no-pager show --name-only --oneline $OU | grep ACSMHK  | wc -l) # for each hash count the file updates in specified sermon source
echo on CBI ...      ; CHNG_CNT_CBI=$(    git --no-pager show --name-only --oneline $OU | grep CBI     | wc -l) # for each hash count the file updates in specified sermon source
echo on CGST ...     ; CHNG_CNT_CGST=$(   git --no-pager show --name-only --oneline $OU | grep CGST    | wc -l) # for each hash count the file updates in specified sermon source
echo on DSCCC ...    ; CHNG_CNT_DSCCC=$(  git --no-pager show --name-only --oneline $OU | grep DSCCC   | wc -l) # for each hash count the file updates in specified sermon source
echo on FLWC ...     ; CHNG_CNT_FLWC=$(   git --no-pager show --name-only --oneline $OU | grep FLWC    | wc -l) # for each hash count the file updates in specified sermon source
echo on FVC ...      ; CHNG_CNT_FVC=$(    git --no-pager show --name-only --oneline $OU | grep FVC     | wc -l) # for each hash count the file updates in specified sermon source
echo on GFC ...      ; CHNG_CNT_GFC=$(    git --no-pager show --name-only --oneline $OU | grep GFC     | wc -l) # for each hash count the file updates in specified sermon source
echo on HKBC ...     ; CHNG_CNT_HKBC=$(   git --no-pager show --name-only --oneline $OU | grep HKBC    | wc -l) # for each hash count the file updates in specified sermon source
echo on JNG ...      ; CHNG_CNT_JNG=$(    git --no-pager show --name-only --oneline $OU | grep JNG     | wc -l) # for each hash count the file updates in specified sermon source
echo on KFC ...      ; CHNG_CNT_KFC=$(    git --no-pager show --name-only --oneline $OU | grep KFC     | wc -l) # for each hash count the file updates in specified sermon source
echo on MKBC ...     ; CHNG_CNT_MKBC=$(   git --no-pager show --name-only --oneline $OU | grep MKBC    | wc -l) # for each hash count the file updates in specified sermon source
echo on PORCH ...    ; CHNG_CNT_PORCH=$(  git --no-pager show --name-only --oneline $OU | grep PORCH   | wc -l) # for each hash count the file updates in specified sermon source
echo on STBC ...     ; CHNG_CNT_STBC=$(   git --no-pager show --name-only --oneline $OU | grep STBC    | wc -l) # for each hash count the file updates in specified sermon source
echo on VINE ...     ; CHNG_CNT_VINE=$(   git --no-pager show --name-only --oneline $OU | grep VINE    | wc -l) # for each hash count the file updates in specified sermon source
echo on WWBS ...     ; CHNG_CNT_WWBS=$(   git --no-pager show --name-only --oneline $OU | grep WWBS    | wc -l) # for each hash count the file updates in specified sermon source
echo on YFCX ...     ; CHNG_CNT_YFCX=$(   git --no-pager show --name-only --oneline $OU | grep YFCX    | wc -l) # for each hash count the file updates in specified sermon source
echo on YOS ...      ; CHNG_CNT_YOS=$(    git --no-pager show --name-only --oneline $OU | grep YOS     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_TOTAL=$(echo $CHNG_CNT_ABSCC + $CHNG_CNT_ACSMHK + $CHNG_CNT_CBI + $CHNG_CNT_CGST + $CHNG_CNT_DSCCC + $CHNG_CNT_FLWC + $CHNG_CNT_FVC + $CHNG_CNT_GFC + $CHNG_CNT_HKBC + $CHNG_CNT_JNG + $CHNG_CNT_KFC + $CHNG_CNT_MKBC + $CHNG_CNT_PORCH + $CHNG_CNT_STBC + $CHNG_CNT_VINE + $CHNG_CNT_WWBS + $CHNG_CNT_YFCX + $CHNG_CNT_YOS | bc)

echo activeness on ABSCC   : $CHNG_CNT_ABSCC   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_ABSCC   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on ACSMHK  : $CHNG_CNT_ACSMHK  / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_ACSMHK  / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on CBI     : $CHNG_CNT_CBI     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CBI     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on CGST    : $CHNG_CNT_CGST    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CGST    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on DSCCC   : $CHNG_CNT_DSCCC   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on FLWC    : $CHNG_CNT_FLWC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_FLWC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on FVC     : $CHNG_CNT_FVC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_FVC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on GFC     : $CHNG_CNT_GFC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_GFC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on HKBC    : $CHNG_CNT_HKBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on JNG     : $CHNG_CNT_JNG     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_JNG     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on KFC     : $CHNG_CNT_KFC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_KFC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on MKBC    : $CHNG_CNT_MKBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_MKBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on PORCH   : $CHNG_CNT_PORCH   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_PORCH   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on STBC    : $CHNG_CNT_STBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_STBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on VINE    : $CHNG_CNT_VINE    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_VINE    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on WWBS    : $CHNG_CNT_WWBS    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YFCX    : $CHNG_CNT_YFCX    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YOS     : $CHNG_CNT_YOS     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YOS     / CHNG_CNT_TOTAL))e-2)% \)

echo
echo source \| sermon no. \(out of $FN_TOTAL\) \| amount of dev. activity \(out of $CHNG_CNT_TOTAL\)
echo ----\|----\|----
echo ABSCC   \| $(printf "%.1f" $((10**4 * FN_ABSCC   / FN_TOTAL))e-2)% \($FN_ABSCC   \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_ABSCC   / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_ABSCC   \)
echo ACSMHK  \| $(printf "%.1f" $((10**4 * FN_ACSMHK  / FN_TOTAL))e-2)% \($FN_ACSMHK  \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_ACSMHK  / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_ACSMHK  \)
echo CBI     \| $(printf "%.1f" $((10**4 * FN_CBI     / FN_TOTAL))e-2)% \($FN_CBI     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_CBI     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_CBI     \)
echo CGST    \| $(printf "%.1f" $((10**4 * FN_CGST    / FN_TOTAL))e-2)% \($FN_CGST    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_CGST    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_CGST    \)
echo DSCCC   \| $(printf "%.1f" $((10**4 * FN_DSCCC   / FN_TOTAL))e-2)% \($FN_DSCCC   \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC   / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_DSCCC   \)
echo FLWC    \| $(printf "%.1f" $((10**4 * FN_FLWC    / FN_TOTAL))e-2)% \($FN_FLWC    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_FLWC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_FLWC    \)
echo FVC     \| $(printf "%.1f" $((10**4 * FN_FVC     / FN_TOTAL))e-2)% \($FN_FVC     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_FVC     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_FVC     \)
echo GFC     \| $(printf "%.1f" $((10**4 * FN_GFC     / FN_TOTAL))e-2)% \($FN_GFC     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_GFC     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_GFC     \)
echo HKBC    \| $(printf "%.1f" $((10**4 * FN_HKBC    / FN_TOTAL))e-2)% \($FN_HKBC    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_HKBC    \)
echo JNG     \| $(printf "%.1f" $((10**4 * FN_JNG     / FN_TOTAL))e-2)% \($FN_JNG     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_JNG     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_JNG     \)
echo KFC     \| $(printf "%.1f" $((10**4 * FN_KFC     / FN_TOTAL))e-2)% \($FN_KFC     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_KFC     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_KFC     \)
echo MKBC    \| $(printf "%.1f" $((10**4 * FN_MKBC    / FN_TOTAL))e-2)% \($FN_MKBC    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_MKBC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_MKBC    \)
echo PORCH   \| $(printf "%.1f" $((10**4 * FN_PORCH   / FN_TOTAL))e-2)% \($FN_PORCH   \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_PORCH   / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_PORCH   \)
echo STBC    \| $(printf "%.1f" $((10**4 * FN_STBC    / FN_TOTAL))e-2)% \($FN_STBC    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_STBC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_STBC    \)
echo VINE    \| $(printf "%.1f" $((10**4 * FN_VINE    / FN_TOTAL))e-2)% \($FN_VINE    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_VINE    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_VINE    \)
echo WWBS    \| $(printf "%.1f" $((10**4 * FN_WWBS    / FN_TOTAL))e-2)% \($FN_WWBS    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_WWBS    \)
echo YFCX    \| $(printf "%.1f" $((10**4 * FN_YFCX    / FN_TOTAL))e-2)% \($FN_YFCX    \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_YFCX    \)
echo YOS     \| $(printf "%.1f" $((10**4 * FN_YOS     / FN_TOTAL))e-2)% \($FN_YOS     \) \| $(printf "%.1f" $((10**4 * CHNG_CNT_YOS     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_YOS     \)

