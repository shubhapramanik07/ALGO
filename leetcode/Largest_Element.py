array = [707, 108, 595, 649, 123, 68, 66, 1]
# length = len(array)
# for i in range(length):
#     min_index = i
#     for j in range(i + 1, length):
#         if array[j] < array[min_index]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
    

# print("Max element:", array[-1] if array else None)


# ? 2nd method..............

# largest = array[0]
# n = len(array)
# for i in range(n): 
#     largest = max(largest,array[i])
# print(largest)

# time_complexity = O(N)
# space_complexity = O(1)

# ?..........................

# * 3rd method................
largest = float("-inf")
n = len(array)
for i in range(n):
    largest = max(largest,array[i])
print( largest)



