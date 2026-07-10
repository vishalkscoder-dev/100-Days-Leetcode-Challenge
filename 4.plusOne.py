import os
os.system('cls')

def plusOne(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0

    return [1] + arr

arr = [9,9,6]
print(plusOne(arr))