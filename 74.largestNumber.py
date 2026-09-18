from functools import cmp_to_key
import os

os.system('cls')

def largestNumber(nums):
    nums = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    nums.sort(key=cmp_to_key(compare))

    result = ''.join(nums)

    if result[0] == '0':
        return '0'

    return result

nums = [3,30,34,5,9]
print(largestNumber(nums))