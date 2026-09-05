import os
os.system('cls')

def firstMissingPositive(nums):
    nums.sort()

    missing = 1

    for num in nums:
        if num == missing:
            missing += 1

    return missing

nums = [3,4,-1,1]
print(firstMissingPositive(nums))