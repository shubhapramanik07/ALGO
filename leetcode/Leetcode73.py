# Leetcode 73: Set Matrix Zeros - Part 41
# the question is to set the entire row and column to 0 if an element is 0 in the matrix
#* /****************************************/

def mark_infinity(nums,row_index,col_index):
    for i in range(rows):
        if nums[i][col_index] != 0:
            nums[i][col_index] = float("inf")
    for j in range(cols):
        if nums[row_index][j] != 0:
            nums[row_index][j] = float("inf")
    return nums

# time complexity: O(m+n) where m is the number of rows and n is the number of columns
# space complexity: O(1) as we are using only constant space
def set_matrix_zero(nums):
    for i in range(rows):
        for j in range(cols):
            if nums[i][j] == 0:
                mark_infinity(nums,i,j)
                # time complexity of this function is O(m*n)
    for i in range(rows):
        for j in range(cols):
            if nums[i][j] == float("inf"):
                nums[i][j] = 0
                # time complexity of this function is O(m*n)
    return nums

nums = [[5,1,2,0],[9,4,5,2],[1,3,1,5],[1,5,1,5]]
rows = len(nums)            
cols = len(nums[0])

result = set_matrix_zero(nums)
print(result)   

# overall time complexity: O((m+n)*(m*n)) + O(m*n) where m is the number of rows and n is the number of columns
# overall space complexity: O(1) as we are using only constant 


# this was a brute force approach
#* /****************************************/
#? optimal solution using first row and first column as markers

print("**************************************")

nums = [[5,1,2,0],[9,4,5,2],[1,3,1,5],[1,5,1,5]]
rows = len(nums)            
cols = len(nums[0])
rowtrack = [0]*rows
coltrack = [0]*cols

for i in range(rows):
    for j in range(cols):
        if nums[i][j] == 0:
            rowtrack[i] = -1
            coltrack[j] = -1
    
for i in range(rows):
    for j in range(cols):
        # if nums[i][j] == -1:
        #     nums[i][j] = 0 i made mistake here...
        if rowtrack[i] == -1 or coltrack[j] == -1:
            nums[i][j] = 0


print(nums)
# overall time complexity: O (2(m*n)) = O(m*n) where m is the number of rows and n is the number of columns
# overall space complexity: O(m+n) where m is the number of rows and n is the number of columns
#* /****************************************/