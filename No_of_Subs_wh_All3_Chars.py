'''Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence 
of all these characters a, b and c.
Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of 
the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", 
"bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of 
the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
'''
def All3Chars(s:str)->int:
    if not s:
        return
    last_seen = {'a': -1, 'b': -1, 'c': -1}
    count = 0
    for i, char in enumerate(s):
        last_seen[char] = i
        
        # If all characters 'a', 'b', and 'c' have been seen at least once
        min_last_pos = min(last_seen['a'], last_seen['b'], last_seen['c'])
        if min_last_pos != -1:
            count += min_last_pos + 1
            
    print(count)

#TC+O(N),SC=O(1)
s=input().strip()
All3Chars(s)

'''s="aaacb"
chars=sorted(set(s))
print(chars)
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
        cur=s[i:j+1]
        if sorted(set(cur))==chars:
           count+=1
print(count)

TC=O(n^2)'''

#The Big Idea (The "Cheat Code")
'''If you are looking at a string up to position i (for example, index 4):

You check the last time you saw 'a', 'b', and 'c'.

Find the oldest (smallest index) among those three positions. 
Let's call it min_last_pos.

If all three characters have appeared at least once, every single substring starting 
at or before min_last_pos and ending at i is guaranteed to contain all three characters.

The number of such valid starting positions is simply min_last_pos + 1.

Step-by-Step Dry Run (s = "abcabc")
Start:

last_seen = {'a': -1, 'b': -1, 'c': -1}

count = 0

Index 0 — Character 'a'

Update: 'a' is at index 0. last_seen becomes {'a': 0, 'b': -1, 'c': -1}.

Check: min_last_pos is -1 because 'b' and 'c' haven't been seen yet.

Result: min_last_pos != -1 is False.

count: 0

Index 1 — Character 'b'

Update: 'b' is at index 1. last_seen becomes {'a': 0, 'b': 1, 'c': -1}.

Check: min_last_pos is -1 because 'c' is still missing.

Result: min_last_pos != -1 is False.

count: 0

Index 2 — Character 'c'

Update: 'c' is at index 2. last_seen becomes {'a': 0, 'b': 1, 'c': 2}.

Check: All three characters have been seen! The oldest is 'a' at index 0. 
So min_last_pos = 0.

Result: min_last_pos != -1 is True.

Math: Add 0 + 1 = 1 to count.

New Substring Found: "abc" (starts at index 0, ends at index 2).

count: 1

Index 3 — Character 'a'

Update: Most recent 'a' moves to index 3. last_seen becomes {'a': 3, 'b': 1, 'c': 2}.

Check: The oldest position among the three is 'b' at index 1. So min_last_pos = 1.

Result: min_last_pos != -1 is True.

Math: Add 1 + 1 = 2 to count.

New Substrings Found: "abca" (starts at index 0) and "bca" (starts at index 1).

count: 3 (1 + 2)

Index 4 — Character 'b'

Update: Most recent 'b' moves to index 4. last_seen becomes {'a': 3, 'b': 4, 'c': 2}.

Check: The oldest position among the three is 'c' at index 2. So min_last_pos = 2.

Result: min_last_pos != -1 is True.

Math: Add 2 + 1 = 3 to count.

New Substrings Found: "abcab", "bcab", and "cab".

count: 6 (3 + 3)

Index 5 — Character 'c'Update: Most recent 'c' moves to index 5. last_seen 
becomes {'a': 3, 'b': 4, 'c': 5}.Check: The oldest position among the three is 'a' 
at index 3. So min_last_pos = 3.Result: min_last_pos != -1 is True.
Math: Add 3 + 1 = 4 to count.New Substrings Found: "abcabc", "bcabc", "cabc", and "abc".
count: 10 (6 + 4)
Final Result: The function prints 10.

Why does min_last_pos + 1 work?
Take Index 3 ('a'):

last_seen is {'a': 3, 'b': 1, 'c': 2}.

min_last_pos = 1 (which is 'b').

Any substring ending at index 3 that starts at index 0 or 1 will include indices 0, 1, 2, 3 
or 1, 2, 3—both containing 'a', 'b', and 'c'.

Indices 0 and 1 give us 2 valid substrings (1 + 1 = 2).
'''
