#Example 
list1 =[1,2,3,'text 1', 'text 2']

print(list1)

#Access
print(list1[0])
print(list1[len(list1)-1])

#Update 
list1[1]='text'; 


#Delete 
del list1[2]

#Iteration 
for x in list1: print(x)

#In 
assert 'text 1' in list1

#Mult
assert [1]*2 == [1,1] 
