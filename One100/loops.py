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


def getLargest(a):
    x = a[0] 
    for i in range (len(a)): 
        if(a[i]>x): 
            x=a[i]
    return x
            
def secondLarge2(a): 
    largest= getLargest(a) 
    y= 0
    for i in range (len(a)):
        if(a[i]>y and a[i]<largest):
            y=a[i]
    return y

assert secondLarge2([1,2,3,4,5]) == 4
assert secondLarge2([4,5,6,7,1])==6
assert secondLarge2([4,3,2,2])==3


def sortArr(a):
    for i in range (len(a)):
        for j in range (len(a)):
            if(a[j]>a[i]):
                temp= a[i]
                a[i]=a[j]
                a[j]=temp
    return a

assert sortArr([2,3,1,4]) ==[1,2,3,4]            
assert sortArr([2,3,4,6,1,4]) ==[1,2,3,4,4,6]            
assert sortArr([4,3,2]) ==[2,3,4]            
        
        
def secondLarge3(a):
    x =  sortArr(a)
    return x[(len(x)-2)]

assert secondLarge3([1,2,3,4,5]) == 4
assert secondLarge3([4,5,6,7,1])==6
assert secondLarge3([4,3,2,2])==3


        


