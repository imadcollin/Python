def great(a,b,c):
    x=0
    if a > b :
       x=a
    if a> c:
        x=a  
    if b > c:
        x=b
    else:
        x= c 
    return x 

assert great(1,2,3) ==3  
assert great(3,5,6) ==6  
assert great(1,8,3) ==8  

def greatest(a,b,c):
    
    if a > b and a > c:
        return a 
    if b > a and b > c : 
        return b 
    if c > a and c > b : 
        return c 


assert greatest(1,2,3) ==3
assert greatest(3,5,6) ==6
assert greatest(1,8,3) ==8
       