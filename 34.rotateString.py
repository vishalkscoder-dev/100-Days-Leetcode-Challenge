import os
os.system('cls')

def rotateString(s, goal):

    if len(s) != len(goal):
        return False

    addTheStrings = s + s

    if goal in addTheStrings:
        return True

    return False

s = "abcde"
goal = "cdeab"

print(rotateString(s,goal))