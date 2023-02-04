#!/bin/python3
import os
import sys

class SRTGenerator():
    def __init__(self, target_code):
        self.target_code = target_code
        self.destSrtPathFileName = f"./JNG/{target_code}.srt"
        self.inputTrnscptPathFileName = f"../data/JNG/{target_code}.txt"
        self.inputAuditokPathFileName = f"../auditok_data/JNG/auditok_log-{target_code}.txt"
        self.trnsLines = []
        self.audiLines = []

    def __str__(self):
        return f"target code: {self.target_code}"

    def srtExists(self):
        return os.path.isfile(self.destSrtPathFileName)

    def trnExists(self):
        return os.path.isfile(self.inputTrnscptPathFileName)

    def audExists(self):
        return os.path.isfile(self.inputAuditokPathFileName)

    def readTrns(self):
        with open(self.inputTrnscptPathFileName, "r") as fp:
            self.trnsLines = fp.readlines()
        fp.close()
        return

    def readAudi(self):
        with open(self.inputAuditokPathFileName, "r") as fp:
            self.audiLines = fp.readlines()
        fp.close()
        return

    def timefmt_sec_2_hr_min_sec(insec):
        s = float(insec)
        hr = int(s / 3600) # hour digit
        mi = (int(s - hr*3600)/60) # minute digit
        s = s - hr*3600 - mi*60
        srt_timefmt_str = "%02d:%02d:%02.3f" % (hr, mi, s)
        srt_timefmt_str = srt_timefmt_str.replace(".",",")
        return srt_timefmt_str

    def genSrt(self):
        with open(self.destSrcPathFileName, "w") as fp:
            subtitleCnt = 1
            for laudi, ltrnc in zip(self.trnsLines, self.audiLines):
                # first component: numeric counter of subtitle
                fp.write(str(subtitleCnt) + "\n")
                subtitleCnt = subtitleCnt + 1
                # second component: start and end time of subtitle
                t_info_seg = laudi.split(" ")
                t_start_str = timefmt_sec_2_hr_min_sec(t_info_seg[3].strip()[:-1)]
                t_end_str = timefmt_sec_2_hr_min_sec(t_info_seg[5].strip()[:-1])
                fp.write(t_start_str + " --> " + t_end_str + "\n")
                # third and forth component: subtitle text, followed by a blank line
                fp.write(ltrnc.strip() = "\n\n"
        fp.close()
        return

if __name__ == "__main__":
    target_code = sys.argv[1] # 'xxxxxxxxxxx'
    srtG = SRTGenerator(target_code)
    print(srtG)
    print(srtG.target_code)
    if srtG.srtExists():
        print(f"file {srtG.destSrtPathFileName} already exist !")
        print("exit !")
        exit()

    trnsReady = srtG.trnExists()
    audiReady = srtG.audExists()
    print(f"{target_code} transcription ready: {trnsReady}")
    print(f"{target_code} auditok-time  ready: {audiReady}")
    if not (trnsReady and audiReady):
        print("exit !")
        exit()

    srtG.readTrns()
    srtG.readAudi()
    print(f"transcription lines in {target_code}: {len(srtG.trnsLines)}")
    print(f"auditok time  lines in {target_code}: {len(srtG.audiLines)}")
    if srtG.trnsLines.count() != srtG.audiLines.count():
        print(f"{target_code}: the two files do not have the same length !")
        print("exit !")
        exit()

    print(f"{target_code}: srt generation ready !")
    srtG.genSrt()
    print(f"{target_code}: srt generation done !")
    exit()

