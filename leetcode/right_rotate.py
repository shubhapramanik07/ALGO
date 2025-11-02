# nums = [4,1,8,7,6,5]
# n = len(nums)
# nums[:] = [nums[n-1]] + nums[0:-1]
# print(nums)

# use this method instead of slicing 

nums = [4,1,8,7,6,5]
n = len(nums)
temp = nums[n-1]
for i in range(n-1,0,-1):
    nums[i] = nums[i-1]
nums[0] = temp
print(nums)

# time complexity: O(n-1) = O(n)
# space complexity: O(1)
