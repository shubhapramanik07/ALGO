# one of the most important sorting algorithms
# it is a stable sorting algorithm

# it always works divide and conquer approach


arr = [77, 418, 5, 64, 123, 89, 1]
# length is 07
# mid = 3 (which is left (0-3))
def merge_sort(arr):

    if len(arr) <= 1:
        return arr  # no change
    mid = len(arr)//2  # no change
    left = merge_sort(arr[:mid])  # no change
    right = merge_sort(arr[mid:])  # no change
    merged = merge_arr(left, right)  # no change
    # print(merged)  # removed unnecessary print statement
    return merged  # fixed: return the merged result


def merge_arr(left,right):
    result =[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    # print("result:",result)  # removed unnecessary print statement
    return result  # no change

# Call merge_sort and print the sorted array
print("Sorted array:", merge_sort(arr))

