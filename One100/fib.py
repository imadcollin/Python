def fib(n): 
    if n <=1: return n 
    list = []
    f = 1
    s= 2
    for i in range (2,n): 
        x = f+ s 
        f= s
        s=x 
        list.append(x) 
    return list

assert fib(6) ==[3,5,8,13]

assert fib(13)==[3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

def fibRec(n):
    if (n <=1):
        return n; 
    else:
        return (fibRec(n-1) + fibRec(n-2))
    
assert fibRec(9) ==34
