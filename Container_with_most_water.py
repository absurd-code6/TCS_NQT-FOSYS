'''You are given an integer array height of length n. There are n 
vertical lines 
drawn such that the two endpoints of the ith line are 
(i, 0) 
and (i, height[i]).

Find two lines that together with the x-axis form a container, such that 
the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
 
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
'''
n=int(input())
ht=list(map(int,input().split()))
left=0
right=n-1
max_water=0
while left<right:
    width=right-left
    curr_ht=min(ht[left],ht[right])
    curr_water=width*curr_ht
    if curr_water>max_water:
        max_water=curr_water
    if ht[left]<ht[right]:
        left+=1
    else:
        right-=1
print(max_water)

'''Step 1: Input
n = int(input())

Takes the number of heights.

Example:

8

So,

n = 8
ht = list(map(int, input().split()))

Reads all heights into a list.

Example input:

1 8 6 2 5 4 8 3

So,

ht = [1,8,6,2,5,4,8,3]

Imagine these as vertical lines.

Height

8        |           |
7        |           |
6      | |           |
5      | |     |     |
4      | |     | |   |
3      | |     | |   |
2      | | |   | |   |
1 |    | | | | | | | |
  -----------------------
  0 1 2 3 4 5 6 7
Step 2: Initialize pointers
left = 0
right = n-1

Initially,

left = 0
right = 7

Pointers are at both ends.

L                     R

1 8 6 2 5 4 8 3
^             ^
max_water = 0

Initially,

max_water = 0
Step 3: Loop
while left < right:

Keep moving until pointers meet.

Dry Run
Iteration 1
left = 0
right = 7

Heights are

1 and 3

Width

width = right-left
width = 7

Current height

curr_ht = min(ht[left], ht[right])
min(1,3)=1

Water

curr_water = width * curr_ht
7 x 1 = 7
max_water = max(0,7)=7

Picture

1                     3

|                     |
|_____________________|

width = 7
height = 1
water = 7

Now compare heights.

1 < 3

Move the smaller one.

left +=1

Now

left =1
Iteration 2

Pointers

8                     3

L                     R

Width

7-1 = 6

Height

min(8,3)=3

Water

6x3=18
max_water=18

Now

8 > 3

Move the smaller height.

right -=1

Now

right=6
Iteration 3

Pointers

8                 8

L                 R

Width

6-1=5

Height

min(8,8)=8

Water

5x8=40
max_water=40

Since

8 == 8

The code executes

right -=1

Now

right=5
Iteration 4

Pointers

8           4

Width

5-1=4

Height

min(8,4)=4

Water

4x4=16

Maximum remains

40

Move smaller

right=4
Iteration 5

Pointers

8         5

Width

3

Height

5

Water

15

Maximum

40

Move smaller

right=3
Iteration 6

Pointers

8     2

Width

2

Height

2

Water

4

Move smaller

right=2
Iteration 7

Pointers

8   6

Width

1

Height

6

Water

6

Move smaller

right=1

Now

left==right

Loop ends.

Final Answer
max_water = 40

Output

40
Why do we move the smaller height?

Suppose we have

2                 9

Area is

width x min(2,9)

The shorter line (2) limits the water. Even if the taller line is 
very high, the water cannot rise above height 2.

If we move the taller line inward:

Width decreases.
Limiting height (2) stays the same.
The area cannot increase.

But if we move the shorter line, we might find a taller line that 
increases the limiting height enough to produce a larger area 
despite the reduced width.

This is the key insight behind the two-pointer approach.

Time Complexity

The pointers move toward each other only once.

Time: O(n) (each pointer moves at most n times)
Space: O(1) (only a few extra variables are used)

This is much faster than checking every pair of lines, 
which would take O(n²) time.'''