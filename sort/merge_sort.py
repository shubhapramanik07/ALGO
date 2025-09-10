# one of the most important sorting algorithms
# it is a stable sorting algorithm

# it always works divide and conquer approach


arr = [77, 418, 5, 64, 123, 89, 1]
# length is 07
# mid = 3 (which is left (0-3))
# res of  l - mid = 4 (which is right arr(4-6))

l = len(arr)
mid = l//2
left = []
right = []

def merge_sort(arr):
    while len(left) == 1:
        for i in range(mid):
            left.append(arr[i])
            return left
    while len(right) == 1:
        for j in range(mid+1,l):
            right.append(arr[j])
            return right
    merge_arr(left,right)

result = merge_sort(arr)
print(result)

def merge_arr(left,right):
    result =[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n or j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    return

