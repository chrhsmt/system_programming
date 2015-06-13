def first_last(s): 
  if len(s) <= 1:
    ret = ""
  else:
    ret = s2 = s1[:2] + s1[-2:] 
  return ret

s1 = "spring"
print first_last(s1)

s1 = "hello"
print first_last(s1)

s1 = "a"
print first_last(s1)

s1 = "abc"
print first_last(s1)
