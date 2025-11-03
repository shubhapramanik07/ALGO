# Leetcode 485: Max Consecutive Ones

nums = [1,0,1,1,0,1,1,1,0,1,0,0,1]
count = 0
max_count = 0
for i in range(0,len(nums)):
    if nums[i] == 1:
        count+=1
    else:
        count = 0
    if max_count < count:
        max_count = count
    else:
        max_count = max_count

print(max_count)

# be careful with the = sign and == sign 

# time complexity is O(n)
# space complexity is O(1)