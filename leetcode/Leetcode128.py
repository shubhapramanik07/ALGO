# Leetcode 128: Longest Consecutive Sequence 

# nums = [1,3,2,101,69,70,100,6,5,4]
# n = len(nums)
# maxi = 0

# for i in range(0,n):
#     temp = nums[i]
#     l = 1
#     while temp+1 in nums:
#         l+=1
#         temp += 1
            
#         maxi = max(l,maxi)

# print(maxi)
# this is brute force approach
# time complexity: O(n^2) where n is the number of elements in the array
# space complexity: O(1) as we are using only constant space

#* /****************************************/
#? optimal solution using hashing
# nums = [1,3,2,101,69,70,100,6,5,4]
# last_smaller = float("-inf")
# count = 0
# maxi = 0
# n = len(nums)
# nums.sort()
# # for this time_complexity O(nlogn)

# for i in range(n):
#     num = nums[i]
#     if num-1 == last_smaller:
#         count += 1
#         last_smaller = num
#     elif num != last_smaller:
#         count = 1
#         last_smaller = num
#     maxi = max(count,maxi)

# print(maxi)

# overall time complexity: O(nlogn + n) where n is the number of elements in the array
# space complexity: O(1) as we are using only constant space

#* /****************************************/
# aur better solution using set data set
nums = [1,2,101,2,70,100,7,6,5,4]
count = 0
maxi = 0
num_set = set()
for i in range(len(nums)):
    num_set.add(nums[i])

for num  in num_set:
    if num - 1 not in num_set:  
        lowest = num
        count = 1
        while lowest + 1 in num_set:
            count += 1
            lowest += 1

            
        maxi = max(count,maxi)
print(maxi)

# time complexity: O(n+n+n) = O(n) where first n is for creating the set, second n is for iterating through the set, and third n is for the while loop in the worst case scenario where all elements are consecutive.
# space complexity: O(n) where n is the number of elements in the array due to the use of the set to store unique elements.