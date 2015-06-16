# -*- coding: utf-8 -*-

import re
def not_bad(s):
  return re.sub(r'not.*bad', "good", s)

print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")
