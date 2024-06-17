#!/usr/bin/python3
import os
import sys
import re


currdir = os.getcwd()
print('current directory: %s' % currdir)


if not len(sys.argv) == 4:
    print('missing videos, exlist, and rejection list argument !')
    print('Usage:')
    print('    python3    1.2.b_gen_download_from_vid_exl_rjl.py \\')
    print('               videos    \\')
    print('               ex_list.txt    \\')
    print('               rejection_list.txt')
    print('\n\n')
    print('error exit()')
    print('\n\n')
    exit()


videos_fname = sys.argv[1]
exlist_fname = sys.argv[2]
rjlist_fname = sys.argv[3]


print('read in the html source of the webpage')
with open(videos_fname, 'r') as fp:
    vtext = fp.read()
fp.close()

print('\n\n')


print('refetch the list of existing audio files')
with open(exlist_fname, 'r') as fp:
    ex_list = fp.readlines()
fp.close()
ex_list = [ _.strip() for _ in ex_list if len(_.strip()) ]
print('existing list contains %d' % len(ex_list))

print('\n\n')


with open(rjlist_fname, 'r') as fp:
    rj_list = fp.readlines()
fp.close()
rj_list = [ _.strip() for _ in rj_list if len(_.strip()) ]
print('rejection list contains %d' % len(rj_list))

print('\n\n')


print('use regular expression to find all the occurance of video')
print('by the youtube code pattern')
_list = re.findall( r'watch\?v=(...........)', vtext)
print('completed list contains %d' % len(_list))

print('\n\n')


print('for newly found youtube videos in webpage html but')
print('not yet in the list of audio files, we identify them')
print('and pack them into \"needed_list\"')
needed_list =  [_ for _ in _list if _ not in ex_list and _ not in rj_list ]
needed_list = list(set(needed_list))
N = len(needed_list)
print('total count of new recording contents: %d' % N)

print('\n\n')


print('generate download script')
cnt = 1
if not os.path.isfile('download.sh'):
    with open('download.sh', 'w') as fp:
        fp.write('#!/bin/bash\n')
        for needed_code in needed_list:
            fp.write('echo ; echo ; date ; ')
            fp.write('echo ; echo ; echo %d / %d ; ' % (cnt, N))
            fp.write('echo ; echo $(pwd) ; echo ; yt-dlp -x --audio-format mp3 ')
            fp.write('https://youtube.com/watch?v=%s\n' % needed_code)
            cnt += 1
    fp.close()
else:
    print('download.sh is already found ! error exit !')
    exit()


print('done !')


