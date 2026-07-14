import os
os.system('cls')

def majorityElement(nums):
    count = 0
    finalResult = None

    for num in nums:
        if count == 0:
            finalResult = num
        
        if num == finalResult:
            count += 1
        else:
            count -= 1

    return finalResult

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

















