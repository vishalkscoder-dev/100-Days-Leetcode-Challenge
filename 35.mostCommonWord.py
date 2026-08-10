import os, string
os.system('cls')

def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()

    freq = {}

    for ch in string.punctuation:
        paragraph = paragraph.replace(ch, " ")

    words = paragraph.split()

    for word in words:
        if word not in banned:
            freq[word] = freq.get(word, 0) + 1

    result = ""
    maximum = 0

    for key,value in freq.items():
        if value > maximum:
            result = key
            maximum = value

    return result

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))