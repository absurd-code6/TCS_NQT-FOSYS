'''Given an array of integers nums and an integer threshold, we will choose 
a positive integer divisor, divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than 
or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or 
equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum 
will be 5 (1+1+1+2). 

Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
'''
import math
def Smallest_Divisor(nums:list[int],T:int)->int:
    if not nums:
        return -1
    l=1
    h=max(nums)
    ans=-1
    while l<=h:
        sum=0
        mid=(l+h)//2
        for i in nums:
            sum+=math.ceil(i/mid) #or (i + mid - 1) // mid
        if sum>T:
            l=mid+1
        else:
            ans=mid
            h=mid-1
    return ans # or l

n=int(input())
#nums=[int(input()) for _ in range(n)]
nums=[]
for _ in range(n):
    nums.append(int(input()))
T=int(input())
print(Smallest_Divisor(nums,T))
'''To understand (i + mid - 1) // mid, let's first look at what problem it solves.

In programming, we often need to divide numbers and always round up (this is 
called "ceiling division"). For example, if you are dividing 7 items into groups 
of 3, you get 2 full groups and 1 leftover item. That leftover item still needs 
its own group, so you actually have 3 groups total.

If you use normal Python integer division (7 // 3), it gives you 2 because it 
always rounds down. That would break our math!

Here is how (i + mid - 1) // mid cleverly forces Python to round up using only whole numbers:

A Quick Example
Let's pretend:

mid = 3 (the size of each group)

i = 7 (the number of items we have)

Let's plug those numbers into the formula:

mid - 1 becomes 3 - 1 = 2

i + (mid - 1) becomes 7 + 2 = 9

9 // 3 becomes 3

It correctly tells us we need 3 groups!

What if it divides evenly?
Let's test it when things divide cleanly (e.g., i = 6 items, mid = 3 items per group):

mid - 1 becomes 2

6 + 2 = 8

8 // 3 = 2 (Integer division drops the remainder, so 8 // 3 equals 2).
It correctly tells us we need 2 groups!

Why does this trick work?
Adding mid - 1 acts like a clever "nudge" or safety buffer.

If a number divides evenly, the nudge isn't quite big enough to push it to the 
next whole number.

If there is even a tiny remainder (like 1 leftover item), the nudge pushes the total 
just high enough so that // rounds it up to the next integer.

It is a neat, old-school math trick that keeps your code fast and avoids messy 
decimal errors!
Here is step-by-step how (7 + 3 - 1) // 3 gives us the rounded-up answer:

Step-by-Step Calculation
Start with the formula:

Result=(i+mid-1)//mid
Plug in 
i=7 and 
mid=3:

Result=(7+3-1)//3
Do the addition/subtraction inside the parentheses first:

7+3=10

10-1=9

Perform the integer division (//):

9//3=3
Why this works visually:
Without the trick:

7//3=2(rounds down, missing the remainder)
With the trick:

Adding 
3-1=2 turns 
7 into 
9.

Since 
9 divides cleanly by 
3, 
9//3=3.

Adding 
2 gave 
7 just enough of a bump to push it into the next multiple of 
3, forcing the division to round up!'''