from array import * 

arr1= array('i', [1,2,3,4,5])


def printArr(arr):
    for i in arr: 
        print(i)


printArr(arr1)

print('#### INSERT #####')
arr1.insert(5,6)
printArr(arr1)

print('#### REMOVE #####')
arr1.remove(6)
printArr(arr1)


print('#### INDEX #####')
arr1.index(5)
printArr(arr1)