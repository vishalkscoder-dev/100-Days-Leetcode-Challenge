import os
os.system('cls')

def primePalindrome(n):
    prime = []

    if n <= 2:
        return 2

    if n <= 3:
        return 3
    
    if n <= 5:
        return 5
    
    if n <= 7:
        return 7
    
    if n <= 11:
        return 11

    for i in range(1,2000000):
        s = str(i)
        num = int(s + s[-2::-1])

        if num < n:
            continue

        for j in range(2, int(num ** 0.5)+1):
            if num % j == 0:
                break

        else:
            return num

n = 6
print(primePalindrome(n))




    