#!/usr/bin/python

def fb(n):
  ret = ""
  fizz = ["Fizz", "", ""]
  buzz = ["Buzz", "", "", "", ""]
  return fizz[n % 3] + buzz[n % 5]

i = 1
while i <= 20:
  print i , fb(i)
  i += 1