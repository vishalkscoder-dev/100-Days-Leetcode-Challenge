import os
os.system('cls')

def lengthOfLongestSubstring(s):
    resultSet = set()

    result = 0
    l = 0

    for i in range(0,len(s)):
        while s[i] in resultSet:
            resultSet.remove(s[l])
            l += 1
        resultSet.add(s[i])
        result = max(result, i-l+1)

    return result

s = "abcabcbb"
print(lengthOfLongestSubstring(s))