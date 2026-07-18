import os
os.system('cls')

def groupAnagrams(strs):
    dictionary = {}

    for i in strs:
        sorting = "".join(sorted(i))
        
        if sorting not in dictionary:
            dictionary[sorting] = [i]
        else:
            dictionary[sorting].append(i)
    
    return list(dictionary.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))