import os
import sys
# ----------------------------------------------------------------------
# description:
# python3 convert_srt2txt.py <sermon_group_directory>
#     from /whisper/<sermon_group_directory>/*.srt
#     generate the corresponding *.txt files and stored
#     to /data/<sermon_group_directory>/
# ----------------------------------------------------------------------

if len(sys.argv) == 1:
    print("sermon group directory is not specified !")
    print("read file usage description !")
    exit()
sermon_group_path_str = sys.argv[1]

filelist = os.listdir(sermon_group_path_str)
print(f"total file count in {sermon_group_path_str}: {len(filelist)}")

srtfilelist = [ filename for filename in filelist if filename[-4:] == '.srt' ]
srtfilelist.sort()
whisperlogfilelist = [ filename for filename in filelist if filename[-4:] == '.log' ]
whisperlogfilelist.sort()
print(f"total .srt file count in {sermon_group_path_str}: {len(srtfilelist)}")
print(f"total .whisper.log file count in {sermon_group_path_str}: {len(whisperlogfilelist)}")

for srtfilename in srtfilelist:
    pathfilename = "./" + sermon_group_path_str + "/" + srtfilename
    try:
        with open (pathfilename, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()
        fp.close()
    except:
        fp.close()
        print(f"exception caught at file {pathfilename}")
    dest_pathfilename = "../data/" + sermon_group_path_str + "/" + srtfilename[:-3] + "txt"
    with open (dest_pathfilename, 'w', encoding='utf-8') as fp:
        for line_ in lines[2::4]:
            fp.write(line_.strip() + "。\n")
    fp.close()

