def add(a, b):

    for i in range(0, b):
        a = a + 1
    return a


assert add(4, 5) == 9
assert add(5, 15) == 20
assert add(10, 14) == 24
assert add(14, 10) == 24


def add2(a, b):
    while (b != 0):
        temp = a & b
        a = a ^ b
        b = temp << 1
        print(temp, ' - ', a, ' - ', b)
    return a


assert add2(4, 5) == 9
assert add2(5, 15) == 20
assert add2(10, 14) == 24
assert add2(14, 10) == 24
