
def divisor(n): 
    x = []
    for i in range(1,n):
        if n %i == 0 :
            x.append(i)
    return x 

assert divisor(6) == [1,2,3]
assert divisor(12) == [1,2,3,4,6]
assert divisor(20) == [1,2,4,5,10]
    
    
def perfect(n): # 6-> 3 2 1 
    if n <=1 :
        return n
    sumOfEl = sum(divisor(n))
    if sumOfEl == n: 
        return True
    return False
    
assert perfect(6)==True
assert perfect(28)==True
assert perfect(7)==False
assert perfect(27)==False
