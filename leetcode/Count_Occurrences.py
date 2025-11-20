# Count Occurrences in Sorted Array | Binary Search Approach - Part 51

#? Given a sorted array and a target value, count the number of occurrences of the target in the array using binary search.

# this is the brute force approach
# as in this case time complexity will be O(n) and space complexity will be O(1) so interviewers will not prefer this approach....

# def count_occurrences(nums, target):
#     first = -1
#     last = -1
#     for i in range(len(nums)):
#         if nums[i] == target:
#             if first == -1:
#                 first = i
#             last = i
#     if first == -1:
#         return 0
#     return last - first + 1

# nums = [1,2,2,2,3,4,5,5,5,6,7,8]
# target = 2
# result = count_occurrences(nums, target)
# print("The count of occurrences of", target, "in the array is:", result)

#* ************************************
# this is the optimal approach...using binary search

def find_first_occurrence(nums, target):
    
    def lower_bound(nums, target):
        lb = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
                
            else:
                left = mid + 1
                
        return lb
    
    def upper_bound(nums, target):
        n = len(nums)
        ub = n
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target:
                ub = mid
                right = mid - 1
            else:
                left = mid + 1
        return ub

    lb = lower_bound(nums, target)
    if lb == -1:
        return 0
    ub = upper_bound(nums, target)
    return ub - lb

nums = [1,2,2,2,3,4,5,5,5,6,7,8]
target = 2
result = find_first_occurrence(nums, target)
print("The count of occurrences of", target, "in the array is:", result)

# * ************************************
# Time Complexity: O(log n)
# Space Complexity: O(1)

# !*************************************
# LeetCode Link: https://leetcode.com/problems/count-of-occurrences-in-sorted-array