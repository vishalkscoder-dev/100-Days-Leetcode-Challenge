import subprocess
subprocess.run('cls', shell=True)

def isMatch(s, p):
    if p == ".*":
        return True

    i = 0
    j = 0

    while i < len(s) and j < len(p):

        if j + 1 < len(p) and p[j + 1] == "*":
            while i < len(s) and (s[i] == p[j] or p[j] == "."):
                i += 1
            j += 2

        elif s[i] == p[j] or p[j] == ".":
            i += 1
            j += 1

        else:
            return False

    while j + 1 < len(p) and p[j + 1] == "*":
        j += 2

    return i == len(s) and j == len(p)

s = "aa"
p = ".*"

print(isMatch(s,p))