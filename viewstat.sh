#!/bin/bash
echo FILE COUNT STATISTICS:

FN_DSCCC=$(ls -1 ./data/DSCCC | wc -l)
FN_HKBC=$(ls -1 ./data/HKBC | wc -l)
FN_JNG=$(ls -1 ./data/JNG | wc -l)
FN_YFCX=$(ls -1 ./data/YFCX | wc -l)
FN_TOTAL=$(echo $FN_DSCCC + $FN_HKBC + $FN_JNG + $FN_YFCX | bc)

echo sermon count in DSCCC : $FN_DSCCC / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_DSCCC / FN_TOTAL))e-2)% \)
echo sermon count in HKBC  : $FN_HKBC  / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_HKBC  / FN_TOTAL))e-2)% \)
echo sermon count in JNG   : $FN_JNG   / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_JNG   / FN_TOTAL))e-2)% \)
echo sermon count in YFCX  : $FN_YFCX  / $FN_TOTAL \( $(printf "%.1f" $((10**4 * FN_YFCX  / FN_TOTAL))e-2)% \)

echo
echo DEVELOPMENT ACTIVE STATISTICS:
OU=$(git --no-pager log --oneline --since=$(date -v-90d '+%Y-%m-%d') --pretty=format:"%h") # gather the git hash within the past 90 day period
CHNG_CNT_DSCCC=$( git --no-pager show --name-only --oneline $OU | grep DSCCC   | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_HKBC=$(  git --no-pager show --name-only --oneline $OU | grep HKBC    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_JNG=$(   git --no-pager show --name-only --oneline $OU | grep JNG     | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_YFCX=$(  git --no-pager show --name-only --oneline $OU | grep YFCX    | wc -l) # for each hash count the file updates in specified sermon source
CHNG_CNT_TOTAL=$(echo $CHNG_CNT_DSCCC + $CHNG_CNT_HKBC + $CHNG_CNT_JNG + $CHNG_CNT_YFCX | bc)

echo activeness on DSCCC   : $CHNG_CNT_DSCCC / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on HKBC    : $CHNG_CNT_HKBC  / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC  / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on JNG     : $CHNG_CNT_JNG   / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_JNG   / CHNG_CNT_TOTAL))e-2)% \)
echo activeness on YFCX    : $CHNG_CNT_YFCX  / $CHNG_CNT_TOTAL \( $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX  / CHNG_CNT_TOTAL))e-2)% \)

echo
echo sermon source \| text transcript proportion \| portion in recent development
echo ----\|----\|----
echo DSCCC   \| $(printf "%.1f" $((10**4 * FN_DSCCC / FN_TOTAL))e-2)%    \| $(printf "%.1f" $((10**4 * CHNG_CNT_DSCCC / CHNG_CNT_TOTAL))e-2)%
echo HKBC    \| $(printf "%.1f" $((10**4 * FN_HKBC / FN_TOTAL))e-2)%     \| $(printf "%.1f" $((10**4 * CHNG_CNT_HKBC  / CHNG_CNT_TOTAL))e-2)%
echo JNG     \| $(printf "%.1f" $((10**4 * FN_JNG / FN_TOTAL))e-2)%      \| $(printf "%.1f" $((10**4 * CHNG_CNT_JNG   / CHNG_CNT_TOTAL))e-2)%
echo YFCX    \| $(printf "%.1f" $((10**4 * FN_YFCX / FN_TOTAL))e-2)%     \| $(printf "%.1f" $((10**4 * CHNG_CNT_YFCX  / CHNG_CNT_TOTAL))e-2)%
