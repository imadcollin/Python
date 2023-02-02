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


def parrot_trouble(talking, hour):
    if(talking and (hour <7 or hour >20)): 
        return True; 
    else:
        return False; 


assert parrot_trouble(True, 6) == True
assert parrot_trouble(True, 7) == False
assert parrot_trouble(False, 6) == False


def makes10(a, b):
    return ((a == 10 or b==10) or (a+b==10))


assert makes10(9, 10) == True
assert makes10(9, 9) == False
assert makes10(1, 9) == True


def pos_neg(a, b, negative):
    if(negative):
        return (a<0 and b<0)
    else:
        return (a >0 and b < 0) or (a<0 and b>0)
    
assert pos_neg(-4, 5, True) == False
assert pos_neg(-1, 1, False) == True
assert pos_neg(-4, -5, True) == True	