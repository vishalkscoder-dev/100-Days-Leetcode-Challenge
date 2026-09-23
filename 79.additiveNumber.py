import subprocess
subprocess.run('cls', shell=True)

def isAdditiveNumber(num):
    n = len(num)

    if n <= 2:
        return False

    for i in range(1, n):
        if num[0] == '0' and i > 1:
            break

        first = int(num[:i])

        for j in range(i + 1, n):
            if num[i] == '0' and j > i + 1:
                break

            second = int(num[i:j])

            left = first
            right = second
            k = j

            while k < n:
                addition = left + right
                target = str(addition)

                if not num.startswith(target, k):
                    break

                left = right
                right = addition
                k += len(target)

            if k == n:
                return True

    return False

num = "112358"
print(isAdditiveNumber(num))