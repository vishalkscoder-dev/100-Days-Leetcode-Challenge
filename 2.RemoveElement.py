import os
os.system('cls')

def removeElement(arr, val):

    k = 0

    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]

            k += 1

    return k


arr = [1,2,4,3,5,3,5,2,5,2]
val = 5

print(removeElement(arr,val))