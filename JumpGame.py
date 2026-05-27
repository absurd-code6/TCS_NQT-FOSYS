'''Jump Game - Minimum Jumps to Reach End
Last Updated : 3 Apr, 2026
Given an array arr[] of non-negative integers, where each element represents 
the maximum number of steps you can jump forward from that index, determine 
the minimum number of jumps required to reach the last index starting 
from the first index. If it is not possible to reach the end, return -1.

Examples: 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 

Input: arr []= [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

Input: arr[] = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.

Table of Content

[Naive] Using Recursion - O(n^n) Time and O(n) Space
[Better] Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space
[Expected] Using Greedy Approach - O(n) Time and O(1) Space
'''
def minJump(arr):
    if len(arr)==1:
        return 0
    if arr[0]==0:
        return -1
    reach=arr[0]
    steps=arr[0]
    jumps=1
    for i in range(1,len(arr)):
        if i==len(arr)-1:
            return jumps
        reach=max(reach,i+arr[i])
        steps-=1
        if steps==0:
            jumps+=1
            if i>=reach:
              return -1
            steps=reach-i
    return -1

#arr=list(map(int,input().split())) 
arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Min jumps required:",minJump(arr))

'''Example Walkthrough

Consider:

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

Index positions:

Index: 0 1 2 3 4 5 6 7 8 9 10
Value: 1 3 5 8 9 2 6 7 6 8 9
Initial State

We start at index 0.

reach = arr[0] = 1
steps = arr[0] = 1
jumps = 1

Meaning:

With 1 jump, we can currently reach up to index 1.
Iteration 1 → i = 1

Current element:

arr[1] = 3
Update reach
reach = max(1, 1 + 3)
       = 4

Now we can reach up to index 4.

Consume one step
steps -= 1
steps = 0

We used all steps from the previous jump.

Need another jump
jumps += 1
jumps = 2

Now calculate new steps:

steps = reach - i
       = 4 - 1
       = 3

So with the second jump, we can move 3 more positions.

State After i = 1
Variable	Value
reach	4
steps	3
jumps	2
Iteration 2 → i = 2
arr[2] = 5
Update reach
reach = max(4, 2 + 5)
       = 7

Now farthest reachable index is 7.

Consume step
steps = 2
Iteration 3 → i = 3
arr[3] = 8
Update reach
reach = max(7, 3 + 8)
       = 11

Great! We can now theoretically go beyond the last index.

Consume step
steps = 1
Iteration 4 → i = 4
arr[4] = 9
Update reach
reach = max(11, 4 + 9)
       = 13
Consume step
steps = 0

Need another jump.

jumps = 3

New steps:

steps = reach - i
       = 13 - 4
       = 9
Continue...

Eventually we reach:

i == n - 1

which is index 10.

So return:

return jumps

Output:

3

The Meaning of steps
steps

represents:

How many more indices we can move before we MUST take another jump.

Think of it like fuel for the current jump.

Example
arr = [1, 3, 5, 8, 9]
Initial State

At index 0:

arr[0] = 1

This means:

from index 0
we can move at most 1 step forward

So:

steps = 1
Why Do We Decrease steps?

Every time we move one index ahead:

steps -= 1

because we used one step from the current jump.

Dry Run
Start
Index	steps
0	1

We move from index 0 → 1.

That movement consumes one step.

So:

steps -= 1
steps = 0

Now:

Index	steps
1	0
What Does steps == 0 Mean?

It means:

The current jump cannot take us any further.

So now we are forced to make another jump.

Then Why Increase jumps?
jumps += 1

Because we are starting a NEW jump range.

Then Why:
steps = reach - i

This is the tricky but important part.

Understanding reach

reach stores:

the farthest index we can reach so far.

Suppose:

reach = 4
i = 1

Meaning:

while exploring previous indices,
we found that index 4 is the farthest reachable place.

Currently we are at index 1.

So from here, how many more indices can we travel?

4 - 1 = 3

Thus:

steps = reach - i

means:

"In this new jump, we can still move 3 more positions."

Full Visualization

Suppose:

arr = [1, 3, 5, 8, 9]
At index 0
reach = 1
steps = 1
jumps = 1

Range covered by current jump:

[0 ---- 1]
Move to index 1

We consume one step:

steps = 0

Current jump ends here.

Now from index 1:

arr[1] = 3

we can reach:

1 + 3 = 4

So:

reach = 4

Now we start another jump:

jumps = 2

How many steps are available in this new jump?

Current position:

i = 1

Farthest reachable:

reach = 4

Remaining distance:

4 - 1 = 3

So:

steps = 3

Now the new jump covers:

[1 -------- 4]

if i >= reach:
    return -1
What does reach mean?

reach = farthest index reachable so far.

What does i mean?

i = current index where we are standing.

So What Does:
i >= reach

mean?

It means:

We cannot move beyond the current position.

We are stuck.

Example
arr = [1, 0, 0, 0]
Initial Values
reach = 1
steps = 1
jumps = 1
Move to index 1
i = 1

Update reach:

reach = max(1, 1 + arr[1])
       = max(1, 1 + 0)
       = 1

Reach is still 1.

Consume step:

steps = 0

Now we need another jump.

Check:
if i >= reach

Substitute values:

1 >= 1

TRUE.

Meaning:

current position is the farthest possible position
cannot go further
destination is unreachable
Visual Understanding
Index: 0 1 2 3
Value: 1 0 0 0

From index 0, we can only reach index 1.

At index 1, value is 0.

So movement stops forever.'''
