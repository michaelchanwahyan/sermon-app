#!/usr/bin/python3
import os
import re
import pathlib


def ytcode_retrieval(infilename):
    if '.mp3' not in infilename and '.txt' not in infilename and '.srt' not in infilename and '.whisper.log' not in infilename:
        print('non txt non srt file name input: ', infilename)
        return ''
    try:
        #yt_pos = re.search('[A-Za-z0-9_-]'*11, infilename).span(0)
        #if yt_pos[0] != 0 and infilename[yt_pos[0]-1] == '[':
        #    # confirm to be new yt-dlp command output filename format
        #    return infilename[yt_pos[0]:yt_pos[1]]
        #elif yt_pos[0] != 0 and infilename[yt_pos[1]+1] == '.':
        #    # confirm to be old youtube-dl command output filename format
        #    return infilename[yt_pos[0]+1:yt_pos[1]+1]
        #else:
        #    return infilename[yt_pos[0]:yt_pos[1]]
        ytc = re.search('[A-Za-z0-9_-]'*11, infilename[::-1]).group()
        ytc = ytc[::-1]
        return ytc
    except:
        print('ytcode pattern search fail for: ', infilename)
        return ''


with open('transcription_server_ip.txt', 'r') as fp:
    transcription_server_ip = fp.read()
transcription_server_ip = transcription_server_ip.strip()
 
with open('PROJECT_LIST', 'r') as fp:
    PROJECT_LIST = [ _.strip() for _ in fp.readlines() if len(_) ]

transfer_script_str = ''
for PROJECT in PROJECT_LIST:
    print('on PROJECT :', PROJECT)
    if  PROJECT == 'DSCCC' or \
        PROJECT == 'HKBC' :
        print(f'skipped {PROJECT}!')
        continue
    # audio file list out
    proj_mp3_dir = str(pathlib.Path.home()) + '/TPPHC/SERMON/' + PROJECT + '/'
    mp3_list = os.listdir(proj_mp3_dir)
    mp3_list = [ ytcode_retrieval(_) for _ in mp3_list ]
    mp3_list = [ _ for _ in mp3_list if len(_) ]
    # srt transcribed file list out
    proj_srt_dir = '../whisper/' + PROJECT + '/'
    srt_list = os.listdir(proj_srt_dir)
    srt_list = [ ytcode_retrieval(_) for _ in srt_list ]
    srt_list = [ _ for _ in srt_list if len(_) ]
    fcnt = 0
    for ytcode in mp3_list:
        if ytcode not in srt_list:
            fcnt += 1
            # print(f'{fcnt}: find untranscribed file in project {PROJECT}: {ytcode}')
            cmdstr = f'scp -p {proj_mp3_dir}*{ytcode}*.mp3 {transcription_server_ip}:{proj_mp3_dir}'
            print(cmdstr)
            transfer_script_str += cmdstr + '\n'

with open('transfer.sh', 'w') as fp:
    fp.write(transfer_script_str)

