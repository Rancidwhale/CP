def maxProfit(prices):
    profit = 0
    b=prices[0]
    for i in prices[1:]:
        if i< b:
            b=i
        profit = max(profit, i-b)
    return profit

print(maxProfit([7,6,4,3,1]))