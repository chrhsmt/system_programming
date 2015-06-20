# -*- coding: utf-8 -*-

import sys
import re

try:
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'rU')
    else: 
        f = sys.stdin
except IOError as (errorno, strerror):
    print "Oops.. input not found [no. {0},] [{1}]".format(errorno, strerror)
    sys.exit()

all = f.readlines()

words = {}

for line in all:
    for w in line.split(" "): 
        w = re.sub(r',|\.|"|\?', "", w.lower()).strip()
        if len(w) == 0:
            continue
        elif words.has_key(w):
            words[w] += 1
        else: 
            words[w] = 1

i = 0
for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True):
    if i == 20:
        break
    print k, ":", v
    i += 1
f.close()