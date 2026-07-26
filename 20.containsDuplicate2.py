import os
os.system('cls')

def containsDuplicate(nums,k):
    lastIndex = {}

    for i in range(len(nums)):
        if nums[i] in lastIndex:
            if i - lastIndex[nums[i]] <= k:
                return True

        lastIndex[nums[i]] = i

    return False

nums = [1,2,3,1]
k = 3

print(containsDuplicate(nums,k))