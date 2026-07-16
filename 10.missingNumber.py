import os
os.system('cls')

def missingNumber(numSet):
    for i in range(len(numSet)+1):
        if i not in numSet:
            return i

nums = [0,1,2,3,4]
numSet = set(nums)

print(missingNumber(numSet))