#!/bin/bash
echo FILE COUNT STATISTICS:

FN_ACSMHK=$( ls -1 ./data/ACSMHK  | wc -l)
FN_CBI=$(    ls -1 ./data/CBI     | wc -l)
FN_CGST=$(   ls -1 ./data/CGST    | wc -l)
FN_DSCCC=$(  ls -1 ./data/DSCCC   | wc -l)
FN_FLWC=$(   ls -1 ./data/FLWC    | wc -l)
FN_FVC=$(    ls -1 ./data/FVC     | wc -l)
FN_HKBC=$(   ls -1 ./data/HKBC    | wc -l)
FN_JNG=$(    ls -1 ./data/JNG     | wc -l)
FN_KFC=$(    ls -1 ./data/KFC     | wc -l)
FN_PORCH=$(  ls -1 ./data/PORCH   | wc -l)
FN_STBC=$(   ls -1 ./data/STBC    | wc -l)
FN_VINE=$(   ls -1 ./data/VINE    | wc -l)
FN_WWBS=$(   ls -1 ./data/WWBS    | wc -l)
FN_YFCX=$(   ls -1 ./data/YFCX    | wc -l)
FN_YOS=$(    ls -1 ./data/YOS     | wc -l)
FN_TOTAL=$(echo $FN_ACSMHK + $FN_CBI + $FN_CGST + $FN_DSCCC + $FN_FLWC + $FN_FVC + $FN_HKBC + $FN_JNG + $FN_KFC + $FN_PORCH + $FN_STBC + $FN_VINE + $FN_WWBS + $FN_YFCX + $FN_YOS | bc)

echo sermon count in ACSMHK  : $FN_ACSMHK  / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_ACSMHK  / FN_TOTAL))e-2)% \)
echo sermon count in CBI     : $FN_CBI     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CBI     / FN_TOTAL))e-2)% \)
echo sermon count in CGST    : $FN_CGST    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CGST    / FN_TOTAL))e-2)% \)
echo sermon count in DSCCC   : $FN_DSCCC   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_DSCCC   / FN_TOTAL))e-2)% \)
echo sermon count in FLWC    : $FN_FLWC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_FLWC    / FN_TOTAL))e-2)% \)
echo sermon count in FVC     : $FN_FVC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_FVC     / FN_TOTAL))e-2)% \)
echo sermon count in HKBC    : $FN_HKBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_HKBC    / FN_TOTAL))e-2)% \)
echo sermon count in JNG     : $FN_JNG     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_JNG     / FN_TOTAL))e-2)% \)
echo sermon count in KFC     : $FN_KFC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_KFC     / FN_TOTAL))e-2)% \)
echo sermon count in PORCH   : $FN_PORCH   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_PORCH   / FN_TOTAL))e-2)% \)
echo sermon count in STBC    : $FN_STBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_STBC    / FN_TOTAL))e-2)% \)
echo sermon count in VINE    : $FN_VINE    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_VINE    / FN_TOTAL))e-2)% \)
echo sermon count in WWBS    : $FN_WWBS    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_WWBS    / FN_TOTAL))e-2)% \)
echo sermon count in YFCX    : $FN_YFCX    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YFCX    / FN_TOTAL))e-2)% \)
echo sermon count in YOS     : $FN_YOS     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YOS     / FN_TOTAL))e-2)% \)

