from math import ceil


def ferToCel(n):
    if n < 0:
        return -1
    else:
        return ((n - 32) * 5) / 9

assert ferToCel(96.8) == 36.0
assert ferToCel(54) == 12.222222222222221


def celToFer(n):
    if n < 0:
        return -1
    else:
        return round((n - 32) * 5) / 9


assert celToFer(98.6) == 37
