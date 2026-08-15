import os
os.system('cls')


def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

    print(nums)
    
nums = [1,2,3,4,5,6,7] 
k = 3

rotate(nums,k)

        
        