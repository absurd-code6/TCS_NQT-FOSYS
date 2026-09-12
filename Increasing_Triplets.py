'''Given an integer array nums, return true if there exists a triple of 
indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), 
because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''

def Increasing_Triplets(nums):
    first=float('inf')
    second=float('inf')

    for num in nums:
        if num<=first:
            first=num
        elif num<=second:
            second=num
        else:
            return True
    return False

line=input().strip()
raw_nums=line.split('[')[1].split(']')[0]
if raw_nums:
    nums=list(map(int,raw_nums.split(',')))
else:
    nums=[]
result=Increasing_Triplets(nums)
print(str(result).lower())

'''This code solves a classic puzzle: finding out if an array contains three numbers in increasing order (i < j < k) such 
that nums[i] < nums[j] < nums[k].

float('inf') represents infinity—a number larger than any other number.

We initialize first and second to infinity because we are searching for the smallest possible candidates for our triplet. first will keep track of the smallest number seen so far, and second will keep track of the second smallest (which must come after first).

for num in nums:
    We start walking through the list of numbers, one by one.


        if num <= first:
            first = num
Step A: If the current number is smaller than or equal to first, we
update first to this new smaller number. This keeps our barrier for
entry as low as possible!


        elif num <= second:
            second = num
Step B: If the current number is larger than first but smaller than or 
equal to second, we update second. This means we've successfully 
found a pair where first < second.


        else:
            return True
Step C: If the current number is larger than both first and second, 
we found our triplet! Think about it: it is larger than second, 
and second is larger than whatever first was when second was set. 
We immediately return True.


    return False
If we check every single number in the list and never hit that 
else block, it means no such triplet exists. We return False.

Current num	Condition Triggered	Updated Variables	Explanation									
2	num <= first (2≤∞)	first = 2, second = inf	2 is the smallest number seen so far.									
1	num <= first (1≤2)	first = 1, second = inf	1 is even smaller than 2. We reset first to 1.									
5	num <= second (5≤∞)	first = 1, second = 5	5 is bigger than 1, so it fills our second slot. We now have a valid pair (1<5).									
0	num <= first (0≤1)	first = 0, second = 5	0 is smaller than 1. We update first = 0. (Note: 5 still remembers that there was a number smaller than it previously, so this is perfectly safe!)									
4	num <= second (4≤5)	first = 0, second = 4	4 is bigger than 0 but smaller than 5. We lower our second slot to 4, making it easier for a future number to beat it.									
6	else (6>0 and 6>4)	Triggers return True	6 is greater than second (4). Since second was only allowed to exist because a smaller number came before it, we have guaranteed a triplet (1,5,6 or 0,4,6).									'''