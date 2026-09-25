import subprocess
subprocess.run('cls', shell=True)

def nextGreaterElement(nums1, nums2):
    result = []

    for x in nums1:
        index = nums2.index(x)
        greater = -1

        for j in range(index + 1, len(nums2)):
            if nums2[j] > x:
                greater = nums2[j]
                break

        result.append(greater)

    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1, nums2))