'''You have a long flowerbed in which some of the plots are planted, and 
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means 
empty and 1 means not empty, and an integer n, return true if n new 
flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
#Greedy Algorithm
def cp_flowers(flowerbed,n):
    count=0
    length=len(flowerbed)
    for i in range(length):
        if flowerbed[i]==0:
            left_empty=(i==0) or (flowerbed[i-1]==0)
            right_empty=(i==length-1) or (flowerbed[i+1]==0)
            if left_empty and right_empty:
                flowerbed[i]=1
                count+=1
                if count>=n:
                    return True
    return count>=n
data=list(map(int,input().split()))
size=data[0]
flowerbed=data[1:size+1]
n=data[-1]
res=cp_flowers(flowerbed,n)
print(str(res).lower())

'''1. Step-by-Step Code Explanation
The Main Logic (cp_flowers function)
count = 0: A counter to keep track of how many new flowers we have 
successfully planted so far.

length = len(flowerbed): Finds out how many total plots are in our flowerbed.

for i in range(length):: Loops through the flowerbed, 
checking each plot one by one using its index i.

if flowerbed[i] == 0:: We can only plant a flower if the 
current plot is empty (0).

left_empty = (i == 0) or (flowerbed[i-1] == 0): To plant a 
flower, the left side must be empty. This line checks 
if we are either at the very first plot (i == 0, meaning there is no left neighbor) OR if the plot to the left is empty (flowerbed[i-1] == 0).

right_empty = (i == length-1) 
⚠️ THE BUG IS HERE: The code says the right side is empty
only if we are at the very last plot (i == length-1). 
It completely forgets to check if the next plot is 0!

How to fix it: It should be right_empty = (i == length-1) or (
    flowerbed[i+1] == 0).

if left_empty and right_empty:: If both neighbors (left and right) are safe, 
we can plant!

flowerbed[i] = 1: We plant a flower here so future checks know 
it's occupied. count += 1: We increment our counter.

if count >= n: return True: A quick shortcut. If we've already 
planted enough flowers (n), we stop immediately and return True.

return count >= n: If the loop finishes and we didn't hit the shortcut, 
we check if the final count is enough.

The Input Setup (Bottom lines)
data = list(map(int, input().split())): Takes a line of numbers 
from the user and turns it into a list of integers.

size = data[0]: Assumes the first number you type is the size of the flowerbed.

flowerbed = data[1:size+1]: Grabs the actual flowerbed plots based on that size.

n = data[-1]: Grabs the very last number, which is how many flowers 
you want to plant.

Loop Index (i)	Plot Value flowerbed[i]	Left Check (left_empty)	Right Check (right_empty)	Action Taken / Result			
i = 0	1	Skipped (Not 0)	Skipped	Can't plant. Moving on.			
i = 1	0	False (Left neighbor is 1)	True (Next is 0)	Cannot plant here.			
i = 2	0	True (Left is 0)	True (Right is 0)	Plant! Bed becomes [1, 0, 1, 0, 1]. count becomes 1.'''