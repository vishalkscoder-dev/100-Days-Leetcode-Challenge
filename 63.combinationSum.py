import os
os.system('cls')

def combinationSum(candidates, target):
    result = []

    def find(start, total, arr):

        if total == target:
            result.append(arr[:])
            return 

        if total > target:
            return

        for i in range(start, len(candidates)):
            arr.append(candidates[i])

            find(i, total + candidates[i], arr)

            arr.pop()

    find(0, 0, [])

    return result

candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates, target))
