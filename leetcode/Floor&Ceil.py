# Floor & Ceil in Sorted Array | Binary Search Approach - Part 49 

#? Given a sorted array and a target value, the floor of the target is the greatest element in the array that is less than or equal to the target, and the ceil of the target is the smallest element in the array that is greater than or equal to the target.

def floor_ceil(arr, target):
    new_set = set()
    floor = -1
    ceil = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr [mid] == target:
            return [arr[mid], arr[mid]]
        
        elif arr[mid] > target:
            ceil = arr[mid]
            end = mid - 1

        else:
            floor = arr[mid]
            start = mid + 1
    return [floor, ceil]
 
arr = [1,3,5,6,7,9,99,100]
target = 8
result = floor_ceil(arr, target)
print(result)  # Output: (5, 6)

# time complexity: log(n) base 2 as we are using binary search approach.
# space complexity: O(1)

# this is the implementation of floor and ceil in a sorted array using binary search approach.
# the approach is similar to binary search where we keep track of floor and ceil values while traversing the array.
# if the mid element is equal to target, we return the mid element as both floor and ceil.
# if the mid element is greater than target, we update ceil and move to the left half of the array.
# if the mid element is less than target, we update floor and move to the right half of the array.
# finally, we return the floor and ceil values.

#? *********************************888

# using linear search approach
def floor_ceil_linear(arr, target):
    floor = -1
    ceil = -1
    for num in arr:
        if num <= target:
            floor = num
        if num >= target and ceil == -1:
            ceil = num
            
    return [floor, ceil]
arr = [1,3,5,6,7,9,99,100]
target = 8
result = floor_ceil_linear(arr, target)
print(result)  # Output: (7, 9)
# time complexity: O(n) as we are traversing the entire array in the worst case.
# space complexity: O(1)
# this is the implementation of floor and ceil in a sorted array using linear search approach.