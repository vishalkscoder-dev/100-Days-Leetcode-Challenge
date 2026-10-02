import subprocess
subprocess.run('cls', shell=True)

"""

    1000 → M
    900  → CM
    500  → D
    400  → CD
    100  → C
    90   → XC
    50   → L
    40   → XL
    10   → X
    9    → IX
    5    → V
    4    → IV
    1    → I

"""

def integerToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    result = ""
    
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]

    return result

num = 6732
print(integerToRoman(num))























