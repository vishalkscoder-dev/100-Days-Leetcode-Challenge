import os
os.system('cls')

def moveZeros(nums):
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[index] = nums[index], nums[i]

            index += 1
        
    return nums

nums = [0,1,0,3,12]
print(moveZeros(nums))
