def string_times(str, n):
    x= ""
    for i in range(n): 
        x= x+str;
    return x

assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'


def front_times(str, n):      
    x= str[:3]
    temp =""
    for i in range(n): 
        temp+= x; 
    return temp


assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'