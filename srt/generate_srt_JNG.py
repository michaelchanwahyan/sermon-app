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

    def timefmt_sec_2_hr_min_sec(self, insec):
        s = float(insec)
        hr = int(s / 3600) # hour digit
        mi = int((s - hr*3600)/60) # minute digit
        s = s - hr*3600 - mi*60
        srt_timefmt_str = "%02d:%02d:%02.3f" % (hr, mi, s)
        srt_timefmt_str = srt_timefmt_str.replace(".",",")
        return srt_timefmt_str

    def genSrt(self):
        with open(self.destSrtPathFileName, "w") as fp:
            subtitleCnt = 1
            for ltrns, laudi in zip(self.trnsLines, self.audiLines):
                ''' sample: zzcvcdgkilA
                <line no> <srt text file content>
                |    1   |  1                                             | <1st component>
                |    2   |  00:00:2,450 --> 00:00:8,200                   | <2nd component>
                |    3   |  多謝你咁介紹我啫，嚇我都諗緊係邊個啦啦。      | <3rd component>
                |    4   |                                                | <4th component>
                |    5   |  2                                             |
                |    6   |  00:00:8,500 --> 00:00:11,000                  |
                |    7   |  我就唔敢當嚇，即係因為。                      |
                |    8   |                                                |
                |    9   |  3                                             |
                |   10   |  00:00:11,000 --> 00:00:14,900                 |
                |   11   |  誒，正常咧，一個快樂嘅人咧？應該1日咧？係笑。 |
                |   12   |                                                |
                |   13   |  4                                             |
                |   14   |  00:00:15,100 --> 00:00:16,900                 |
                |   15   |  誒256次。                                     |
                '''
                # first component: numeric counter of subtitle
                fp.write(str(subtitleCnt) + "\n")
                subtitleCnt = subtitleCnt + 1
                # second component: start and end time of subtitle
                t_info_seg = laudi.split(" ")
                print(t_info_seg)
                t_start_str = self.timefmt_sec_2_hr_min_sec(t_info_seg[-1].strip()[:-1])
                t_end_str = self.timefmt_sec_2_hr_min_sec(t_info_seg[-3].strip()[:-1])
                print(t_start_str, t_end_str)
                fp.write(t_start_str + " --> " + t_end_str + "\n")
                # third and forth component: subtitle text, followed by a blank line
                fp.write(ltrns.strip() + "\n\n")
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
    if len(srtG.trnsLines) != len(srtG.audiLines):
        print(f"{target_code}: the two files do not have the same length !")
        print("exit !")
        exit()

    print(f"{target_code}: srt generation ready !")
    srtG.genSrt()
    print(f"{target_code}: srt generation done !")
    exit()

