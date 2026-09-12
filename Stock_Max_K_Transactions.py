'''You are given:
An integer k (maximum number of transactions allowed).
An array prices where prices[i] is the stock price on day i.
You can perform at most k transactions, and you must sell before
buying again (no overlapping transactions).
Each transaction consists of:

One buy
One sell
Your goal is to compute the maximum profit you can earn 
from these transactions. '''

def max_profit(k, prices):
    n = len(prices)
    if n == 0 or k == 0:
        return 0

# Optimization when k is larger than possible non-overlapping transactions
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # buy[i] stores the max balance after i-th purchase
    # sell[i] stores the max balance after i-th sale
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - price)
            sell[t] = max(sell[t], buy[t] + price)

    return sell[k]


# --- Input Handling for the Platform ---
if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().split()
    if input_data:
        k = int(input_data[0])
        n = int(input_data[1])
        prices = [int(x) for x in input_data[2:]]
        print(max_profit(k, prices))

'''Think of this algorithm as keeping track of your bank 
balance across k potential trades. You start with 0. 
Every time you buy a stock, you spend money (balance decreases), 
and every time you sell, you gain money (balance increases).
Here is a step-by-step breakdown of how the logic works, 
followed by a dry run.

1. Edge Cases & Fast-Track Optimizationif n == 0 or k == 0: 
If there are no days/prices or you're allowed 0 transactions, 
your profit is 0. 
if k >= n // 2: You can buy on one day and sell on the next at 
most n/2 times. If k is greater than or equal to 
half the number of days, k is no longer a restriction! 
You can simply grab every positive price 
jump(buy low today, sell high tomorrow).

2. Tracking Balances (buy and sell lists)When k is limited, 
we use dynamic programming:buy[t]: The maximum money in your 
pocket after completing your $t$-th buy. (This will usually be 
negative early on, because you just spent money).sell[t]: 
The maximum money in your pocket after completing your t-th sell.

At any given day's price, for transaction number t:

buy[t] = max(buy[t], sell[t - 1] - price)

Option A: Do nothing today (keep previous buy[t]).

Option B: Buy today using money made from the previous 
completed sale (sell[t-1] - price).

sell[t] = max(sell[t], buy[t] + price)

Option A: Do nothing today (keep previous sell[t]).

Option B: Sell today at price using the stock bought in 
transaction t (buy[t] + price).

Step-by-Step Dry RunLet's trace the execution with an example 
where k = 2 and prices = [2, 4, 1, 5].
Setup k = 2, n = 4.Is k > n // 2? (2 > 2) Yes! 
The optimization block triggers!
Since the code hits if k >= n // 2:, let's trace that loop:
Initial state: profit = 0D ay 1 to 2 (i=1, prices[1] = 4, prices[0] = 2):
4 > 2 -> Profit increases by (4 - 2) = 2.profit = 2 
Day 2 to 3 (i=2, prices[2] = 1, prices[1] = 4): 1 < 4 Price dropped, 
do nothing.
Day 3 to 4 ($i=3$, prices[3] = 5, prices[2] = 1):$5 > 1 -> 
Profit increases by (5 - 1) = 4.profit = 2 + 4 = 6
Result: 6

Dry Run of the DP State (When k < n // 2)
To see how buy and sell arrays update, let's 
trace prices = [3, 2, 6, 50] with k = 1 (k < 4 // 2):
Initialization: buy = [-inf, -inf]sell = [0, 0]

Day 1: price = 3t = 1:buy[1] = max(-inf, sell[0] - 3) -> 
max(-inf, 0 - 3) = -3sell[1] = max(0, buy[1] + 3) -> 
max(0, -3 + 3) = 0

Day 2: price = 2t = 1:buy[1] = max(-3, 0 - 2) -> -2 
(Better to buy at 2 than 3!)
sell[1] = max(0, -2 + 2) -> 0

Day 3: price = 6t = 1:buy[1] = max(-2, 0 - 6) -> -2 (Keep buying at 2)
sell[1] = max(0, -2 + 6) -> 4 (Sell today at 6 for profit of 4)

Day 4: price = 50t = 1:buy[1] = max(-2, 0 - 50) ->
-2sell[1] = max(4, -2 + 50) -> 48 
(Sell today at 50 for profit of 48)

Final Output: return sell[1] -> 48
'''