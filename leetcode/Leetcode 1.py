# Leetcode 1: Two Sum Problem

# nums = [8,77,21,4,13,6,99,34,2]
# target = 79
# i = 0
# n = len(nums)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if nums[i] + nums[j] == target:
#             print(i,j)    

# time complexity is O(n(n+1)/2) = O(n^2) because of the nested loops where for each element we are checking all the other elements.
# space complexity is O(1) because we are not using any extra space that grows with input size.

# /****************************************/
# optimal solution using hashmap
nums = [8,77,21,4,13,6,99,34,2]
target = 101 
n = len(nums)
num_map = {}
for i in range(n):
    remaining = target - nums[i]
    # if nums[i] in num_map:
    #     print(nums[i],remaining)
    # else:
    #     num_map[i] = 0

    if remaining in num_map:
        print(num_map[remaining],i)
    else:
        num_map[nums[i]] = i

# time complexity is O(n) because we are iterating through the list only once.
# space complexity is O(n) because in the worst case, we may store all n elements in the hashmap.