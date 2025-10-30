nums = [1,2,6,40,77,69,0,5,69,51]
for i in range(0,len(nums)-1):
    if nums[i] > nums[i+1]:
        print("False")
        break
else:
    print("True")


    # timecomplexity = O(N)
    # spacecomplexity = O(1)
    #  because no extra space is used only a few variables are used for comparison)
# ?.................................................