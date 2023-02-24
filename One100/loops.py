def secondLarge(a):
    x=0
    y=0
    z=0 
    w=0
    for i in range (len(a)):
        x=a[i]
        if(x>y):
            y=x 
    for i in range (len(a)):
        z=a[i]
        if(w<z and z<y):
            w=z
    return w 
assert secondLarge([1,2,3,4,5]) == 4
assert secondLarge([4,5,6,7,1])==6
assert secondLarge([4,3,2,2])==3

def secondLarge2(a): 
    x= a[0] 
    y= 0
    for i in range (len(a)):
        if(a[i]>x):
            y=x
            x=a[i]
    return y

assert secondLarge2([1,2,3,4,5]) == 4
assert secondLarge2([4,5,6,7,1])==6
assert secondLarge2([4,3,2,2])==3


