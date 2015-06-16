def remove_adjacent(li):
  result = []
  last = None
  for x in li:
    if x != last:
      result.append(x)
      last = x
  return result

print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])
print remove_adjacent([])
