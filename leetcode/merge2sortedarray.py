# Merge 2 Sorted Arrays Without Duplicates 

num1 = [1, 2, 2, 4, 6, 7, 9]
num2 = [1, 3, 5, 8]

n = len(num1)
m = len(num2)
merge = []
i = 0
j = 0

while i < n and j < m:
    if num1[i] <= num2[j]:
        if len(merge) == 0 or merge[-1] != num1[i]: 
            # for the 1st element to insert in the merge array we are checking if the length of merge is 0 then only we can insert the element otherwise we will check if the last element of merge is not equal to the current element to be inserted
            merge.append(num1[i])
        i += 1
    
    else:
        if num2[j] <= num1[i]:
            if len(merge) == 0 or merge[-1] != num2[j]:
                merge.append(num2[j])
        j += 1


while i < n:
    if len(merge) == 0 or merge[-1] != num1[i]:
        merge.append(num1[i])
        i += 1

while j < m:
    if len(merge) == 0 or merge[-1] != num2[j]:
        merge.append(num2[j])
        j += 1

print(merge)
# time complexity is O(n + m) where n and m are the lengths of the two arrays being merged. This is because we traverse each array once.
# space complexity is O(n + m) in the worst case, where all elements from both arrays are unique and need to be stored in the merged array.        result.append(right_arr[j])
