import subprocess
subprocess.run('cls', shell=True)

def findSubstring(s, words):
    left = 0
    result = []
    wordLength = len(words[0])
    right = len(words) * wordLength

    freq2 = {}

    for word in words:
        freq2[word] = freq2.get(word, 0) + 1

    while right <= len(s):
        concat = s[left:right]

        freq1 = {}

        for i in range(0, len(concat), wordLength):
            word = concat[i:i + wordLength]
            freq1[word] = freq1.get(word, 0) + 1

        if freq1 == freq2:
            result.append(left)

        left += 1
        right += 1
        
    return result 

s = "barfoothefoobarman"
words = ["foo","bar"]

print(findSubstring(s, words))