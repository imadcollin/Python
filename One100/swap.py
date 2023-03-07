def swap (a,b):
    temp = a 
    a = b 
    b = temp 
    return [a,b]

assert swap(1,2) == [2,1] 
assert swap(4,5) == [5,4] 
assert swap(8,6) == [6,8] 

def swap2(a,b):
    a = a -b 
    b= a +b 
    a = b-a 
    return [a,b]


assert swap2(1,2) == [2,1]
assert swap2(4,5) == [5,4]
assert swap2(8,6) == [6,8]
