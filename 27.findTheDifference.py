import os
os.system('cls')

def findTheDifference(s, t):
    count = {}

    for ch in s:
        count[ch] = count.get(ch,0)+1

    for ch in t:
        if ch not in count:
            return ch

        count[ch] -= 1

        if count[ch] < 0:
            return ch

s = "abcd" 
t = "abcde"

print(findTheDifference(s,t))