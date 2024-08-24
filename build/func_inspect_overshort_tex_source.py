#!/usr/local/bin/python3

import os
import re

for PROJFOLDER in [ PROJ for PROJ in os.listdir("./") if "." not in PROJ and "_" not in PROJ ]:
    for file in os.listdir(PROJFOLDER):
        if file.endswith(".tex"):
            print(PROJFOLDER + "/" + file)
            with open("./KFC/sermon_KFC_2020-present.tex", "r") as fp:
                lines = [ _.strip() for _ in fp.readlines() ]
            fp.close()
            n = 0
            n_prev = -9999
            n_curr = -9999
            hashline_curr = ''
            for li, line in enumerate(lines):
                n += 1
                if line == "\\section{}":
                    hashline_prev = hashline_curr
                    hashline_curr = lines[li+1]
                    n_prev = n_curr
                    n_curr = n
                    if n_curr - n_prev < 100:
                        print(hashline_prev, n_curr - n_prev)