echo
echo DEVELOPMENT ACTIVE STATISTICS:
OU=$(git --no-pager log --oneline --since=$(date -v-90d '+%Y-%m-%d') --pretty=format:"%h") # gather the git hash within the past 90 day period
echo ACSMHK ...   ; CHNG_CNT_ACSMHK=$( git --no-pager show --name-only --oneline $OU | grep ACSMHK  | wc -l) # for each hash count the file updates in specified sermon source
echo CBI ...      ; CHNG_CNT_CBI=$(    git --no-pager show --name-only --oneline $OU | grep CBI     | wc -l) # for each hash count the file updates in specified sermon source
echo CGST ...     ; CHNG_CNT_CGST=$(   git --no-pager show --name-only --oneline $OU | grep CGST    | wc -l) # for each hash count the file updates in specified sermon source
echo DSCCC ...    ; CHNG_CNT_DSCCC=$(  git --no-pager show --name-only --oneline $OU | grep DSCCC   | wc -l) # for each hash count the file updates in specified sermon source
echo FLWC ...     ; CHNG_CNT_FLWC=$(   git --no-pager show --name-only --oneline $OU | grep FLWC    | wc -l) # for each hash count the file updates in specified sermon source
echo FVC ...      ; CHNG_CNT_FVC=$(    git --no-pager show --name-only --oneline $OU | grep FVC     | wc -l) # for each hash count the file updates in specified sermon source
echo HKBC ...     ; CHNG_CNT_HKBC=$(   git --no-pager show --name-only --oneline $OU | grep HKBC    | wc -l) # for each hash count the file updates in specified sermon source
echo JNG ...      ; CHNG_CNT_JNG=$(    git --no-pager show --name-only --oneline $OU | grep JNG     | wc -l) # for each hash count the file updates in specified sermon source
echo KFC ...      ; CHNG_CNT_KFC=$(    git --no-pager show --name-only --oneline $OU | grep KFC     | wc -l) # for each hash count the file updates in specified sermon source
echo PORCH ...    ; CHNG_CNT_PORCH=$(  git --no-pager show --name-only --oneline $OU | grep PORCH   | wc -l) # for each hash count the file updates in specified sermon source
echo STBC ...     ; CHNG_CNT_STBC=$(   git --no-pager show --name-only --oneline $OU | grep STBC    | wc -l) # for each hash count the file updates in specified sermon source
echo VINE ...     ; CHNG_CNT_VINE=$(   git --no-pager show --name-only --oneline $OU | grep VINE    | wc -l) # for each hash count the file updates in specified sermon source
echo WWBS ...     ; CHNG_CNT_WWBS=$(   git --no-pager show --name-only --oneline $OU | grep WWBS    | wc -l) # for each hash count the file updates in specified sermon source
echo YFCX ...     ; CHNG_CNT_YFCX=$(   git --no-pager show --name-only --oneline $OU | grep YFCX    | wc -l) # for each hash count the file updates in specified sermon source
echo YOS ...      ; CHNG_CNT_YOS=$(    git --no-pager show --name-only --oneline $OU | grep YOS     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_TOTAL=$(echo $CHNG_CNT_ACSMHK + $CHNG_CNT_CBI + $CHNG_CNT_CGST + $CHNG_CNT_DSCCC + $CHNG_CNT_FLWC + $CHNG_CNT_FVC + $CHNG_CNT_HKBC + $CHNG_CNT_JNG + $CHNG_CNT_KFC + $CHNG_CNT_PORCH + $CHNG_CNT_STBC + $CHNG_CNT_VINE + $CHNG_CNT_WWBS + $CHNG_CNT_YFCX + $CHNG_CNT_YOS | bc)

echo activeness on ACSMHK  : $CHNG_CNT_ACSMHK  / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_ACSMHK  / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on CBI     : $CHNG_CNT_CBI     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CBI     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on CGST    : $CHNG_CNT_CGST    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CGST    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on DSCCC   : $CHNG_CNT_DSCCC   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on FLWC    : $CHNG_CNT_FLWC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_FLWC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on FVC     : $CHNG_CNT_FVC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_FVC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on HKBC    : $CHNG_CNT_HKBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on JNG     : $CHNG_CNT_JNG     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_JNG     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on KFC     : $CHNG_CNT_KFC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_KFC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on PORCH   : $CHNG_CNT_PORCH   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_PORCH   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on STBC    : $CHNG_CNT_STBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_STBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on VINE    : $CHNG_CNT_VINE    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_VINE    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on WWBS    : $CHNG_CNT_WWBS    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YFCX    : $CHNG_CNT_YFCX    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YOS     : $CHNG_CNT_YOS     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YOS     / CHNG_CNT_TOTAL))e-2)% \)

