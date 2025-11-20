# Search in Rotated Sorted Array | Binary Search Approach - Part 52
#? Given a rotated sorted array and a target value, find the index of the target in the array using binary search.


#* 1st step : find the pivot point in the rotated sorted array where the rotation happened.
#* 2nd step : perform binary search in the appropriate half of the array based on the target value and the pivot point. where pivot point means the index of the smallest element in the rotated sorted array.
# * this is the optimal approach...time complexity will be O(log n) and space complexity will be O(1)

# def search_rotated_sorted_array(nums, target):

#     n = len(nums)
#     start = 0
#     end = n - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if nums[mid] == target:
#             return mid
        
#         if nums[mid] <= nums[end]:  # right sorted

#             if nums[mid] < target <= nums[end]:
#                 start = mid + 1
#             else:
#                 end = mid - 1

#         else:   # left sorted

#             if nums[start] <= target < nums[mid]:
#                 end = mid -1 
#             else:
#                 start = mid + 1

#     return -1


# nums = [333,404,1,4,68,69,101]
# target = 4
# result = search_rotated_sorted_array(nums, target)
# print(result)    
    


# * .........................................
# # this is the brute force approach...time complexity will be O(n) and space complexity will be O(1)

# def search_rotated_sorted_array(nums, target):
#     n = len(nums)

#     for i in range(n):
#         if nums[i] == target:
#             return i
#     return -1
# nums = [44,55,6,7,10,12,22]
# target = 7
# result = search_rotated_sorted_array(nums, target)
# print(result)  # Output: 4


# ?.................................................


#* Search in Rotated Sorted Array II | Binary Search with Duplicate - Part 53


#? Given a rotated sorted array that may contain duplicates and a target value, find the index of the target in the array using binary search.....

def search_rotated_sorted_array_with_duplicates(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
  
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] == nums[high]: # handling duplicates as in this case we cannot decide which half is sorted so we just shrink the search space by moving both pointers inward
            low += 1
            high -= 1
            continue
        # this part is same as search in rotated sorted array without duplicates
        if nums[mid] <= nums[high]:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid -1
        else:
            if nums[mid] >= target > nums[low]:
                high = mid - 1
            else:
                low = mid + 1
    return False
nums = [7,7,7,7,7,7,7,1,2,3,4,7]
target = 33
# nums = [222,404,999,999,1,3,3,4,66,69,69,101]
# target = 69
result = search_rotated_sorted_array_with_duplicates(nums,target)
print (result)

# time complexity: O(log n) in average case and O(n/2) = O(n) in worst case due to duplicates and we are shrinking the search space by moving both pointers inward when we encounter duplicates.
# space complexity: O(1)    