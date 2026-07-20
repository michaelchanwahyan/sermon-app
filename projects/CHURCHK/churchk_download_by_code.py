import os
import sys
import math

if len(sys.argv) > 1:
    code_ = sys.argv[1]
else:
    exit()

code_ = int(code_)
code_str = "%06d" % code_
code_parent_ = math.floor(code_ / 1000) * 1000
code_parent_str = str(code_parent_)

cmd_str = 'wget -O ./church.com.hk.html/' + code_str + '.html "https://www.church.com.hk/acms/content.asp?site=cdc&op=show&type=product&code=' + code_str + '&layout=sermon"'
_ = os.system(cmd_str)
cmd_str = 'wget -O ' + code_str + '.mp3 https://www.church.com.hk/ftp/mp3/' + code_parent_str + '/' + code_str + '.mp3'
_ = os.system(cmd_str)

