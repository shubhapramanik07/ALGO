#  Find First & Last Occurrence in Sorted Array | Binary Search - Part 50
#? Given a sorted array of integers, find the first and last occurrence of a given target value using binary search.

# def first_and_last_occurrence(nums, target):
#     n = len(nums)
    
#     # Helper function to find lower bound (first occurrence)
#     def lbb(nums, target):
#         low = 0
#         high = n - 1
#         lb = -1
#         while low <= high:
#             mid = (high + low) // 2
#             if nums[mid] >= target:
#                 lb = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return lb
    
#     # Helper function to find upper bound (last occurrence)
#     def upp(nums, target):
#         low = 0
#         high = n - 1
#         up = -1
#         while low <= high:
#             mid = (high + low) // 2
#             if nums[mid] > target:
#                 high = mid - 1
#             else:
#                 up = mid
#                 low = mid + 1
#         return up
    
#     first = lbb(nums, target)
#     if first == -1:
#         return[-1,-1]
#     last = upp(nums, target)
#     return [first, last]
    
# nums = [1,2,2,2,3,4,5,5,5,6,7,8]
# target = 2
# result = first_and_last_occurrence(nums, target)
# print(result)  # Output: [6, 8]


# ? **********************888************



def xcv(nums,target):
    first = -1
    last = -1
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
        # if first != -1 and  nums[i] != target:
        #     last = i-1
    return(first,last)


nums = [1,2,2,2,3,4,5,5,5,6,7,8]
target = 2
result = xcv(nums, target)
print(result)

