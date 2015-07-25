# -*- coding: utf-8 -*-

import sys
import os
import time
import argparse
import re
from tarfile import filemode
import pwd
import grp

parser = argparse.ArgumentParser()
parser.add_argument("path", 
                    metavar="path",
                    nargs="?", 
                    default="",
                    type=str, 
                    help="expect shown directory")
parser.add_argument("-a",
                    action="store_true",
                    default=False)
parser.add_argument("-i",
                    action="store_true",
                    default=False)
parser.add_argument("-l",
                    action="store_true",
                    default=False)

args = parser.parse_args()

pattern = re.compile(r'^\..*$')

try:
    dir_list = os.listdir("./%s" % args.path)
except OSError as (errorno, error):
    sys.exit("python %s: %s: %s" % (sys.argv[0], args.path, error))

if not args.a:
    for src in dir_list[:]:
        if pattern.match(src):
            dir_list.remove(src)
else:
    dir_list = [".", ".."] + dir_list

if args.l:
    for src in dir_list:
        stat = os.stat(args.path + src)
        uname = pwd.getpwuid(stat.st_uid).pw_name
        gname = grp.getgrgid(stat.st_gid).gr_name
        mtime = time.strftime("%m %d %H:%M", time.localtime(stat.st_mtime))
        inode = stat.st_ino
        if args.i:
            print "%s %s  %2s %s  %s %5d  %s %s" % (stat.st_ino, filemode(stat.st_mode), stat.st_nlink, uname, gname, stat.st_size, mtime, src)
        else:
            print "%s  %2s %s  %s %5d  %s %s" % (filemode(stat.st_mode), stat.st_nlink, uname, gname, stat.st_size, mtime, src)
else:
    if args.i:
        print "\t".join([ "%s %s" % (os.stat(args.path + src).st_ino, src) for src in dir_list])
    else:
        print "\t".join(dir_list)