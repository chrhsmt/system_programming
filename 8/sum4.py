def sum4(array):
    if (not isinstance(array, list)):
        raise Exception("argument type is invalid")
    sum = 0
    skip = False
    for n in array:
        if (skip):
            skip = False
            continue
        else:
            sum += n
        if (n == 4):
            skip = True
    return sum

print sum4([1, 2])
print sum4([3, 4])
print sum4([4, 5, 6])
print sum4([4, 9, 4, 9, 4, 9])
print sum4([])