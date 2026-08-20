import os
os.system('cls')

def reverseWords( s):
    words = s.strip()
    listing = words.split(" ")

    left = 0
    right = len(listing)-1

    while left < right:
        listing[left], listing[right] = listing[right], listing[left]

        left += 1
        right -= 1

    result = " ".join(listing)        
    final = " ".join(result.split())

    return final

s = "the sky is blue"
print(reverseWords(s))