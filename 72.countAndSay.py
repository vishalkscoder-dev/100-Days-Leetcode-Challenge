import os
os.system('cls')

def countAndSay(n):
    result = "1"

    for i in range(n-1):
        newResult = ""
        count = 1

        for j in range(1, len(result)+1):
            if j < len(result) and result[j] == result[j-1]:
                count += 1
            
            else:
                newResult += str(count) + result[j-1]
                count = 1
                
        result = newResult

    return result


n = 4
print(countAndSay(n))







        