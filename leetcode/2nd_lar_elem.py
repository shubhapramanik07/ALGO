# arr = [39,1,6,400,77,69,0,5,69,51]

# def s_lar():
#     largest = float("-inf")
#     second_largest = float("-inf")

#     for i in range(len(arr)):
#         largest = max(largest,arr[i])
#     for i in range(len(arr)):
#         if arr[i] > second_largest and arr[i] < largest:
#             second_largest = arr[i]
#     print(second_largest)
#     return second_largest

# s_lar()


# *************************************************
# time complexity = O(N+N) = O(2N) = O(N)
#                                      space complexity = O(1)
#  because no extra space is used only a few variables are used for comparison)


# **************************************************# ? another method to find the 2nd largest element in the array.................


array = [39,1,6,400,77,69,0,5,69,51]

largest = float("-inf")
s_lar = float("-inf")

for i in range(len(array)):
    if largest < array[i]:
        s_lar = largest
        largest = array[i]
    elif s_lar < array[i] and array[i] != largest:
        s_lar = array[i]

print(s_lar)




# timecomplexity = O(N)
# spacecomplexity = O(1)

#  because no extra space is used only a few variables are used for comparison)
# ?.................................................