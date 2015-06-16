def match_ends(li):
  # resultList = filter(lambda w: 
  #   (len(w) >=2 and w[0] == w[-1]), li)
  # return len(resultList)
  return len([x for x in li if len(x) >= 2 and x[0] == x[-1]])

print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])
