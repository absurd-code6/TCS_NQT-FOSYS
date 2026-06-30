'''Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].
You must write an algorithm that runs in O(n) time and without 
using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
'''

def productExceptItself(nums):
    n=len(nums)
    answer=[1]*n
    prefix=1
    for i in range(n):
        answer[i]=prefix
        prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        answer[i]*=suffix
        suffix*=nums[i]
    return answer
_=input()
nums=list(map(int,input().split()))
result=productExceptItself(nums)
print(*result)

'''Main Idea

Instead of multiplying all numbers again and again (which is slow), the algorithm breaks the work into two parts:

Product of everything to the left (Prefix)
Product of everything to the right (Suffix)

Then,

Answer = Prefix x Suffix
Step 1: Initialization

Suppose

nums = [1, 2, 3, 4]
n = len(nums)
n = 4
answer = [1] * n

Creates

answer = [1,1,1,1]

Why all 1s?

Because 1 is the multiplicative identity.

Step 2: Prefix Pass
prefix = 1

Initially,

prefix = 1

Now the loop

for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

Let's dry run.

Iteration 1
i = 0

Current prefix

prefix = 1

Store it

answer[0] = 1

Now

answer = [1,1,1,1]

Update prefix

prefix = prefix x nums[0]
       = 1 x 1
       = 1
Iteration 2
i = 1

Current prefix

1

Store

answer[1] = 1

Update prefix

1 x 2 = 2

Now

prefix = 2
Iteration 3
i = 2

Store

answer[2] = 2

Update prefix

2 x 3 = 6

Now

prefix = 6
Iteration 4
i = 3

Store

answer[3] = 6

Update prefix

6 x 4 = 24

End of first loop.

Current answer:

[1,1,2,6]
Meaning

Each position now stores the product of all numbers before it.

Index	Left numbers	Product
0	None	1
1	1	1
2	1,2	2
3	1,2,3	6
Step 3: Suffix Pass

Now we move from right to left.

suffix = 1

Initially

suffix = 1

Loop

for i in range(n-1,-1,-1):
    answer[i] *= suffix
    suffix *= nums[i]
Iteration 1
i = 3

Current suffix

1

Multiply

answer[3] = 6 x 1
          = 6

Update suffix

1 x 4 = 4

Now

suffix = 4

Answer

[1,1,2,6]
Iteration 2
i = 2

Current suffix

4

Multiply

answer[2] = 2 x 4
          = 8

Update suffix

4 x 3 = 12

Now

suffix = 12

Answer

[1,1,8,6]
Iteration 3
i = 1

Current suffix

12

Multiply

answer[1] = 1 x 12
          = 12

Update suffix

12 x 2 = 24

Now

suffix = 24

Answer

[1,12,8,6]
Iteration 4
i = 0

Current suffix

24

Multiply

answer[0] = 1 x 24
          = 24

Update suffix

24 x 1 = 24

Final answer

[24,12,8,6]
Complete Dry Run Table
Prefix Pass
i	prefix before	answer	prefix after
0	1	[1,1,1,1]	1
1	1	[1,1,1,1]	2
2	2	[1,1,2,1]	6
3	6	[1,1,2,6]	24
Suffix Pass
i	suffix before	answer	suffix after
3	1	[1,1,2,6]	4
2	4	[1,1,8,6]	12
1	12	[1,12,8,6]	24
0	24	[24,12,8,6]	24
Why Does This Work?

For every index:

Product except itself
=
(Product of all elements on the left)
x
(Product of all elements on the right)

For index 2:

nums = [1,2,3,4]
           ^

Left product

1 × 2 = 2

Right product

4

Multiply

2 × 4 = 8

Exactly what we want.

Time and Space Complexity
Time Complexity: O(n) because the array is traversed twice 
(both passes are linear).'''