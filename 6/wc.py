#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import os

argc = len(sys.argv)
if argc == 1 and not os.isatty(file.fileno(sys.stdin)):
    f = sys.stdin
elif  argc == 2:
    try:
        f = open(sys.argv[1], 'rU')
    except IOError as (errorno, strerror):
        sys.exit("Oops.. wc: %s: No such file or directory [no. {0},] [{1}]".format(argv[1], errorno, strerror))
else: 
    sys.exit("usage: wc.py [file]")

all = f.readlines()

words = {}

for line in all:
    for w in line.split(" "): 
        w = re.sub(r',|\.|"|\?|-|_|\!|(|)|/', "", w.lower()).strip()
        if len(w) == 0:
            continue
        elif words.has_key(w):
            words[w] += 1
        else: 
            words[w] = 1

print "Number of words: %d" % len(words)

i = 0
for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True):
    if i == 20:
        break
    print k, ":", v
    i += 1
f.close()