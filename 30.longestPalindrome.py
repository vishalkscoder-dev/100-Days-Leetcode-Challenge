import os
os.system('cls')


def longestPalindrome(s):
    freq = {}
    count = 0
    odd = False

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for value in freq.values():
        if value % 2 == 0:
            count += value
        else:
            count += value - 1
            odd = True

    if odd:
        count += 1

    return count

s = "abccccdd"
print(longestPalindrome(s))