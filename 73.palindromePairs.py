import os
os.system('cls')

def palindromePairs(words):
    result = []
    wordMap = {}

    for i in range(len(words)):
        wordMap[words[i]] = i

    for i in range(len(words)):
        word = words[i]

        for j in range(len(word) + 1):
            left = word[:j]
            right = word[j:]

            if left == left[::-1]:
                reverse = right[::-1]

                if reverse in wordMap and wordMap[reverse] != i:
                    result.append([wordMap[reverse], i])

            if j != len(word) and right == right[::-1]:
                reverse = left[::-1]

                if reverse in wordMap and wordMap[reverse] != i:
                    result.append([i, wordMap[reverse]])

    return result

words = ["abcd","dcba","lls","s","sssll"]
print(palindromePairs(words))