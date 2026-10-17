import subprocess
subprocess.run('cls', shell=True)

def subarraySum(nums, k):
    total = 0
    freq = {0:1}

    addition = 0

    for num in nums:
        addition += num

        if addition - k in freq:
            total += freq[addition - k]

        freq[addition] = freq.get(addition,0) + 1

    return total

    
nums = [1,1,1]
k = 2

print(subarraySum(nums,k))

        