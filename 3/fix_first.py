# -*- coding: utf-8 -*-

def fix_first(s):
  first = s[0]
  ret = first + s.replace(first, "*")[1:]
  return ret

print fix_first("babble")
print fix_first("google")
print fix_first("apple")
print fix_first("orange")