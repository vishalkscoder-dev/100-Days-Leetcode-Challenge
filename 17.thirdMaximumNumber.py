import os
os.system("cls")

nums = [3,2,1,35,27,2]

# Remove duplicates we can use set().

nums = list(set(nums))

nums.sort(reverse=True)

if len(nums) >= 3:
    print(nums[2])
else:
    print(nums[0])





