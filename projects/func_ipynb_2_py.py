import json
import sys
path = sys.argv[1] # 'michael-1.ipynb'

with open(path, encoding="utf-8") as f:
    # Force insert executor for simpler code
    injection = """
from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err


"""
    js = json.loads(f.read())
    cells = js['cells']

outpath = path.replace(".ipynb",".py")
with open(outpath, "w", encoding="utf-8") as f:
    f.write('#!/usr/local/bin/python3\n\n\n')
    f.write(injection)
    for cell in cells:
        source = "".join(cell['source'])
        if source.strip().startswith("%%bash"):
            # Low level way to obtain the actual command(s)
            # Could handle spaces and line breaks before "%%bash" keyword
            command = source
            target = "%%bash"
            while target:
                if command[0] == target[0]:
                    target = target[1:]
                command = command[1:]
            source = "command='''{command}'''".format(command=command)
            source += "\nou,er = execute_commands(command)"
        elif source.strip().startswith("%matplotlib inline"):
            # avoid inline matplotlib enablling by commenting out
            source = "#" + source

        f.write(source+"\n\n\n") if cell['cell_type'] == "code" else f.write("\n'''"+source+"'''\n\n\n")

with open(outpath, "r", encoding="utf-8") as f:
    pass
    # print(f.read())
