# arr = [7, 18, 45, 64, 23, 89, 12]

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         #? if arr[key] < arr[i-1]:
#         #?     arr[key], arr[i-1] == arr[i-1], arr[key]
#         #? return arr
#         j = i - 1
#         while arr[key] < arr[j]:
#             arr[key], arr[i-1] == arr[i-1], arr[key]
#     return arr

# insertion_sort(arr)
# print(arr)
# *******************************************************
# Mistakes in my code:

# for i in range(1, len(arr)-1):
# → should be range(1, len(arr)) (you need to check all elements, not skip the last one).

# key = i
# → wrong! key should be the value (arr[i]), not the index.

# arr[key], arr[i-1] == arr[i-1], arr[key]
# → you used == (comparison) instead of = (assignment). Also, this swap logic isn’t correct for insertion sort.

# You used return arr inside the loop. That makes the function stop after the first iteration. It should be after the loop.

# *******************************************************
# Corrected Code:


arr = [7, 18, 45, 64, 23, 89, 12]
def insertion_sort(arr):
    for i in range(1, len(arr)):   # start from 2nd element

        key = arr[i]              # current element
        j = i - 1                 # previous index
   # shift bigger elements one step to the right
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

            
        arr[j+1] = key # place key in correct spot
    return arr

insertion_sort(arr)
print(arr)



#?.............................................
# Time complexity is O(n^2) because of nested loops ... tc= O(n*(n-1)) = O(n^2) because of nested loops and it is not dependent on the order of elements here the loops will run n*(n-1)/2 times so it is O(n^2)

# Space complexity is O(1) because no extra space is used only a few variables are used for swapping and indexing if we use recursion then space complexity will be O(n) due to call stack

#? Best case: O(n) when the array is already sorted (only one pass needed)
#? Average case: O(n^2)
#?* Worst case: O(n^2) when the array is sorted in reverse order (maximum shifts needed)

# Insertion sort is efficient for small datasets and mostly sorted arrays. It’s stable and in-place, making it useful for certain applications.

#? Algorithm Steps:


# 1. Start with the second element (index 1) as the key.    
# 2. Compare the key with the elements before it (to its left).
# 3. Shift all larger elements one position to the right to make space for the key.
# 4. Insert the key into its correct position.  
# 5. Repeat steps 1-4 for all elements in the array.

#? Example:

# Unsorted array: [7, 18, 45, 64, 23, 89, 12]
# Step 1: Key = 18, compare with 7 → [7, 18, 45, 64, 23, 89, 12]
# Step 2: Key = 45, compare with 18 → [7, 18, 45, 64, 23, 89, 12]
# Step 3: Key = 64, compare with 45 → [7, 18, 45, 64, 23, 89, 12]
# Step 4: Key = 23, compare with 64, 45 → [7, 18, 23, 45, 64, 89, 12]
# Step 5: Key = 89, compare with 64 → [7, 18, 23, 45, 64, 89, 12]
# Step 6: Key = 12, compare with 89, 64, 45, 23, 18 → [7, 12, 18, 23, 45, 64, 89]


# Sorted array: [7, 12, 18, 23, 45, 64, 89]

