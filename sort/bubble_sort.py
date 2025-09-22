# def swap(arr,f,s):
#     if f>s:
#         arr[f],arr[s]=arr[s],arr[f]
#     f+=1
#     s+=1


# using two pointers..........#
def bubble_arr(arr,first,second):
    n = len(arr)
    while second < n:    # loop until second pointer reaches end
        if arr[first] > arr[second]:
            arr[first], arr[second] = arr[second], arr[first] # swap if needed
        first += 1
        second += 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        bubble_arr(arr,0,1)
    return arr


arr = [26,2,65,1,99,6,32]
bubble_sort(arr)
print(arr)




#? this will sort the array in ascending order and the output will be [1, 26, 32, 65, 99]

#*  tc= O(n*(n-1)) = O(n^2) because of nested loops and it is not dependent on the order of elements here the loops will run n*(n-1)/2 times so it is O(n^2)

#? for the best case ,,,TC = O(n) & SC = O(1) 


# *another easy way to solve the problem

# arr = [26,2,65,1,99,6,32]

# n = len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)