'''Given an array of characters chars, compress it using the
following algorithm:

Begin with an empty string s. For each group of consecutive repeating 
characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths 
that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length 
of the array.
You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter 
and should be ignored.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses 
to "a2b2c3".
After modifying the input array in-place, the first 6 characters 
of chars should be ["a","2","b","2","c","3"].
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed 
since it is a single character.
After modifying the input array in-place, the first character 
of chars should be ["a"].
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses 
to "ab12".
After modifying the input array in-place, the first 4 characters 
of chars should be ["a","b","1","2"].'''

# Sneaky Approach
_=input()
chars=input().split()
res=[]
from itertools import groupby
for ch,g in groupby(chars):
    count=len(list(g))
    res.append(ch)
    if count>1:
        res.extend(list(str(count)))
print(len(res))
print(*res)

#Logical Apprch O(n)
def compress(chars):
    write_idx=0
    read_idx=0
    n=len(chars)
    while read_idx<n:
        char=chars[read_idx]
        count=0
        #Count consecutive occurence of the current char
        while read_idx<n and chars[read_idx]==char:
            read_idx+=1
            count+=1
        # Write the character to the write pointer destination
        chars[write_idx]=char
        write_idx+=1
        #If the char repeated,write its count as string digits
        if count>1:
            for digit in str(count):
                chars[write_idx]=digit
                write_idx+=1
    #Return how far the right pointer moved
    return write_idx
_ = input()
raw_chars=input*().strip()
chars=[c for c in raw_chars if c!=' ']
new_len=compress(chars)
compressed="".join(chars[:new_len])
print(new_len)
print(compressed)
   
#1st Code
'''
Input:
a a a b b b b b b b b b b c

1.Input ProcessingLine 1 (_=input()): 
Reads "12". Ignore it.
Line 2 (chars = input().split()):
chars = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c']
Line 3 (res = []): Starts as empty [].
2.Loop Iterations (groupby)groupby breaks chars 
into 3 consecutive groups:
Iteration 1: 
Group 'a'Group g: ['a', 'a', 'a']ch: 'a'
count: 3res.append('a') -> res becomes ['a'] 
Since count > 1, convert 3 to '3' and extend 
res:res is now: ['a', '3']

Iteration 2: Group 'b'Group g: 10 occurrences of 'b'ch: 'b'count: 10
res.append('b')-> res becomes ['a', '3', 'b']
Since count > 1, convert 10 to string '10', 
split into characters ['1', '0'], and extend res:
res is now: ['a', '3', 'b', '1', '0']

Iteration 3: Group 'c'Group g: ['c']ch: 'c'count: 1res.append('c') 
-> res becomes ['a', '3', 'b', '1', '0', 'c']
Since count is NOT $> 1$, do nothing.
res is now: ['a', '3', 'b', '1', '0', 'c']

Output Generation
Line 10 (print(len(res))): Prints 6 (since res has 6 elements).

Line 11 (print(*res)): Unpacks res and prints:

Plaintext
a 3 b 1 0 c

How is 10 split into 1,0 ?
The line responsible for splitting 10 into '1' and '0' is:
Pythonres.extend(list(str(count)))
Here is the exact step-by-step mechanism when count is equal to 10:
Step 1: str(count)First, Python converts the integer 10 
into a string:10 -> '10'
Step 2: list(...)
In Python, converting a string into a list breaks the string down 
into individual characters:list('10')->['1', '0']
Step 3: res.extend(...)
Unlike res.append(), which would add ['1', '0'] as a single 
nested list inside res, .extend() takes each element from the l
ist and appends them one by one to res:
If res was ['a', '3', 'b'], doing res.extend(['1', '0']) turns 
it into:['a', '3', 'b', '1', '0']

Why are we needing 2 variables ch and g in 
for ch, g in groupby(chars): ?

In Python, groupby(chars) returns pairs of values for each 
distinct consecutive group.

Because it returns two items at once, you need two variables 
(ch and g) to unpack them:

groupby(chars)→(key,group iterator)
What Each Variable Holds
Variable	What It Holds	
Example (if group is ['a', 'a', 'a'])
ch	The key — the character itself that is repeating - 'a'
g -> The group — an iterator containing all the occurrences of 
that character in the current sequence.	
An iterator containing ['a', 'a', 'a']

Why Can't We Just Use One?
If you only used one variable, like for item in groupby(chars):,
item would be a tuple containing both pieces:

Python
# item is ('a', <grouper object>)
ch = item[0]  # 'a'
g = item[1]   # <grouper object>
'''

'''Input: chars = ["a", "a", "b", "b", "c", "c", "c"]
Initial variables: read = 0, write = 0, n = 7
Step-by-Step Execution

Iteration 1: Processing group "aa"
read = 0: curr_char = chars[0] ('a').
Inner Loop (read counts consecutive 'a's):
At read = 0: matches 'a' -> read becomes 1, count = 1.
At read = 1: matches 'a' -> read becomes 2, count = 2.
At read = 2: sees 'b', stops.
Writing to Array:Write character: chars[write] = 'a' (chars[0] = 'a'), write becomes 1.
Since count > 1 (2 > 1), convert count to string ("2") and write each digit:chars[1] = '2',
write becomes 2.
State after Iteration 1:

chars = ["a", "2", "b", "b", "c", "c", "c"]

read = 2, write = 2
Iteration 2: Processing group "bb"read = 2: curr_char = chars[2] ('b').
Inner Loop (read counts consecutive 'b's):
At read = 2: matches 'b' -> read becomes 3, count = 1.
At read = 3: matches 'b' -> read becomes 4, count = 2.
At read = 4: sees 'c', stops.

Writing to Array:

Write character: chars[write] = 'b' (chars[2] = 'b'), write becomes 3.

Since count > 1 (2 > 1):

chars[3] = '2', write becomes 4.

State after Iteration 2:

chars = ["a", "2", "b", "2", "c", "c", "c"]

read = 4, write = 4
Iteration 3: Processing group "ccc"
read = 4: curr_char = chars[4] ('c').

Inner Loop (read counts consecutive 'c's):At read = 4: matches 'c' -> read becomes 5, 
count = 1.At read = 5: matches 'c' -> read becomes 6, count = 2.
At read = 6: matches 'c' -> read becomes 7, count = 3.
Loop ends because read (7) is no longer < n (7).

Writing to Array:

Write character: chars[write] = 'c' (chars[4] = 'c'), write becomes 5.

Since count > 1 (3 > 1):

chars[5] = '3', write becomes 6.

State after Iteration 3:

chars = ["a", "2", "b", "2", "c", "3", "c"]

read = 7, write = 6

The function returns write, which is 6.

The first 6 characters of the array (["a", "2", "b", "2", "c", "3"]) represent the 
compressed string, and anything beyond index 5 is ignored.
'''