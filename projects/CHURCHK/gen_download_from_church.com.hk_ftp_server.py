#!/usr/bin/python3
import os
import sys
import re



currdir = os.getcwd()
print("current directory: %s" % currdir)


if not len(sys.argv) == 3:
    print("missing videos, exlist argument !")
    print("Usage:")
    print("    python3    gen_download_from_church.com.hk_ftp_server.py \\")
    print("               videos    \\")
    print("               ex_list.txt")
    print("\n\n")
    print("error exit()")
    print("\n\n")
    exit()


videos_fname = sys.argv[1]
exlist_fname = sys.argv[2]


print('read in the html source of the webpage')
with open(videos_fname, 'r') as fp:
    vtext = fp.read()

print('\n\n')


print('refetch the list of existing audio files')
with open(exlist_fname, 'r') as fp:
    ex_list = fp.readlines()
ex_list = [ _.strip() for _ in ex_list if len(_.strip()) ]
print('existing list contains %d' % len(ex_list))

print('\n\n')


# church.com.hk topmostrecent page source structure looks like
# <a href="content.asp?site=cdc&op=show&type=product&code=031343&layout=sermon" target="_blank"><span class="sermon-title">怕甚麼？靠甚麼？再思彌賽亞的來臨</span></a><br>
# while for each sermon page the sermon audio mp3 ftp link looks like
# https://www.church.com.hk/ftp/mp3/10000/010001.mp3
# https://www.church.com.hk/ftp/mp3/30000/030348.mp3
# https://www.church.com.hk/ftp/mp3/31000/031348.mp3


print("use regular expression to find all the occurance of sermon")
print("by church.com.hk ftp server mp3 url pattern")
_list = re.findall(r"code=......&layout=sermon", vtext)
print("completed list contains %d" % len(_list))

print("\n\n")


print("for newly found church.com.hk ftp mp3 in webpage html but")
print("not yet in the list of audio files, we identify them")
print("and pack them into \"needed_list\"")
needed_list = [ _.replace("code=", "").replace("&layout=sermon", "") \
        for _ in _list \
        if _.replace("code=", "").replace("&layout=sermon", "") not in ex_list ]
needed_list = list(set(needed_list))
needed_list.sort()
N = len(needed_list)
print("total count of new recording contents: %d" % N)

print("\n\n")


print("generate download script")
cnt = 1
if not os.path.isfile("download.sh"):
    with open("download.sh", "w") as fp:
        fp.write("#!/bin/bash\n")
        for needed_code in needed_list:
            fp.write("echo ; echo ; date ; ")
            fp.write("echo ; echo ; echo %d / %d ; " % (cnt, N))
            fp.write("echo ; echo $(pwd) ; echo ; ")
            sermon_src_webpage_url = "https://www.church.com.hk/acms/content.asp?"
            sermon_src_webpage_url += "site=cdc&op=show&type=product&code="
            sermon_src_webpage_url += needed_code
            sermon_src_webpage_url += "&layout=sermon"
            fp.write(\
                    "wget -O ./church.com.hk.html/" \
                    + needed_code + ".html" \
                    + " \"" \
                    + sermon_src_webpage_url \
                    + "\"\n")
            sermon_mp3_ftp_url = "https://www.church.com.hk/ftp/mp3/"
            ftp_foldername = str(int((int(needed_code)-1) / 1000) * 1000)
            sermon_mp3_ftp_url += ftp_foldername + "/"
            sermon_mp3_ftp_url += needed_code + ".mp3"
            fp.write(\
                    "wget -O " \
                    + needed_code + ".mp3" \
                    + " "
                    + sermon_mp3_ftp_url \
                    + "\n")
            cnt += 1
else:
    print('download.sh is already found ! error exit !')
    exit()


print('done !')


