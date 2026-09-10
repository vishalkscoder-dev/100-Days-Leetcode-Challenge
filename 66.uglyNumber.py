import os
os.system('cls')

def nthUglyNumber(n):
    ugly = [1]

    i2 = 0
    i3 = 0
    i5 = 0

    for i in range(1,n):
        next2 = ugly[i2] * 2
        next3 = ugly[i3] * 3
        next5 = ugly[i5] * 5

        minimum = min(next2, next3, next5)
        ugly.append(minimum)

        if minimum == next2:
            i2 += 1
        if minimum == next3:
            i3 += 1
        if minimum == next5:
            i5 += 1

    return ugly[-1]

num = 10
print(nthUglyNumber(num))

















    