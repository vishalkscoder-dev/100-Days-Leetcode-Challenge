import os
os.system('cls')

def containsDuplicate(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for value in freq.values():
        if value > 1:
            return True
    
    return False

nums = [2,1,2,4,5]
print(containsDuplicate(nums))