import os
os.system('cls')

def isIsomorphic(s, t):
    sMap = {}
    tMap = {}

    for a, b in zip(s, t):

        if a in sMap and sMap[a] != b:
            return False

        if b in tMap and tMap[b] != a:
            return False

        sMap[a] = b
        tMap[b] = a

    return True

s = "paper"
t = "title"

print(isIsomorphic(s,t))