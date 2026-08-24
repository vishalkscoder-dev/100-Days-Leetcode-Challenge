import os
os.system('cls')

def longestConsecutive(nums):
    if not nums:
        return 0
    
    nums.sort()

    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
        elif nums[i] == nums[i-1]:
            continue
        else:
            current = 1
        
        longest = max(longest, current)
    
    return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))