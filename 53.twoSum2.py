import os
os.system('cls')

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]

        elif total < target:
            left += 1

        else:
            right -= 1


numbers = [1,23,445,232,5676]
target = 677

print(twoSum(numbers, target))