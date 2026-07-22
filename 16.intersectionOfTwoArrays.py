import os
os.system('cls')

def intersection(nums1, nums2):
    freq1 = {}
    freq2 = {}

    result = []

    for num in nums1:
        freq1[num] = freq1.get(num,0)+1
    
    for num in nums2:
        freq2[num] = freq2.get(num,0)+1
    
    for key1,value1 in freq1.items():
        for key2, value2 in freq2.items():
            if key1 == key2:
                result.append(key1)

    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))