import os

filelist = os.listdir('JNG')
print(f"total file count in JNG: {len(filelist)}")

srtfilelist = [ filename for filename in filelist if filename[-4:] == '.srt' ]
srtfilelist.sort()
whisperlogfilelist = [ filename for filename in filelist if filename[-4:] == '.log' ]
whisperlogfilelist.sort()
print(f"total .srt file count in JNG: {len(srtfilelist)}")
print(f"total .whisper.log file count in JNG: {len(whisperlogfilelist)}")

for srtfilename in srtfilelist:
    pathfilename = "./JNG/" + srtfilename
    with open (pathfilename, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    fp.close()
    dest_pathfilename = "../data/JNG/" + srtfilename[:-3] + "txt"
    with open (dest_pathfilename, 'w', encoding='utf-8') as fp:
        for line_ in lines[2::4]:
            fp.write(line_.strip() + "。\n")
    fp.close()

