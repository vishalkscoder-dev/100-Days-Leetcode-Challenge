import os
os.system('cls')


def sortColors(nums):

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

nums = [1,3,0,0,2,5,2]
print(sortColors(nums))