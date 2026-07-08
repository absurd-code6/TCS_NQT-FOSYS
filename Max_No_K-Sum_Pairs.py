'''You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals 
k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''
from collections import Counter
def max_operations(nums,k):
    count=Counter(nums)
    operations=0
    for num in list(count.keys()):
        complement=k-num
        if num==complement:
            operations+=count[num]//2
        elif num<complement:
            if complement in count:
                pairs=min(count[num],count[complement])
                operations+=pairs
    return operations

line1=input().split()
k=int(line1[1])
nums=list(map(int,input().split()))
print(max_operations(nums,k))

# By using dictionary instead of Counter
def max_operations(nums, k):
    freq = {}
    for i in nums:
        freq[i]+=1 #freq[i] = freq.get(i, 0) + 1
        
        #freq.get(i, 0) + 1: Standard dictionaries throw a 
        # KeyError if you try to do freq[i] += 1 on a 
        # number that hasn't been seen yet. Using .get(i, 0) 
        # safely grabs the current count or defaults to 0.
        
        operations = 0
    for i in freq:
         complement = k - i
         if i == complement:
            operations += freq[i] // 2
         elif i < complement:
            # To avoid double-counting, only check when i < complement
            if complement in freq:
                pairs = min(freq[i], freq[complement])
                operations += pairs
    return operations

# Using defaultdict
from collections import defaultdict
def max_operations(nums, k):
    # 1. Initialize freq as a defaultdict of integers (defaults to 0)
    freq = defaultdict(int)
    for i in nums:
        freq[i] += 1        
    #No KeyError: When Python hits freq[i] += 1 for a number 
    # it hasn't seen yet, defaultdict(int) automatically creates 
    # the key and assigns it a default value of 0 before adding 1.    
    operations = 0
    
    for i in freq:
        complement = k - i
        if i == complement:
            operations += freq[i] // 2
        elif i < complement:
            # To avoid double-counting, only check when i < complement
            if complement in freq:
                pairs = min(freq[i], freq[complement])
                operations += pairs
                
    return operations

'''This function counts the maximum number of pairs whose sum is k.

Let's understand only the working part with a dry run.

Example
nums = [1, 2, 3, 4]
k = 5

The pairs that sum to 5 are:

(1, 4)
(2, 3)

Answer = 2

Step 1: Count the frequency of each number
count = Counter(nums)

Counter stores how many times each number appears.

For our example:

count = {
    1: 1,
    2: 1,
    3: 1,
    4: 1
}

So instead of searching through the list again and again, 
we already know how many of each number exist.

Step 2: Visit every unique number
for num in list(count.keys()):

count.keys() gives

[1, 2, 3, 4]

Now we'll check each number.

First iteration
num = 1

Find its partner:

complement = k - num
complement = 5 - 1 = 4

We need 4 because

1 + 4 = 5

Now check

if num == complement:

Is

1 == 4 ?

No.

Go to

elif num < complement:
1 < 4

Yes.

Now check

if complement in count:

Does 4 exist?

Yes.

Now

pairs = min(count[1], count[4])

Both appear once.

pairs = min(1,1) = 1

So

operations += 1

Now

operations = 1
Second iteration
num = 2

Partner:

complement = 5 - 2 = 3

Again,

2 < 3

Yes.

pairs = min(count[2], count[3])
pairs = min(1,1) = 1

Now

operations = 2
Third iteration
num = 3

Partner:

2

Now

3 < 2

False.

Nothing happens.

Why?

Because we already counted the pair (2,3) when num was 2.

This avoids counting the same pair twice.

Fourth iteration
num = 4

Partner:

1

Again,

4 < 1

False.

Nothing happens.

Again, the pair (1,4) was already counted.

Final answer:

operations = 2
Why num < complement?

Suppose we didn't write this condition.

When num = 1

we count

(1,4)

Later,

num = 4

we'd count

(4,1)

again.

So we'd count the same pair twice.

The condition

elif num < complement:

ensures each pair is counted only once.

Special case

Suppose

nums = [3,3,3,3]
k = 6

Now

num = 3
complement = 3

Here,

num == complement

is True.

The code executes

operations += count[3] // 2

There are 4 threes.

They can form:

(3,3)
(3,3)

So

4 // 2 = 2

operations becomes

2

If there were

nums = [3,3,3]

then

3 // 2 = 1

Only one pair can be formed, and one 3 is left unused.

Dry Run Summary

For:

nums = [1,2,3,4]
k = 5
num	complement	Action	operations
1	4	Count (1,4)	1
2	3	Count (2,3)	2
3	2	Skip (already counted)	2
4	1	Skip (already counted)	2'

What is Counter?

Counter is a tool that counts how many times each item appears 
in a list (or other iterable).

Imagine you have a basket of fruits:

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

If someone asks:

"How many apples are there?"

Without Counter, you'd have to count them manually.

With Counter:

from collections import Counter

count = Counter(fruits)

print(count)

Output:

Counter({
    'apple': 3,
    'banana': 2,
    'orange': 1
})

It automatically counts everything for you.

Another example
nums = [1, 2, 2, 3, 3, 3]

Now use Counter:

from collections import Counter

count = Counter(nums)

print(count)

Output:

Counter({
    3: 3,
    2: 2,
    1: 1
})

This means:

1 appears 1 time.
2 appears 2 times.
3 appears 3 times.
Accessing the count of one item

Suppose:

count = Counter([1, 2, 2, 3, 3, 3])

You can ask:

print(count[2])

Output:

2

because 2 appears twice.

Similarly,

print(count[3])

Output:

3'''