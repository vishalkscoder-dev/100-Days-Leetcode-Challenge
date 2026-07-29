import os
os.system('cls')

def validParenthesis(s):
    stack = []
    dictionary = {"{":"}", "(":")", "[":"]"}

    for i in s:
        if i in dictionary.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                if dictionary[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

    if stack == []:
        return True
    else:
        return False

s = "()[]{}"
# s = ")[{}"

print(validParenthesis(s))


























