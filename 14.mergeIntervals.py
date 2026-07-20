import os
os.system('cls')

def mergeIntervals(Intervals):
    Intervals.sort(key=lambda x:x[0])

    result = [Intervals[0]]

    for start,end in Intervals[1:]:
        prevInterval = result[-1]

        if start <= prevInterval[1]:
            result[-1][1] = max(end, prevInterval[1])
        else:
            result.append([start, end])
    
    return result


Intervals = [[4,7],[1,4]]
print(mergeIntervals(Intervals))