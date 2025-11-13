# Leetcode 15: 3Sum Problem - Part 44 <HARD_PROBLEM>

#? Find all unique triplets in the array which gives the sum of zero. where triplet is (a,b,c) such that a+b+c=0 and a,b,c are different elements of array.




# nums = [-1, 0, 1, 2, -1, -4]

# def threeSum(nums):
#     n = len(nums)
#     my_set = set()
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if i != j and j != k and i != k:
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = tuple(sorted([nums[i], nums[j], nums[k]]))
#                         my_set.add(temp)
#     return [list(t) for t in my_set]


# print(threeSum(nums))

# Output: [[-1, -1, 2], [-1, 0, 1]]
#? Time complexity is O(n^3) due to the three nested loops iterating through the array.
#? Space complexity is O(k) where k is the number of unique triplets found, as they are stored in a set before being converted to a list for the final output.
#? This is a brute-force solution and may not be efficient for large inputs. More optimal solutions exist using sorting and two-pointer techniques.

#* -----------------------------------------
#? here is the optimal solution for the same problem.....................................




# def threeSums(nums):
#     n = len(nums)        
#     k_set = set()

#     for i in range(n):
#         my_set = set()
#         for j in range(i+1,n):
#             k = -(nums[i] + nums[j])
#             if k in my_set:
#                 temp = [nums[i], nums[j], k]
#                 temp.sort()
#                 k_set.add(tuple(temp))
#             my_set.add(nums[j])      # Always update after checking



# # If the sum of two elements equals the negative of a third element, this triplet will give zero sum

# # We cannot add a list to a set because sets don't allow mutable elements, so we add tuples which are immutable to store unique triplets
            
#     return [list(t) for t in k_set] # Convert unique triplets (tuples) back to list form

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSums(nums))

#? Time complexity is O(n^2) because we have a nested loop where the outer loop runs n times and the inner loop runs up to n times in the worst case.
#? Space complexity is O(k) where k is the number of unique triplets found, as they are stored in a set before being converted to a list for the final output. Additionally, the inner set used for checking complements also takes up space, but it is temporary and resets with each iteration of the outer loop.
#* -----------------------------------------

# ? best optimal solution starts here.........................................



def threeSumOptimal(nums):
    
    ans = []
    n = len(nums)
    # my_set = set()

    nums.sort()

    for i in range(n):
        if i!=0 and nums[i] == nums[i-1]:
            continue
        # moving the two pointers 
        j = i+1
        k = n-1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1

                # my_set.add(temp)
                # move j and k to the next different numbers to avoid duplicates
                while j < k and nums[j] == nums[j-1]:  
                    j += 1
                    # it avoids duplicates for the second number
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
                    # it avoids duplicates for the third number
              
    return [list(t) for t in ans]

nums = [-1, 0, 1, 2, -1, -4]
print(threeSumOptimal(nums))

# ? Time complexity is O(n^2) because we sort the array (O(n log n)) and then use a nested loop where the outer loop runs n times and the inner two-pointer approach runs in O(n) time. Overall, O(n log n + n^2) simplifies to O(n^2) for large n.

# ? Space complexity is O(1) if we don't count the output list, as we are using only a constant amount of extra space for variables. The output list itself takes O(k) space where k is the number of unique triplets found.

# ? This is the most optimal solution for the 3Sum problem in terms of time complexity