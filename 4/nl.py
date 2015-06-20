# -*- coding: utf-8 -*-

import sys

try:
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'rU')
    else: 
        f = sys.stdin
except IOError as (errorno, strerror):
    print "Oops.. input not found [no. {0},] [{1}]".format(errorno, strerror)
    sys.exit()

all = f.readlines()
degree = len(str(len(all)))
for i, line in enumerate(all):
    print >>sys.stdout, " " * (degree - 1 - (i/10)), i, " ", line.rstrip()

f.close()