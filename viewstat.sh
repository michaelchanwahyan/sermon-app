#!/bin/bash
echo FILE COUNT STATISTICS:

FN_CBI=$(    ls -1 ./data/CBI     | wc -l)
FN_CGST=$(   ls -1 ./data/CGST    | wc -l)
FN_DSCCC=$(  ls -1 ./data/DSCCC   | wc -l)
FN_FVC=$(    ls -1 ./data/FVC     | wc -l)
FN_HKBC=$(   ls -1 ./data/HKBC    | wc -l)
FN_JNG=$(    ls -1 ./data/JNG     | wc -l)
FN_WWBS=$(   ls -1 ./data/WWBS    | wc -l)
FN_YFCX=$(   ls -1 ./data/YFCX    | wc -l)
FN_TOTAL=$(echo $FN_CBI + $FN_CGST + $FN_DSCCC + $FN_FVC + $FN_HKBC + $FN_JNG + $FN_WWBS + $FN_YFCX | bc)

echo sermon count in CBI     : $FN_CBI     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CBI     / FN_TOTAL))e-2)% \)
echo sermon count in CGST    : $FN_CGST    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_CGST    / FN_TOTAL))e-2)% \)
echo sermon count in DSCCC   : $FN_DSCCC   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_DSCCC   / FN_TOTAL))e-2)% \)
echo sermon count in FVC     : $FN_FVC     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_FVC     / FN_TOTAL))e-2)% \)
echo sermon count in HKBC    : $FN_HKBC    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_HKBC    / FN_TOTAL))e-2)% \)
echo sermon count in JNG     : $FN_JNG     / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_JNG     / FN_TOTAL))e-2)% \)
echo sermon count in WWBS    : $FN_WWBS    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_WWBS    / FN_TOTAL))e-2)% \)
echo sermon count in YFCX    : $FN_YFCX    / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YFCX    / FN_TOTAL))e-2)% \)

echo
echo DEVELOPMENT ACTIVE STATISTICS:
OU=$(git --no-pager log --oneline --since=$(date -v-90d '+%Y-%m-%d') --pretty=format:"%h") # gather the git hash within the past 90 day period
CHNG_CNT_CBI=$(    git --no-pager show --name-only --oneline $OU | grep CBI     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_CGST=$(   git --no-pager show --name-only --oneline $OU | grep CGST    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_DSCCC=$(  git --no-pager show --name-only --oneline $OU | grep DSCCC   | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_FVC=$(    git --no-pager show --name-only --oneline $OU | grep FVC     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_HKBC=$(   git --no-pager show --name-only --oneline $OU | grep HKBC    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_JNG=$(    git --no-pager show --name-only --oneline $OU | grep JNG     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_WWBS=$(   git --no-pager show --name-only --oneline $OU | grep WWBS    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_YFCX=$(   git --no-pager show --name-only --oneline $OU | grep YFCX    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_TOTAL=$(echo $CHNG_CNT_DSCCC + $CHNG_CNT_HKBC + $CHNG_CNT_JNG + $CHNG_CNT_YFCX | bc)

echo activeness on CBI     : $CHNG_CNT_CBI     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CBI     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on CGST    : $CHNG_CNT_CGST    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_CGST    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on DSCCC   : $CHNG_CNT_DSCCC   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on FVC     : $CHNG_CNT_FVC     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_FVC     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on HKBC    : $CHNG_CNT_HKBC    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on JNG     : $CHNG_CNT_JNG     / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_JNG     / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on WWBS    : $CHNG_CNT_WWBS    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS    / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YFCX    : $CHNG_CNT_YFCX    / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX    / CHNG_CNT_TOTAL))e-2)% \)

echo
echo sermon source \| transcript in portion \| recent development in portion
echo ----\|----\|----
echo CBI     \| $(printf "%.1f" $((10**4 * FN_CBI   / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_CBI   / CHNG_CNT_TOTAL))e-2)%
echo CGST    \| $(printf "%.1f" $((10**4 * FN_CGST  / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_CGST  / CHNG_CNT_TOTAL))e-2)%
echo DSCCC   \| $(printf "%.1f" $((10**4 * FN_DSCCC / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC / CHNG_CNT_TOTAL))e-2)%
echo FVC     \| $(printf "%.1f" $((10**4 * FN_FVC   / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_FVC   / CHNG_CNT_TOTAL))e-2)%
echo HKBC    \| $(printf "%.1f" $((10**4 * FN_HKBC  / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC  / CHNG_CNT_TOTAL))e-2)%
echo JNG     \| $(printf "%.1f" $((10**4 * FN_JNG   / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_JNG   / CHNG_CNT_TOTAL))e-2)%
echo WWBS    \| $(printf "%.1f" $((10**4 * FN_WWBS  / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_WWBS  / CHNG_CNT_TOTAL))e-2)%
echo YFCX    \| $(printf "%.1f" $((10**4 * FN_YFCX  / FN_TOTAL))e-2)% \| $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX  / CHNG_CNT_TOTAL))e-2)%
