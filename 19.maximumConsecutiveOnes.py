import os
os.system("cls")

def maximumConsecutiveOnes(nums):
    count = 0
    maximum = 0

    for num in nums:
        if num == 1:
            count += 1
            if maximum < count:
                maximum = count
        else:
            count = 0

    return maximum

nums = [1,1,2,1,1,1,1]
print(maximumConsecutiveOnes(nums))