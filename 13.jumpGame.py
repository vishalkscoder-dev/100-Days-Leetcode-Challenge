import os
os.system('cls')

# Greedy Algorithm

def jumpGame(nums):
    final = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if final <= nums[i] + i:
            final = i
        
    if final == 0:
        return True
    else:
        return False

nums = [2,3,1,1,4]
print(jumpGame(nums))