echo
echo sermon source \| transcript total count \| recent development activity
echo ----\|----\|----
echo ACSMHK  \| $(printf "%.1f" $((10**4 * FN_ACSMHK  / FN_TOTAL))e-2)% \($FN_ACSMHK  / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_ACSMHK  / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_ACSMHK  / $CHNG_CNT_TOTAL\)
echo CBI     \| $(printf "%.1f" $((10**4 * FN_CBI     / FN_TOTAL))e-2)% \($FN_CBI     / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_CBI     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_CBI     / $CHNG_CNT_TOTAL\)
echo CGST    \| $(printf "%.1f" $((10**4 * FN_CGST    / FN_TOTAL))e-2)% \($FN_CGST    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_CGST    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_CGST    / $CHNG_CNT_TOTAL\)
echo DSCCC   \| $(printf "%.1f" $((10**4 * FN_DSCCC   / FN_TOTAL))e-2)% \($FN_DSCCC   / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC   / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_DSCCC   / $CHNG_CNT_TOTAL\)
echo FLWC    \| $(printf "%.1f" $((10**4 * FN_FLWC    / FN_TOTAL))e-2)% \($FN_FLWC    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_FLWC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_FLWC    / $CHNG_CNT_TOTAL\)
echo FVC     \| $(printf "%.1f" $((10**4 * FN_FVC     / FN_TOTAL))e-2)% \($FN_FVC     / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_FVC     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_FVC     / $CHNG_CNT_TOTAL\)
echo HKBC    \| $(printf "%.1f" $((10**4 * FN_HKBC    / FN_TOTAL))e-2)% \($FN_HKBC    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_HKBC    / $CHNG_CNT_TOTAL\)
echo JNG     \| $(printf "%.1f" $((10**4 * FN_JNG     / FN_TOTAL))e-2)% \($FN_JNG     / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_JNG     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_JNG     / $CHNG_CNT_TOTAL\)
echo KFC     \| $(printf "%.1f" $((10**4 * FN_KFC     / FN_TOTAL))e-2)% \($FN_KFC     / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_KFC     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_KFC     / $CHNG_CNT_TOTAL\)
echo PORCH   \| $(printf "%.1f" $((10**4 * FN_PORCH   / FN_TOTAL))e-2)% \($FN_PORCH   / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_PORCH   / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_PORCH   / $CHNG_CNT_TOTAL\)
echo STBC    \| $(printf "%.1f" $((10**4 * FN_STBC    / FN_TOTAL))e-2)% \($FN_STBC    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_STBC    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_STBC    / $CHNG_CNT_TOTAL\)
echo VINE    \| $(printf "%.1f" $((10**4 * FN_VINE    / FN_TOTAL))e-2)% \($FN_VINE    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_VINE    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_VINE    / $CHNG_CNT_TOTAL\)
echo WWBS    \| $(printf "%.1f" $((10**4 * FN_WWBS    / FN_TOTAL))e-2)% \($FN_WWBS    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_WWBS    / $CHNG_CNT_TOTAL\)
echo YFCX    \| $(printf "%.1f" $((10**4 * FN_YFCX    / FN_TOTAL))e-2)% \($FN_YFCX    / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX    / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_YFCX    / $CHNG_CNT_TOTAL\)
echo YOS     \| $(printf "%.1f" $((10**4 * FN_YOS     / FN_TOTAL))e-2)% \($FN_YOS     / $FN_TOTAL\) \| $(printf "%.1f" $((10**4 * CHNG_CNT_YOS     / CHNG_CNT_TOTAL))e-2)% \($CHNG_CNT_YOS     / $CHNG_CNT_TOTAL\)

