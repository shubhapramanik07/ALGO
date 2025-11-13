# // Implementation of Lower and Upper Bound - Part 47

#? In computer science, the terms "lower bound" and "upper bound" refer to specific positions in a sorted array where a given target value can be inserted while maintaining the sorted order.
#? The lower bound is the position of the first element that is not less than the target
#? The upper bound is the position of the first element that is greater than the target.

nums = [1,2,4,4,5,6,8,9]
target = 4

def lower_Bound(nums,target):
    n = len(nums)
    lb = n 
    # Initialize lower bound to n, which is an invalid index, to handle cases where target is greater than all elements
    low = 0
    high = n-1
    while low <= high:

        mid = (high+low) // 2
        if nums[mid] >= target:
            lb = mid
            high  = mid - 1
        else:
            low = mid + 1

    return lb


xcv = lower_Bound(nums,target)
print(xcv)

# output: 2
# time complexity: log(n) base 2


def upper_Bound(nums,target):
    n = len(nums)
    ub = n 
    # Initialize upper bound to n, which is an invalid index, to handle cases where target is greater than all elements
    low = 0
    high = n-1
    while low <= high:

        mid = (high+low) // 2
        if nums[mid] > target:
            ub = mid
            high  = mid - 1
        else:
            low = mid + 1
    return ub
xcv2 = upper_Bound(nums,target)
print(xcv2)