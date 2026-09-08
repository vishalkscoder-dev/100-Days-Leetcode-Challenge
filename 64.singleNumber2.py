import os
os.system('cls')

def singleNumber(nums):
    listing = []
    freq = {}

    for num in nums:
        listing.append(str(num))

    for num in listing:
        freq[num] = freq.get(num, 0) + 1

    for key,value in freq.items():
        if value == 1:
            return int(key)  


nums = [1,2,4,4,4,2]
print(singleNumber(nums))