def first_last6(nums):
    return nums[0] == 6 or nums[-1]== 6


assert first_last6([1, 2, 6]) == True
assert first_last6([6, 1, 2, 3]) == True
assert first_last6([13, 6, 1, 2, 3]) == False