#  Leetcode 53: Find the Maximum Subarray Sum
#* /****************************************/

# nums = [8,7,-2,4,-13,6,-9,7,2]
# maxi = float('-inf')

# for i in range(len(nums)):
#     total = 0
#     for j in range(len(nums)):
#         total = total + nums[j]
#         maxi = max(maxi,total)

# print(maxi)
# print("Brute Force Approach")


# time complexity is O(n^2) because of the nested loops where for each element we are checking all the other elements.
# space complexity is O(1) because we are not using any extra space that grows with input size.

#* /****************************************/

#? optimal solution using Kadane's Algorithm

#* /****************************************/

nums = [8,7,-2,4,-13,6,-9,7,2]
maxi = float('-inf')
current_sum = 0

for i in range(len(nums)):
    current_sum += nums[i]
    maxi = max(maxi, current_sum)
    if current_sum < 0:
        current_sum = 0

print(maxi)