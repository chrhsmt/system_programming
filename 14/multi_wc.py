# -*- coding: utf-8 -*-

import sys
import urllib
import subprocess
import threading

sum = 0
s1 = s2 = ""

class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.setDaemon(True)
    def run(self):
        global sum, s1, s2
        f = urllib.urlopen(self.url)
        s = f.read()
        p = subprocess.Popen(["wc", "-w"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = p.communicate(s)
        ret = int(out)
        sum += ret
        s1 += str(ret) + " + "
        s2 += "%7d %s\n" % (ret, url.split("/")[-1])
        f.close()

tl = []
for url in sys.argv[1:]:
    wc = MyThread(url)
    wc.start()
    tl.append(wc)

for t in tl:
    t.join()

print "Total : %d = %s" % (sum, s1[:-3])
print s2

