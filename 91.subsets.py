import subprocess
subprocess.run('cls', shell=True)


def subsets(nums):
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result

    
nums = [1,2,3]
print(subsets(nums))