def first_last6(nums):
    return nums[0] == 6 or nums[-1]== 6


assert first_last6([1, 2, 6]) == True
assert first_last6([6, 1, 2, 3]) == True
assert first_last6([13, 6, 1, 2, 3]) == False


def common_end(a, b):
    return a[0] ==b[0] or a[-1]== b[-1]


assert common_end([1, 2, 3], [7, 3]) ==True
assert common_end([1, 2, 3], [7, 3, 2]) == False
assert common_end([1, 2, 3], [1, 3]) ==True



def sum3(nums):
    sum= 0;
    for i in range (len(nums)): 
        sum = sum+nums[i]
    return sum

assert sum3([1, 2, 3]) == 6
assert sum3([5, 11, 2]) == 18
assert sum3([7, 0, 0]) == 7


def rotate_left3(nums):
    l= (len(nums)-1)
    arr = [0]
    arr[0]=nums[l] 
    for i in range (len(nums)):
        if(i !=0): 
            arr.append(nums[i])
    arr[nums[l-1] ] = nums[0]
    return arr


def rotate_right(nums): 
    nums.insert(0, nums.pop())    
    return nums

assert rotate_right([1,2,3]) == [3,1,2]

assert rotate_left3([1,2,3]) == [3,2,1]


def reverse3(nums):
    arr = [1,1,1]
    for i in range (len(nums)): 
        arr[i] = nums.pop()
    return arr

assert reverse3([1,2,3]) == [3,2,1]
assert reverse3([1, 2, 3]) == [3, 2, 1]
assert reverse3([5, 11, 9]) == [9, 11, 5]
assert reverse3([7, 0, 0]) ==[0, 0, 7]


def max_end3(nums):
    x= 0
    if nums[0] > nums[(len(nums)-1)]: 
        x = nums[0]
    else:
        x= nums[(len(nums)-1)]

    for i in range (len(nums)): 
        nums[i] = x 
    return nums 

def max_2(nums): 
    x= max(nums[0], nums[2])
    for i in range (len(nums)):
        nums[i] = x; 
    return nums

assert max_end3([1, 2, 3]) == [3, 3, 3]
assert max_end3([11, 5, 9]) == [11, 11, 11]
assert max_end3([2, 11, 3]) ==[3, 3, 3]


assert max_2([1, 2, 3]) == [3, 3, 3]
assert max_2([11, 5, 9]) == [11, 11, 11]
assert max_2([2, 11, 3]) ==[3, 3, 3]


def sum2(nums):
    return nums[0] + nums[1]

assert sum2([1, 2, 3]) == 3
assert sum2([1, 1]) == 2
assert sum2([1, 1, 1, 1]) ==2


def middle_way(a, b):
    arr = [0,0]  
    arr[0] =a[1]
    arr[1] =b[1]
    return arr

assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]