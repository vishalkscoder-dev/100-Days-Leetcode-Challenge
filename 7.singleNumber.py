import os
os.system('cls')

def singleNumber(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            del freq[num]
    
    return list(freq.keys())[0]


nums = [2,2,7,7,9]
print(singleNumber(nums))