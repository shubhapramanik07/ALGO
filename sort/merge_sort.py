# one of the most important sorting algorithms
# it is a stable sorting algorithm

# it always works divide and conquer approach


arr = [77, 418, 5, 64, 123, 89, 1]
# length is 07
# mid = 3 (which is left (0-3))
# res of  l - mid = 4 (which is right arr(4-6))

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge_arr(left,right)
    print(merged)
    # return merged

    print(merge_arr(left,right))


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
    return result

