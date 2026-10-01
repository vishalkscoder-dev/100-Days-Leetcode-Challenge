import subprocess
subprocess.run('cls', shell=True)

def fullJustify(words, maxWidth):
    result = []
    i = 0

    while i < len(words):
        line = []
        length = 0

        while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
            line.append(words[i])
            length += len(words[i])
            i += 1

        if i == len(words) or len(line) == 1:
            text = " ".join(line)
            result.append(text + " " * (maxWidth - len(text)))
            continue

        spaces = maxWidth - length
        gaps = len(line) - 1

        each = spaces // gaps
        extra = spaces % gaps

        text = ""

        for j in range(len(line) - 1):
            text += line[j]
            text += " " * (each + (1 if j < extra else 0))

        text += line[-1]
        result.append(text)

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(fullJustify(words, maxWidth))