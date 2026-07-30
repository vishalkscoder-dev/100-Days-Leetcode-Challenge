import os
os.system('cls')

def firstOccurence(n,m,haystack, needle):

    for i in range(n-m+1):
        if haystack[i:i+m] == needle:
            return i

    return -1

haystack = "sadbutsad"
needle = "sad"

n = len("sadbutsad")
m = len("sad") 

print(firstOccurence(n, m, haystack, needle))