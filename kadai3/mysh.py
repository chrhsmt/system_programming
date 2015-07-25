# -*- coding: utf-8 -*-

import sys
import os
import re
import subprocess

histories = []

def history(str=None):
    for index, line in enumerate(histories):
        sys.stdout.write("%2d %s\n" % (index, line))

pattern = re.compile(r'\~') 
inner_func = {
    "cd": os.chdir,
    "exit": sys.exit,
    "history": history
}

while(True): 
    print "\nmysh> ",
    line = sys.stdin.readline().strip()
    if (len(line) == 0):
        continue

    commands = line.split()
    command = commands[0]
    if (inner_func.has_key(command)):
        temp_arg = ""
        if (len(commands) > 1):
            temp_arg = commands[1]
        if ("/" in temp_arg):
            temp_arg = os.getcwd() + "/" + temp_arg
        temp_arg = re.sub(pattern, os.environ['HOME'], temp_arg)
        histories.append(line)
        inner_func[command](temp_arg)
    else:
        try:
            ret = subprocess.call(line, shell=True)
            if (ret == 0):
                histories.append(line)
        except Exception as (errorno, e):
            print e, commands
