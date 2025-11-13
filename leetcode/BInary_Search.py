#  Introduction to Binary Search - Part 46

#? Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.
#*Easy Problem............................  

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 7
# # the given array should be sorted for binary search to work correctly. otherwise, we have to sort it first.
# def binary_search(arr, target):
#     n = len(arr)
#     start = 0
#     end = n-1
#     while start <= end:
#         mid = (start+end)//2    

#         if target == arr [mid]:
#             return mid
#         elif target < arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found in the array.")

# this was the basic implementation of binary search algorithm. using while loop.

# * .........................................
# * .........................................

# koi loop agaar bar bar karke 2 divide krta jaa rha hai. to isme time complexity log2(n) hoti hai. #### agar mai har ak loop mai 10 divide krdu to time complexity log10(n) ho jaayegi.like that.

# so over all time complexity of binary search is log(n) base 2. where n is the number of elements in the array.
# space complexity is O(1) as we are not using any extra space.
# * .........................................
# * .........................................
#? Binary Search Applications:
# 1. Finding an element in a sorted array.
# 2. Finding the first or last occurrence of an element in a sorted array.
# 3. Finding the square root of a number.
# 4. Searching in a rotated sorted array.
# 5. Finding the peak element in an array.
# 6. Finding the minimum or maximum element in a bitonic array.
# 7. Allocating resources efficiently (e.g., in load balancing).
# 8. Solving optimization problems (e.g., finding the optimal value in a range).
# 9. Searching for a specific value in a matrix where each row and column is sorted.
# 10. Finding the smallest/largest element that satisfies a certain condition (e.g., in binary search on answer problems).  
#* .........................................

# * .........................................
#? now, let's see the recursive implementation of binary search algorithm.

def binary_search_recursive(arr, target, start, end):

    if start > end:
        return -1
    mid = (start + end)//2
    if arr[mid] > target:
        return binary_search_recursive(arr,target,start,mid-1)
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid+1,end)
    else:
        return mid
    
arr = [1,3,5,6,7,9,99,100]
target = 7
start = 0
end = len(arr) - 1 
bs = binary_search_recursive(arr,target,start,end)
print(bs)
