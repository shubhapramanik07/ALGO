# Leetcode 48: Rotate Matrix by 90 Degrees - Part 42

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rows = len(matrix)
cols = len(matrix[0])
results = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        results[j][rows-1-i] = matrix[i][j]
print(results)
print("**************************************")
for i in range(len(results)):
    for j in range(len(results[0])):
        print(results[i][j],end=" ")
    print()
print("**************************************")
# time complexity: O(n^2) where n is the number of rows or columns in the matrix
# space complexity: O(n^2) as we are using an extra matrix to store the result
#* /****************************************/
#? optimal solution without using extra space   
# step 1: transpose the matrix
