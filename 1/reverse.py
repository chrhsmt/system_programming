def reverse(s):

  ret = ""
  for i in range(1, len(s) + 1):
    ret = ret + s[-i]
  return ret

orig = raw_input("Type  a  phrease: ")
result = reverse(orig)
print result