import subprocess
subprocess.run('cls', shell=True)

def myPow(x, n):
    if n < 0:
        n = -n
        x = 1 / x

    answer = 1

    while n > 0:
        if n % 2 == 1:
            answer = answer * x
        
        x = x * x
        n = n // 2

    return answer

x = 2.00000
n = 10

print(myPow(x,n))