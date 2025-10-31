# using set or dict we can remove duplicates from an array and then convert it back to list this is the simplest way to remove duplicates from an array in python


# arr = [1,1,2,3,3,4,4,5,5,5,10]

# n = len(arr)
# freq_map = {}
# for i in range(0,n):
#     freq_map[arr[i]] = 0
#     j = 0
#     for k in freq_map:
#         arr[j] = k
#         j+=1


# print(j)
# print(freq_map)
# print(arr[:j])
# *************************************************
# here time complexity is O(n+m) where n is the size of the array and m is the number of unique elements in the array
# here space complexity is O(m) where m is the number of unique elements in the array because we are using a dictionary to store the unique elements
# *************************************************
# ? another method to remove duplicates from a sorted array in place without using extra space.................
def remove_duplicates(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            print("i:",i,"j:",j,"arr:",arr)
        j += 1
    return i+1
    

arr = [1,1,2,3,3,4,4,5,5,5,10]
result = remove_duplicates(arr)

print(result)
print(arr[:result])

    # *************************************************
# time complexity is O(N) because we are traversing the array only once
# space complexity is O(1) because we are not using any extra space


        