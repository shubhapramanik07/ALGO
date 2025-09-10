arr = [64, 25, 12, 22, 11]
# start = arr[0]

def ss(arr):
    # n = len(arr)
    for i in range (0,len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] #this line is for swapping the elements 

    # return arr



ss(arr)
print(arr)

# this will sort the array in ascending order and the output will be [11, 12, 22, 25, 64]
# # time complexity is O(n^2) because of nested loops  ...  tc= O(n*(n-1)) = O(n^2) because of nested loops and it is not dependent on the order of elements here the loops will run n*(n-1)/2 times so it is O(n^2)

# # space complexity is O(1) because no extra space is used  because no extra space is used only a few variables are used for swapping and indexing if we use recursion then space complexity will be O(n) due to call stack


#???????????????????????????????????????????????

