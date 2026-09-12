'''You are given an integer array nums consisting of n elements, and an integer 
k.Find a contiguous subarray whose length is equal to k that has the maximum 
average value and return this value. Any answer with a calculation error 
less than 10-5 will be accepted.
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000 '''
line1=input().split()
n=int(line1[0])
k=int(line1[1])
nums=list(map(int,input().split()))
curr_sum=sum(nums[:k])
max_sum=curr_sum
for i in range(k,n):
    curr_sum+=nums[i]-nums[i-k]
    if curr_sum>max_sum:
        max_sum=curr_sum
max_avg=max_sum/k
print(f"{max_avg:.5f}")

#Function
def Max_Avg_Subarray(nums,k):
    cur_sum=sum(nums[:k])
    max_sum=cur_sum
    for i in range(k,len(nums)):
        cur_sum+=nums[i]-nums[i-k]
        max_sum=max(max_sum,cur_sum)
    return max_sum/k

'''This code finds the maximum average of any subarray of size k using the 
sliding window technique.

Example Input
5 3
1 12 -5 -6 50

Here:

n = 5 (total numbers)
k = 3 (window size)
nums = [1, 12, -5, -6, 50]
Step 1: Calculate the first window sum
curr_sum = sum(nums[:k])

nums[:3] means the first 3 elements:

[1, 12, -5]

Their sum is:

1 + 12 + (-5) = 8

So,

curr_sum = 8
max_sum = 8

Current window:

[1, 12, -5]
Step 2: Move the window one step at a time
for i in range(k, n):

Since k = 3 and n = 5,

range(3,5)

So i will be:

3, 4
First iteration (i = 3)

Current window is

[1, 12, -5]

We now slide it to

[12, -5, -6]

Instead of adding all numbers again, the code does:

curr_sum += nums[i] - nums[i-k]

Let's substitute the values.

curr_sum += nums[3] - nums[0]
curr_sum += (-6) - (1)

Old sum:

8

New sum:

8 + (-6) - 1 = 1

Now,

curr_sum = 1

Compare:

if curr_sum > max_sum:
1 > 8 ?

No.

So,

max_sum = 8
Second iteration (i = 4)

Current window:

[12, -5, -6]

Move it one step:

[-5, -6, 50]

Again,

curr_sum += nums[4] - nums[1]

Substitute values:

curr_sum += 50 - 12

Old sum:

1

New sum:

1 + 50 - 12 = 39

So,

curr_sum = 39

Compare:

39 > 8

Yes.

Therefore,

max_sum = 39
Step 3: Calculate the maximum average
max_avg = max_sum / k
39 / 3 = 13.0

Finally,

print(f"{max_avg:.5f}")

prints

13.00000'''

#Why does this line work? Main Logic
'''curr_sum += nums[i] - nums[i-k]

Imagine the window as a train with 3 seats.

Initial window:

[1, 12, -5]

When it moves right,

[12, -5, -6]
1 leaves the window → subtract it.
-6 enters the window → add it.

So instead of recalculating

12 + (-5) + (-6)

the code simply updates the previous sum:

new_sum = old_sum - outgoing + incoming

This is much faster because each move takes only one addition and one 
subtraction, instead of summing all k elements again.'''

'''Dry Run Table
Iteration	Window	curr_sum	max_sum
Initial	[1, 12, -5]	8	8
i = 3	[12, -5, -6]	1	8
i = 4	[-5, -6, 50]	39	39

The largest window sum is 39, so the maximum average is:

39 ÷ 3 = 13.00000'''

#This is the essence of the sliding window technique: reuse the 
#previous window's sum by removing the element that leaves 
#the window and adding the new element that enters it.'''