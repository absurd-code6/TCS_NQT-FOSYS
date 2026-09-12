'''We define a harmonious array as an array where the difference between 
its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest 
harmonious subsequence among all its possible subsequences.
Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], 
all of which have a length of 2.
Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

'''
from collections import Counter
def Harmonious(nums):
    counts = Counter(nums)
    res = 0

    for num in counts:
        # Check if the adjacent key exists
        if num + 1 in counts:
            # Combine frequencies of 'num' and 'num + 1'
            res = max(res, counts[num] + counts[num + 1])

    return res

nums=list(map(int,input().split(",")))
print(Harmonious(nums))

'''Dry Run Example
Let's walk through the code step-by-step using this input:
nums = [1, 3, 2, 2, 5, 2, 3, 7]

Step 1: Count Frequencies
The Counter(nums) line creates a frequency map of all unique numbers
Number(num) Count(counts[num])
1	                 1
3	                 2
2                    3	
5	                 1
7                    1

We also start with res = 0.
Step 2: Loop Through Unique NumbersWe check each unique number in counts one by one:
Checking num = 1:Is 1 + 1 (which is 2) in our counts? Yes!
Combine counts: counts[1] + counts[2] -> 1 + 3 = 4 
Update result: res = max(0, 4) = 4

Checking num = 3: Is 3 + 1 (which is 4) in our counts? No.
Skip to the next number.

Checking num = 2:
Is 2 + 1 (which is 3) in our counts? Yes!
Combine counts: counts[2] + counts[3] -> 3 + 2 = 5 
Update result: res = max(4, 5) = 5 
Checking num = 5:Is 5 + 1 (which is 6) in our counts? No.

Checking num = 7:
Is 7 + 1 (which is 8) in our counts? No.

Final OutputAfter checking every number, the function returns res = 5.
This corresponds to collecting all three 2s and both 3s from the 
original list to form the harmonious sub-collection [2, 2, 2, 3, 3].
'''
