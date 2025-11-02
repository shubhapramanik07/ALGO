# nums = [0, 1, 0, 3, 12, 0, 7]
# arr = []
# n = len(nums)
# for i in range(n):
#     if nums[i] != 0:
#         arr.append(nums[i])

# # nums[:] = arr + [0] * (n - len(arr))
# len_arr = len(arr)
# for i in range(len_arr):
#     nums[i] = arr[i]

# for i in range(len_arr, n):
#     nums[i] = 0

# print(nums)

# ? ***************************************
# time complexity: O(n+n) = O(n) coz we are traversing the array two times while appending non-zero elements to a new array and then filling the original array with non-zero elements followed by zeros
# space complexity: O(n) coz we are using an extra array to store non-zero elements in the worst case when there are no zeros in the original array

# ? ***************************************
# another method to move all zeros to the end of the array in place without using extra space.................
# Initialize array and get its length
nums = [0, 1, 0, 3, 12, 0, 7]
n = len(nums)

# Pointer i tracks position for next non-zero element
i = 0

# Traverse through the array
for j in range(n):
    # If current element is non-zero, swap it to position i
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1

print(nums)

# ? ***************************************
# TIME COMPLEXITY EXPLANATION:
# - The outer for loop runs exactly n times (from 0 to n-1)
# - Inside the loop, we perform constant time operations:
#   * Comparison: nums[j] != 0 is O(1)
#   * Swap operation: nums[i], nums[j] = nums[j], nums[i] is O(1)
#   * Increment: i += 1 is O(1)
# - Since we iterate n times and each iteration does O(1) work
# - Total Time Complexity: O(n) where n is the length of the array
# ? ***************************************

# SPACE COMPLEXITY EXPLANATION:
# - We are modifying the array in-place (no extra data structures)
# - Only using two integer variables: i and j
# - These variables take constant space O(1) regardless of input size
# - No additional arrays, lists, or data structures are created
# - Total Space Complexity: O(1) - constant/auxiliary space only
# ? ***************************************

# 
# 
# 
# 

# nums = [0,1,0,2,4,3,0,0,3,5,1]
# i = -1
# j = i + 1
# while j < len(nums):
#     if nums[j] != 0:
#         i = i + 1
#         nums[i],nums[j] = nums[j],nums[i]
#     j = j + 1
# print(nums)