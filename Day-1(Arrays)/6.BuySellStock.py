# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def buysell(a):
    profit = 0
    maxProfit = 0
    for i in range(1,len(a)):
        profit += a[i]-a[i-1]
        profit = max(profit,0)
        maxProfit = max(maxProfit, profit)

    return maxProfit

print(buysell([7,1,5,3,6,4]))
print(buysell([7,6,4,3,1]))
print(buysell([1,2,3,4,5,6,7]))