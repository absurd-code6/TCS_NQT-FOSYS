'''Stickler the thief wants to loot money from the houses arranged in a line. 
He cannot loot two consecutive houses and aims to maximize his total loot.
Given an array, arr[] where arr[i] represents the amount of money 
in the i-th house. Determine the maximum amount he can loot.

Examples:

Input: arr[] = [6, 7, 1, 3, 8, 2, 4]
Output: 19
Explanation: Maximum amount he can get by looting 1st, 3rd, 5th and 7th house, which is 6 + 1 + 8 + 4 = 19.
Input: arr[] = [5, 3, 4, 11, 2]
Output: 16
Explanation: Maximum amount he can get by looting 1st and 4th house, which is 5 + 11 = 16.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104'''

def Stickler(house_prices):
    # Edge case: If there are no houses, there's nothing to loot!
    if not house_prices:
        return 0
    # Edge case: If there is only 1 house, take it.
    if len(house_prices)==1:
        return house_prices[0]
    
    prev1=house_prices[0]
    prev2=house_prices[1]
    for i in range(2,len(house_prices)):
        curr_max=max(house_prices[i]+prev2,prev1)
        
        prev2=prev1
        prev1=curr_max
    return prev1

arr=list(map(int,input().split()))
print(f"Maximized loot is: {Stickler(arr)}")
        
"""Step 1: Understand the Core DecisionImagine you are Stickler 
the thief, standing in front of the very last house in the line. 
You have a choice to make for this specific house:You LOOT this house: 
If you choose to loot it, you get its money. 
But because of the alarm system, you cannot have 
looted the house right before it. That means your 
total money will be: 
Current House Money + Maximum money from 2 houses ago.You SKIP this house: 
If you skip it, you don't get its money. 
However, you are safe to take whatever the 
maximum loot was up to the immediate previous house.
Your goal is to maximize profit, so you will naturally c
hoose the maximum of those two choices.

Step 2: Scale it Down (Start Small)Let's look at how the decision 
builds up using a tiny version of the problem: 
arr = [6, 7, 1]House 0 (Value 6): Only one house. Easy choice.
Max money = 6.House 1 (Value 7): Two houses. 
You can't pick both. Which is bigger, 6 or 7? 
Max money = 7.House 2 (Value 1): Now we apply our rule from Step 1.
Option A (Loot it): 
Value of this house (1) + Max money from House 0 (6) = 7.
Option B (Skip it): Max money up to House 1 = 7.
The max of Option A and B is 7.Do you see the pattern? 
To know the answer for the current house, we only ever 
need to know two things: the answer for the 
previous house and the answer for the house before that.

Step 3: Translating Logic into Code VariablesInstead of keeping 
track of the whole street, we only need to keep track of 
two moving numbers as we walk down the line:prev2: 
The max money we could make up to 2 houses ago.prev1: 
The max money we could make up to 1 house ago.
As we move to a new house, 
the new maximum becomes:
max(current house + prev2,prev1)
Then, we just shift our focus forward! prev2 becomes what 
prev1 was, and prev1 becomes the new maximum we just calculated."""  
#Example
'''House Index (i)	House Value	Loot Option (arr[i] + prev2)	Skip Option (prev1)	current_max	New prev2	New prev1
Start	—	—	—	—	6	7
2	1	1 + 6 = 7	7	7	7	7
3	3	3 + 7 = 10	7	10	7	10
4	8	8 + 7 = 15	10	15	10	15
5	2	2 + 10 = 12	15	15	15	15
6	4	4 + 15 = 19	15	19	15	19'''