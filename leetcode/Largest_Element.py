array = [707, 108, 595, 649, 123, 698, 6969, 6961]
length = len(array)
for i in range(length):
    min_index = i
    for j in range(i + 1, length):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    

print("Max element:", array[-1] if array else None)

