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


         
       