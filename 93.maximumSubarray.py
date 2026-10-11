import subprocess
subprocess.run('cls', shell=True)

def maxSubArray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)

    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))