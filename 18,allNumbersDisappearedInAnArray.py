import os
os.system('cls')

nums = [4,3,2,7,8,2,3,1]

length = len(nums)
result = []

for i in range(1,length+1):
    if i not in nums:
        result.append(i)

print(result)