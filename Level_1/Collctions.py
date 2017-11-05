"""This file contains basics fundamentals of Collections """

##Tuples
t=("str",1,4)
print t
print t[1]
for i in t:
    print i 


#Find elements 
t=(1,2,3,4,5,"str",2,"st")
print 2 in t
print 33 not in t
print 33 in t 


#Length 
str="this string length is some numbers"
print len(str)


#Join 

list ="___".join(["str1","str2","str3"])
print list


#Partition 
Str="gothentest".partition("then")
print Str


#Format 
str3="this is {0} and {1}".format("Me","You")
print str3


