def front_x(x):
  xList = [w for w in x if w.find("x") == 0]
  nonXList = [w for w in x if w[0] != "x"]
  xList.sort()
  nonXList.sort()
  return xList + nonXList

print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])