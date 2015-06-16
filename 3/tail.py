import sys

if len(sys.argv) > 1:
  f = open(sys.argv[1], 'rU')
else: 
  f = sys.stdin

all = f.readlines()
all.reverse()
for line in all:
  print line.strip()
f.close()