#// ****************************************


# arr = [4,1,8,7,6,5]
# n = len(arr)
# k = 2
# rotations = k % n
# for _ in range(rotations):
#     # temp = arr[n-1]
#     # for i in range(n-1,0,-1):
#     #     arr[i] = arr[i-1]
#     # arr[0] = temp
#     e = arr.pop()
#     arr.insert(0,e)
# print(arr)

# time complexity: O(n*k)
# space complexity: O(1)

#// ****************************************

# nums = [2,3,1,4,22,7,111]
# n = len(nums)
# k = 5
# temp = n%k

# nums[:] = nums[temp:] + nums[:temp]

# print(nums)



# time complexity: O(n)
# space complexity: O(n)

#// ****************************************


nums = [100,69,4,1,8,7,6,5]
n = len(nums)
k = 3
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

reverse(nums, n-k, n-1) #reverse the whole array from n-k to end
reverse(nums, 0, n-k-1) #reverse from start to n-k-1    
reverse(nums, 0, n-1) #reverse from n-k to end again

print(nums)

# time complexity: O(k/2 + (n-k)/2 + n/2) = O(n)
# space complexity: O(1) coz we are not using any extra space but just swapping elements in the same array if we use slicing then space complexity will be O(n) because slicing creates a new array and uses extra space

#// ****************************************
