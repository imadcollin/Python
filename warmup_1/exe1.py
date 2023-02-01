### Sleep in example
def sleep_in(weekday, vacation):
    if (weekday & (not vacation)):
        return False
    else:
        return True


def sleep_in_2(weekday, vacation):
    return (not weekday or vacation)


assert sleep_in(True, True) == True
assert sleep_in(False, False) == True
assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True

assert sleep_in_2(True, True) == True
assert sleep_in_2(False, False) == True
assert sleep_in_2(False, False) == True
assert sleep_in_2(True, False) == False
assert sleep_in_2(False, True) == True


def monkey_trouble(a, b):
    return a == b


def monkey_trouble2(a, b):
    if (a and b):
        return True
    if (not a and not b):
        return True
    else:
        return False


assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False

assert monkey_trouble2(True, True) == True
assert monkey_trouble2(False, False) == True
assert monkey_trouble2(True, False) == False