#!/usr/bin/python3
import os
import re
import pathlib


def ytcode_retrieval(infilename):
    if '.mp3' not in infilename and '.txt' not in infilename and '.srt' not in infilename and '.whisper.log' not in infilename:
        print('non txt non srt file name input: ', infilename)
        return ''
    try:
        # the following regex search approach applys to whisper folder
        # which contains
        #   1. xxxxxxxxxxx.whisper.log
        #   2. xxxxxxxxxxx.srt
        #   3. README.md
        #   4. i j ij ijk ii jj ... etc.
        # in order to retrieve the desired xxxxxxxxxxx pattern,
        # file names are reversed first, followed by regex search
        # of consecutive A-Za-z0-9_- pattern search.
        # note: '.' is not included so that reversed '.whisper.log'
        # and '.srt' pattern are not involved.  'README.md' is also
        # excluded.  i j ... files are too short to be included
        # it is expected that the output srt_list would have each
        # ytc doubled because a pair of *.whisper.log and *.srt
        # files are associated to each ytc.
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

