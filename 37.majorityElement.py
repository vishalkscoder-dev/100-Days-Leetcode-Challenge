import os
os.system('cls')

def majorityElement(nums):
    freq = {}
    result = []
    limit = len(nums) // 3

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for key,value in freq.items():
        if value > limit:
            result.append(key)

    return result

nums = [3,2,3]
print(majorityElement(nums))

        