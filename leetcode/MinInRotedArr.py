# - Find Minimum in Rotated Sorted Array | Binary Search - Part 54
# ? Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# ? Given the sorted rotated array nums of unique elements, return the minimum element of this array


def find_min_in_rotated_sorted_array(nums):
    n = len(nums)
    mini = float('inf')
    low = 0
    for i in range(n):
        mini = min(mini, nums[i])
    return mini
nums = [4,5,6,7,0,1,2]
result = find_min_in_rotated_sorted_array(nums)
print(result)  # Output: 0
        # time complexity: O(n)
        # space complexity: O(1)
# this is the brute force approach...time complexity will be O(n) and space complexity will be O(1)
# as we are traversing the whole array to find the minimum element.
# an optimal approach will be using binary search...time complexity will be O(log n) and space complexity will be O(1)
def find_min_in_rotated_sorted_array_optimal(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float('inf')
    while low <= high:
        mid = (low + high) // 2
        mini = min(mini, nums[mid])
        if nums[mid] >= nums[low]:
            mini = min(mini, nums[low])
            low = mid + 1
        else:
            mini = min(mini, nums[high])
            high = mid - 1
    return mini
nums = [4,5,6,0,1,2,3]
result = find_min_in_rotated_sorted_array_optimal(nums)
print(result)  # Output: 0
        # time complexity: O(log n)
        # space complexity: O(1)