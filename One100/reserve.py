def reverseInt(a):
    x = ''
    if (a <= 9):
        return a
    while (a > 0):
        num = a % 10
        x = x + str(num)
        a = a // 10
    return int(x)


assert reverseInt(43) == 34
assert reverseInt(435) == 534
assert reverseInt(5765) == 5675


def armstrong(a):
    sum = 0
    temp = a
    if temp <= 9:
        return a
    while a > 0:
        num = a % 10
        cube = num * num * num
        sum = sum + cube
        temp = temp // 10
    return sum == a


assert armstrong(153) == True
assert armstrong(370) == True
assert armstrong(1333) == False














