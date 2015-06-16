import sys

if len(sys.argv) > 1:
  f = open(sys.argv[1], 'rU')
else: 
  f = sys.stdin

pat = "but"
for line in f:
  for w in line.split(" "):
    if pat == w.lower():
      line = line.replace(w, "***" + w + "***")
      print line.strip() 
      break;
f.close()