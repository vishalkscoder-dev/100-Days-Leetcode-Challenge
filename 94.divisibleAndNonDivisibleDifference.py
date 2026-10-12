import subprocess
subprocess.run('cls', shell=True)

def differenceOfSums(n, m):
    array = []
    
    for i in range(1, n+1):
        array.append(i)

    divisible = 0
    notDivisible = 0

    for num in array:
        if num % m == 0:
            notDivisible += num

        else:
            divisible += num

    answer = divisible - notDivisible

    return answer
        
n = 10
m = 3

print(differenceOfSums(n,m))