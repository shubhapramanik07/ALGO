#? in interviews they generally ask about this sorting algorithm how it works in the best case and how in the worst case....


def qs(arr):
    lesser = []
    greater = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr[1:]:
            if i < pivot:
                lesser.append(i)
            else:
                greater.append(i)
        return qs(lesser) + [pivot] + qs(greater)
    

arr = [707, 100418, 595, 649, 123, 89, 1]
print("Sorted array:", qs(arr))



# time complexity: O(n log n) on average, O(n^2) in the worst case
#? space complexity: O(log n) due to recursive stack space