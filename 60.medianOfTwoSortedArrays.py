import os
os.system('cls')

def median(nums1,nums2):
    array = nums1 + nums2

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    length = len(array)
    middle = length // 2

    if length % 2 == 0:
        return (array[middle-1] + array[middle]) / 2.0

    else:
        return float(array[middle])

nums1 = [1,5,2,7]
nums2 = [5,1,6,9]
print(median(nums1, nums2))