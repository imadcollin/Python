def even(n):
    if (n % 2 != 0):
        return False
    return True


assert even(41) == False
assert even(31) == False
assert even(22) == True
assert even(12) == True


def lcm(a, b):
    l = 0
    if a > b:
        l = a
    else:
        l = b
    while (True):
        if (l % a == 0 and l % b == 0):
            return l
        l = l + 1
    return 0


assert lcm(4, 6) == 12
assert lcm(9, 18) == 18
assert lcm(72, 120) == 360
