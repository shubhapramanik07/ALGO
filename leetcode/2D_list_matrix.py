# DSA in Python Course - Learn About 2D List or Matrix - Part 40

# nums = [[5,20,3],[10,6,2],[8,-7,4]]
nums = [[5,9,1],[2,3,7]]
rows = len(nums)
columns = len(nums[0])

for i in range(0,rows):
    for j in range(0,columns):
        # print(nums[i][j])
        print(nums[i][j],end=" ")
    print()

# print the upper triangle:---------------
print("***********************************")

for i in range(0,rows):
    for j in range(0,columns):
        if i<=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# print the lower triangle:---------------
print("***********************************")

for i in range(0,rows):
    for j in range(columns):
        if i<=j:
            print("*",end=" ")
        else:
            print(nums[i][j],end=" ")
    print()

# print diagonal:-------------

print("*************************************")

for i in range(0,rows):
    for j in range(0,columns):
        if i == j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


# transpose of matrix:-------------
print("*************************************")

results = [[0]*rows for _ in range(columns)]
for i in range(rows):
    for j in range(columns):
        results[j][i] = nums[i][j]
print(results)

print("****************[OR]*********************")
for i in range(len(results)):
    for j in range(len(results[0])):
        print(results[i][j],end=" ")
    print()

