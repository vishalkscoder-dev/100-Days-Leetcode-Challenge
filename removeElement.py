import os
os.system('cls')

def removeElement(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]

            write += 1
        
    return write

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))