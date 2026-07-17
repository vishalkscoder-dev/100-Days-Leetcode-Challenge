import os
os.system('cls')

def maximumSubarray(nums):
    current = 0
    maximum = nums[0]

    for i in nums:
        if current < 0:
            current = 0
        current += i

        if maximum < current:
            maximum = current

    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))