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


#Range
for i in range(10): 
    print i


##Rang start stop stop
for i in range(10,20,2):
    print i  ## i ++2 

#################################################
#List
#################################################

x="there are some birds over there".split()
print x
print x[2]
print x[1]


y=[[1,2,3,4]]*3
print y 


list=[range(1,10)]*3
print list


rev=["ttt","wwww","ggff"]
print rev
rev.sort()
print rev
rev.reverse()
print rev

