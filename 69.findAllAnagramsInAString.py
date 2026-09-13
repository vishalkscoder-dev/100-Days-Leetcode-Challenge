import os
os.system('cls')

def findAnagrams(s, p):
    length = len(p)

    result = []
    sortedP = sorted(p)

    for i in range(len(s)-length+1):
        substring = s[i:i+length]

        if sorted(substring) == sortedP:
            result.append(i)

    return result
 
s = "cbaebabacd"
p = "abc"

print(findAnagrams(s,p))