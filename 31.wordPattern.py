import os
os.system('cls')

def wordPattern(pattern, s):
    string = s.split(" ")   
    
    if len(string) != len(pattern):
        return False

    for i in range(len(pattern)-1):
        for j in range(i+1,len(pattern)):
            if pattern[i] == pattern[j]:
                if string[i] != string[j]:
                    return False

            if string[i] == string[j]:
                if pattern[i] != pattern[j]:
                    return False
                    
    return True

string = "abba"
pattern = "dog dog cat dog"

print(wordPattern(string, pattern))
                    

        