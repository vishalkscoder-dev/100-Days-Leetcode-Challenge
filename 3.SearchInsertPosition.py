import os
os.system('cls')


def searchInsert(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1

    return left

arr = [1,2,4,7,37]
target = 5

print(searchInsert(arr, target))

