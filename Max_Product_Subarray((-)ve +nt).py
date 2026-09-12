'''Given an array of N integers 
(which may include negative numbers and zeros), find and print 
the largest product obtainable from any contiguous non-empty subarray.
For example — for the array [2, 3, -2, 4], the contiguous 
subarray [2, 3] gives the maximum product, 6. 
(Including -2 would flip the sign, and the 4 is isolated by the negative.)

Requirement: Your solution must run in O(N) time. 
The presence of negative numbers means the standard maximum-subarray 
approach does not directly apply — a negative times a negative can 
produce a large positive, so you must track both the maximum 
and minimum products ending at each index

Testcase 1
Input:

Plaintext
4
2 3 -2 4
Expected Output:

Plaintext
6
'''

import sys
input_data=sys.stdin.read().split()
#with sys.stdin.read(), Python expects input from standard input until it encounters an End-Of-File (EOF) signal.

#Option A: Type directly in the Terminal
#Run python script.py in your terminal.

#Paste or type all your numbers (e.g., 5 2 3 -2 4 -1).

#Press Enter, then send the EOF signal:

#Windows: Press Ctrl + Z then Enter.

'''Option B: Pipe input from a Text File (Recommended for sys.stdin)
Save your input inside a text file named input.txt:

Plaintext
5
2 3 -2 4 -1
Then run this command in your terminal:

Bash
python script.py < input.txt'''

if not input_data:
    exit()
n=int(input_data[0])
nums=[int(i) for i in input_data[1:n+1]]
if not nums:
    exit()
max_prod=nums[0]
min_prod=nums[0]
res=nums[0]
for i in range(1,len(nums)):
    if nums[i]<0:
        max_prod,min_prod=min_prod,max_prod
    max_prod=max(nums[i],max_prod*nums[i])
    min_prod=min(nums[i],min_prod*nums[i])
    res=max(res,max_prod)
print(res)

#Time Complexity:O(N) — iterates through the array once.
#Space Complexity:O(1) — uses constant extra space

'''Why do we swap when num < 0?If max_prod was +6 and min_prod was -12, 
and we multiply both by a negative number like -2: +6 times -2 = -12 
(became the new minimum)-12x-2 = +24 (became the new maximum)
Swapping them before multiplying keeps max_prod tracking the 
largest potential value and min_prod tracking the smallest.'''
#Dry Run
'''Let's walk through the example array: [2, 3, -2, 4]

Initialization (Index 0)
Current number: 2

max_prod = 2

min_prod = 2

result = 2

Iteration 1 (Index 1)Current number num = 3Is 3 < 0? No, so no swap.
Calculate max_prod: max(3, 2 * 3) -> max(3, 6) = 6
Calculate min_prod: min(3, 2 * 3) -> min(3, 6) = 3
Update result: max(2, 6) = 6

Iteration 2 (Index 2)Current number num = -2
Is -2 < 0? Yes! Swap max_prod and min_prod:
max_prod becomes 3min_prod becomes 6
Calculate max_prod: max(-2, 3 * -2) -> max(-2, -6) = -2
Calculate min_prod: min(-2, 6 * -2) -> min(-2, -12) = -12
Update result: max(6, -2) = 6

Iteration 3 (Index 3)Current number num = 4Is 4 < 0? No, so no swap.
Calculate max_prod: max(4, -2 * 4) -> max(4, -8) = 4 
Calculate min_prod: min(4, -12 * 4) -> min(4, -48) = -48
Update result: max(6, 4) = 6

Final Output
result = 6 (from subarray [2, 3])'''
