"""The file contains most common topics 
    related to Objects
"""
x=1000
print x


list =[1,2,3]
list[2]=8
print list


list2=list
print list2


print list==list2

##Mutable both will change! 
list2[1]=50
print list
print list2


import time 
t=time.ctime()
print t

##Using global 
num=0
def get_num():
    print num 

def set_num(n):
    global num  ## This very important 
    num=n

get_num()
set_num(10)
get_num()

