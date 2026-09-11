import os
os.system('cls')

def threeSum(nums):
    nums.sort()

    result = []

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right] 

            if total == 0:
                if [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            
            else:
                right -= 1

    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))