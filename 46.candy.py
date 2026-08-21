import os
os.system('cls')

def candy(ratings):
    ratingsLength = len(ratings)
    candy = []

    for i in range(0, ratingsLength):
        candy.append(1)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1]+1
        
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            maximum = max(candy[i],candy[i+1]+1)
            candy[i] = maximum

    count = 0

    for num in candy:
        count += num

    return count

ratings = [1,0,2]
print(candy(ratings))