# Leetcode 48: Rotate Matrix by 90 Degrees - Part 42

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rows = len(matrix)
cols = len(matrix[0])
rotated_matrix = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        rotated_matrix[j][rows-1-i] = matrix[i][j]
print(rotated_matrix)
print("**************************************")
for i in range(len(rotated_matrix)):
    for j in range(len(rotated_matrix[0])):
        print(rotated_matrix[i][j],end=" ")
    print()
print("**************************************")
# time complexity: O(n^2) where n is the number of rows or columns in the matrix
# space complexity: O(n^2) as we are using an extra matrix to store the result
# ----------------------------------------
#? optimal solution: rotate the matrix in place without using extra space (modifies the original matrix)
# step 1: transpose the matrix
n = len(matrix)
for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # time complexity: O(n*n) because we are traversing half of the matrix

# step 2: reverse each row
for i in range(n):
    matrix[i].reverse() 
    #   time complexity: O(n*n) because we are reversing n rows each of size n

    # here we can also use two pointer approach to reverse the row like below:
    # left = 0
    # right = len(matrix[i]) - 1
    # while left < right:
    #     matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
    #     left += 1
    #     right -= 1

print(matrix)
print("**************************************")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
print("**************************************")


# time complexity: O(n^2) + O(n^2) = O(n^2) where n is the number of rows or columns in the matrix
# space complexity: O(1) as we are not using any extra space



#* /****************************************/