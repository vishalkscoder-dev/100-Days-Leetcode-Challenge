import os
os.system('cls')

def isSubsequence(s, t):
    j = 0

    for ch in t:
        if j < len(s) and s[j] == ch:
            j += 1

    return len(s) == j


s = "abc"
t = "ahbgdc"

print(isSubsequence(s,t))