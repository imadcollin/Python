def prime(n):
    x = []
    l = int(len(n))  # 1 2 3 4
    for i in range(l):
        if (isPrime(n[i])):  # 1 4
            x.append(n[i])
    return x


def isPrime(a):
    if a == 0:
        return False

    for i in range(a):
        if (i > 1 and i != a):
            if (a % i == 0):
                return False
    return True


assert prime([2, 3, 4, 5, 6, 7, 8]) == [2, 3, 5, 7]

assert isPrime(4) == False
assert isPrime(6) == False
assert isPrime(16) == False
assert isPrime(5) == True
assert isPrime(2) == True
assert isPrime(3) == True
