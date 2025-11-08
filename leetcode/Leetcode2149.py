# Leetcode 2149: Rearrange Array Elements by Sign
#* /****************************************/
# Concept:
# Rearrange the array so that positive and negative numbers appear alternately — starting with a positive number — while maintaining their original order.

# Approach:

# Create two lists:

# pos → store positive numbers

# neg → store negative numbers

# Use a loop to fill a new array alternately with elements from pos and neg.

#* /****************************************/
# nums = [3,1,-2,-5,2,-4]
# n = len(nums)
# pos_num = []
# neg_num = []
# num1 = []
# for num in nums:
#     if num>0:
#         pos_num.append(num)
#     else:
#         neg_num.append(num)

# # for i in range(len(pos_num)):
# #     num1.append(pos_num[i])
# #     num1.append(neg_num[i])
# # print(num1)  #slicing the original array to get the rearranged array

# for i in range(0,len(pos_num)):
#     nums[2*i] = pos_num[i]
#     nums[2*i + 1] = neg_num[i]
# print(nums)  #slicing the original array to get the rearranged array



# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(n) where n is the number of elements in the array due to the use of extra space for pos_num and neg_num lists.

#* /****************************************/
#? optimal solution without using extra space
nums = [3,1,-2,-5,2,-4]
N = len(nums)
result = [0]*N
p = 0  # pointer for positive numbers
n = 1  # pointer for negative numbers
for i in range(N):
    if p < N and nums[i] > 0:
        result[p] = nums[i]
        p += 2
    else:
        result[n] = nums[i]
        n += 2
print(result)

# time complexity: O(n) where n is the number of elements in the array
# space complexity: O(n) where n is the number of elements in the array due to the use of extra space for result list. or you can say O(1) if we consider the output array as not part of the space complexity.