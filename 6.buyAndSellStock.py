import os
os.system('cls')


def buyAndSell(prices):
    left = 0
    right = 1
    maximum = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]

            if profit > maximum:
                maximum = profit

        else:
            left = right

        right += 1

    return maximum

prices = [7,1,5,3,6,4]
print(buyAndSell(prices))

