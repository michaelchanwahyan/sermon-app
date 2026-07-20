import os
import sys
import math

if sys.argc > 1:
    code_ = sys.argv[1]
else:
    exit()

code_ = int(code_)
code_parent_ = math.floor(code_ / 1000)

cmd_str = 'wget -O ./church.com.hk.html/' + str(code_) + '.html"https://www.church.com.hk/acms/content.asp?site=cdc&op=show&type=product&code=' + str(code_) + '&layout=sermon"'
_ = os.system(cmd_str)
cmd_str = 'wget -O ' + str(code_) + '.mp3 https://www.church.com.hk/ftp/mp3/' + str(code_parent_) + '/' + str(code_) + '.mp3'
_ = os.system(cmd_str)

