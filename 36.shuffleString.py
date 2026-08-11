import os
os.system('cls')

def restoreString(s, indices):
    result = [""] * len(s)

    for i in range(len(indices)):
        result[indices[i]] = s[i]

    answer = "".join(result)
    
    return answer

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s,indices))