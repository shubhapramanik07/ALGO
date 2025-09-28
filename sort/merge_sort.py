# one of the most important sorting algorithms
# it is a stable sorting algorithm

# it always works divide and conquer approach


# arr = [77, 418, 5, 64, 123, 89, 1]
# # length is 07
# # mid = 3 (which is left (0-3))
# def merge_sort(arr):

#     if len(arr) <= 1:
#         return arr  # no change
#     mid = len(arr)//2  # no change
#     left = merge_sort(arr[:mid])  # no change
#     right = merge_sort(arr[mid:])  # no change
#     merged = merge_arr(left, right)  # no change
#     # print(merged)  # removed unnecessary print statement
#     return merged  # fixed: return the merged result


# def merge_arr(left,right):
#     result =[]
#     i,j=0,0
#     n,m=len(left),len(right)
#     while i<n and j<m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     if i<n:
#         while i<n:
#             result.append(left[i])
#             i+=1
#     if j<m:
#         while j<m:
#             result.append(right[j])
#             j+=1
#     # print("result:",result)  # removed unnecessary print statement
#     return result  # no change

# # Call merge_sort and print the sorted array
# print("Sorted array:", merge_sort(arr))



#* time complexity is O(n log n) because the array is repeatedly divided in half (log n divisions), and merging the divided arrays takes linear time (O(n)) at each level of division.
#? space complexity is O(n) because we need additional space to store the divided arrays during the merge  


# ?  here is the one part code to merge two sorted array........................

left_arr = [1,2,3,4,5,5,10]
right_arr = [3,4,5,6,9]
result = []
m = len(left_arr)
n = len(right_arr)
i,j = 0,0 
 

while i < m and j < n:
    if left_arr[i]<=right_arr[j]:
        result.append(left_arr[i])
        i+=1
    else:
        result.append(right_arr[j])
        j+=1

if i<m:
    while i<m:
        result.append(left_arr[i])
        i+=1
if j<n:
    while j<n:
        result.append(right_arr[j])
        j+=1

print (result)



# ? now here you can see how merge_sort(arr) works.......................
# nums = [3,1,2,4,1,5,2,6,4]
# def merge_sort(arr):
#     if len(arr) < 1:
#         return arr
#     mid = len(arr)//2
#     left_arr = nums[:mid]
#     right_arr=nums[mid:]
#     left = merge_sort(left_arr)
#     right = merge_sort(right_arr)
#     return merge_array(left,right)