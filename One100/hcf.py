def hcf(a,b): 
    s = 0 
    if a<b:
        s = a 
    else : 
        s = b 
    
    while(True): 
        if (a%s ==0 and b%s==0):
            return s 
        s= s-1

assert hcf(4,6)== 2  
assert hcf(5,7)== 1  
assert hcf(9,3)== 3