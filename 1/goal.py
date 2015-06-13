def goal(coun):
  if count >= 10:
    countStr = "many"
  else:
    countStr = str(count)

  s = "Number of goals: " + countStr
  print s

count = 4
goal(count)
count = 9
goal(count)
count = 10
goal(count)
count = 99
goal(count)
