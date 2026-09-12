#Given an array prices[] of non-negative integers, representing 
# the prices of the stocks on different days, find the maximum 
# profit possible by buying and selling the stocks on different days when 
# at most one transaction is allowed. Here one transaction 
# means 1 buy + 1 Sell. If it is not possible to make a profit 
# then return 0.

# Note: Stock must be bought before being sold.

'''Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, 
we can make maximum profit by buying at price[0] and selling 
at price[n-1]
'''

def stock_max_profit(prices):
    n=len(prices)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            res=max(res,prices[j]-prices[i])
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(stock_max_profit(prices))
    