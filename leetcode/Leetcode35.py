#  Leetcode 35: Search Insert Position | Binary Search Optimization - Part 48

#? Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


def searchInsert(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    lb = n
    
    while low <= high:
        mid = (high+low) // 2
        if nums[mid] >= target:
            lb = mid
            high  = mid - 1
        else:
            low = mid + 1

    return lb

nums = [1,3,5,6,7,9,99,100]
target = 8
result = searchInsert(nums, target)
print(result)  # Output: 5

# time complexity: log(n) base 2
# space complexity: O(1)

# this is the optimized version of binary search to find the insert position of target in a sorted array.

# and the approach is similar to lower bound implementation of binary search.