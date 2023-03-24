#Declare 
dict= {'name': 'Alice', 'age': 24}

#Access 
print(dict['name'])
print(dict['age'])

#Uodate 
dict['name'] = 'Bob'
print(dict['name'])

#Clear
del dict['age']
print(dict)

dict2={'name': 'Eva'}
dict2.clear()
print(dict2)