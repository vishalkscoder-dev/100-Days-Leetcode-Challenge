import os
os.system('cls')

def maxProfit(prices):
    left = 0
    right = 1
    profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit += prices[right] - prices[left]

        left = right
        right = right + 1

    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))