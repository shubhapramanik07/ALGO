# Leetcode 268: Find Missing Number in an Array 


# arr = [2, 4, 3, 0]

# def missingNumber(arr):
#     l = len(arr)
#     for i in range(l-1):
#         min_index = i
#         for j in range(i+1,l):
#             if(arr[j] < arr[min_index]):
#                 min_index = j
#             arr[i],arr[min_index] = arr[min_index],arr[i]
            
#     for k in range(l):
#         if arr[k] != k:
#             return k
            

# missingNumber(arr)
# print(missingNumber(arr))

# /****************************************

# arr = [2,5,1,0,3,6,8,9,4]

# for j in range(len(arr)+1):
#     if j not in arr:
#        print(j) 
    
    # time complexity is O(n^2)
    # space complexity is O(1)

# ******************************************/

# nums = [3,0,1,4,2,5,7]
# l = len(nums)
# freq = {}

# for i in range(0,l+1):
#     freq[i] = 0
    
# for num in nums:
#     freq[num] = 1

# for k,v in freq.items():
#     if v == 0:
#       print(k)

# time complexity is O(n+n+n) = O(n)
# space complexity is O(n) due to the freq dictionary
# ******************************************/
# optimal solution

arr = [3,0,1,4,2,5,7]


def missingNumber(arr):
    total = 0
    n = len(arr)
    for i in range(0,n+1):
        total = total + i

    sums = 0
    for num in arr:
        sums = sums + num

    return total - sums

print(missingNumber(arr))


# time complexity is O(n(n+n)/2) = O(n)
# space complexity is O(1) as no extra space is used