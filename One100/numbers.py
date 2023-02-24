import math 
def max(a,b):
    if a>b:
        return a
    return b 


assert max(1,3) ==3
assert max(10,11)==11
assert max(13,259)==259

def max2(a,b):
    return a if a>b else b


assert max2(1,3) ==3
assert max2(10,11)==11
assert max2(13,259)==259


def sumOf(a):
    sum= 0 
    for i in range (len(a)): 
        sum = sum + a[i]
    return sum

assert sumOf([1,2,3,4]) == 10
assert sumOf([1,2,3,4,5]) == 15
assert sumOf([4,5]) == 9


def sumOfList(a):
    return sum(a)
      

assert sumOfList([1,2,3,4]) == 10
assert sumOfList([1,2,3,4,5]) == 15
assert sumOfList([4,5]) == 9

def avg(a): 
    sumOfNum = sum(a)
    return sumOfNum/(int)(len(a))

assert avg([1,2,3])==2
assert avg([2,4,6,8])==5
assert avg({5,5,5,5,5}) ==5