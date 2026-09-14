import os
os.system('cls')


def generateParenthesis(n):
    result = []

    def backtracking(s, open, close):
        if len(s) == 2 * n:
            return result.append(s)

        if open < n:
            backtracking(s + "(", open+1, close)

        if close < open:
            backtracking(s + ")", open, close+1)

    backtracking("", 0, 0)

    return result

n = 3
print(generateParenthesis(n))










