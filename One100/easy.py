import math 
def divission(a,b):
    return a//b


assert divission(9,2) ==4 
assert divission(17,5) ==3 
assert divission(20,6) ==3 


def divission_2(a,b):
    return math.floor(a/b)


assert divission_2(9,2) ==4 
assert divission_2(17,5) ==3 
assert divission_2(20,6) ==3 


def power(a,b): 
    return math.pow(a,b);

assert power(2,2)==4
assert power(2,3)==8
assert power(5,2)==25
assert power(5,5)==3125



def powerOf(a,b):
    sum= b 
    lo=1
    if(b ==2):
        return a*a; 
    for i in range (b):  
        sum = a*lo;
        lo=sum
    return sum;

assert powerOf(2,2)==4
assert powerOf(2,3)==8
assert powerOf(4,2)==16
assert powerOf(5,5)==3125



def powerOfB(a,b):
    return a**b;

assert powerOfB(2,2)==4
assert powerOfB(2,3)==8
assert powerOfB(4,2)==16
assert powerOfB(5,5)==3125


def swap(a,b): 
    temp = a;
    a=b
    b=temp 
    print(a,b)
    
def swapRe(a,b):   
    a,b= b,a
    print(a,b)

def swap3(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

swap(1,2)
swapRe(1,2)
swap3(1,2)
print('-----')
swap(4,5)
swapRe(4,5)
swap3(4,5)
print('-----')

swap(6,7)
swapRe(6,7)
swap3(6,7)
print('-----')