"""
This file is first program with Python 
"""
print "Hello world "

#If statments 
if True:
    print "True"
else:
    print "False"


#If Else
x=10
if x<10: 
    print "less"
else:
    print "greater"


#If else in one
if x<10:
    print "less"
elif x==10:
    print "equal"
    
#For statment
myList=[1,2,3,4]
print myList # OK! 

for i in myList:
    print 'i=' , i  ## Ops!!

#While statment 
while True: 
    if myList.count(1)==2:
        print "Count(1) detected"
        break
    print "Nothing to show "
    break

#String 
str= "This is a string!"
print str

##string concat 
str2= " String 2 "
print str+str2

#Dictionalry 
dic={1:"one",2:"two"}
print dic    

for i in dic:
    print 'i=' , i 

