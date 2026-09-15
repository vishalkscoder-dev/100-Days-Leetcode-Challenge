import os
os.system('cls')

def reverse(x):
    sign = 1 if x>0 else -1
    string = list(str(x))

    if string[0] == "-":
        del string[0]

    reverse = string[::-1]
    reverse = "".join(reverse)

    reverse = int(reverse)

    rev = sign * reverse

    if rev < -2**31 or rev > 2**31-1:
        return 0
    
    return rev

x = -526
print(reverse(x))









































