"""Write a program that processes a given 
string to determine:
The 1st non-repeating character(if +nt)

The most repeated character in the string

If multiple characters hv the same highest freq, 
print the 1st non-repeating character 1st,then 
the repeating character.

If the input string is empty,print 'Invalid input'

If all characters in the string are repeating,
print "None" followed by the 1st 
repeating character

Eg. of input string: Swiss mississippi

Note: In quesns where u hv to determine frequency, use map DS"""

from collections import defaultdict

def find_char(s):
    if not s:
        print("Invalid input!")
        return

    # Frequency map and index map
    freq = defaultdict(int)
    idx = {}

    # Calculate frequency and store first occurrence index
    for i, char in enumerate(s):
        freq[char] += 1
        if char not in idx:
            idx[char] = i

    # Finding the first non-repeating character
    first_non_reptg = None
    for char in s:
        if freq[char] == 1:
            first_non_reptg = char
            break

    # Finding the most repeated character
    max_freq = max(freq.values())
    most_reptg = None
    prev_idx = len(s)
    for char, count in freq.items():
        if count == max_freq:
            # We want the character that appears first in the string
            if idx[char] < prev_idx:
                prev_idx = idx[char]
                most_reptg = char

    # Finding the first repeating character
    first_reptg = None
    for char in s:
        if freq[char] > 1:
            first_reptg = char
            break

    # Output
    if first_non_reptg is None:
        print("None", end=" ")
        if first_reptg:
            print(first_reptg)
        else:
            print()
    else:
        print(first_non_reptg)
        print(most_reptg)

# Main function
if __name__ == "__main__":
    s = input("Enter a string: ")

    find_char(s)


"""defaultdict is a subclass of the built-in dict (dictionary) class, 
which is part of Python's collections module.

The key difference between dict and defaultdict is that defaultdict 
automatically provides a default value for a nonexistent key, so you don't 
have to explicitly check whether a key exists before accessing or updating it

Eg.       from collections import defaultdict

# Create a defaultdict where the default value for missing keys is 0
freq = defaultdict(int)

# Increment values without checking if key exists
freq['a'] += 1
freq['b'] += 1
freq['a'] += 1

# Output the dictionary
print(freq)

Why Use defaultdict(int)?

In your program, defaultdict(int) is used for counting frequencies of 
characters in the string. Normally, you'd have to check whether 
a key exists in the dictionary before incrementing its value. 
With defaultdict(int), it simplifies the code because 
you don't have to do that check — if a key doesn't exist, 
it will automatically initialize it with 0 and then increment the value.

Without defaultdict, you'd have to write something like this:

freq = {}
if char in freq:
    freq[char] += 1
else:
    freq[char] = 1

With defaultdict(int), this becomes:

from collections import defaultdict
freq = defaultdict(int)
freq[char] += 1  # Automatically handles missing keys

Concept of Frequency and Index Maps
Frequency Map (freq):
A frequency map is a dictionary-like data structure (here, defaultdict(int)) that keeps track of how many times each character appears in the string.
A defaultdict(int) is used instead of a normal dictionary. This automatically initializes the value for a key (the character) to 0 if it doesn’t exist in the dictionary, making it easier to increment the count without needing to check if the key already exists.
Index Map (idx):
An index map keeps track of the first occurrence of each character. In this map, the key is the character, and the value is the index (position) of that character in the string.
Dry Run Example

Let’s consider the string Swiss mississippi and step through the code:

from collections import defaultdict

def find_char(s):
    # 1. Frequency map and index map
    freq = defaultdict(int)
    idx = {}

    # 2. Calculate frequency and store first occurrence index
    for i, char in enumerate(s):
        freq[char] += 1              # Increment the frequency of the character
        if char not in idx:          # Check if the character is encountered for the first time
            idx[char] = i            # Store the first occurrence of the character

    print(freq)  # {'S': 1, 'w': 1, 'i': 4, 's': 3, ' ': 2, 'm': 1, 'p': 2} 
    print(idx)   # {'S': 0, 'w': 1, 'i': 2, 's': 3, ' ': 7, 'm': 8, 'p': 10}


Let’s walk through the loop with the string Swiss mississippi:

Loop Breakdown (for i, char in enumerate(s)):
Iteration 1: i = 0, char = 'S'
freq['S'] becomes 1 (since it's encountered for the first time).
'S' is not in idx, so idx['S'] = 0 (store first occurrence index).
Iteration 2: i = 1, char = 'w'
freq['w'] becomes 1 (it's encountered for the first time).
'w' is not in idx, so idx['w'] = 1 (store first occurrence index).
Iteration 3: i = 2, char = 'i'
freq['i'] becomes 1 (it's encountered for the first time).
'i' is not in idx, so idx['i'] = 2 (store first occurrence index).
Iteration 4: i = 3, char = 's'
freq['s'] becomes 1 (it's encountered for the first time).
's' is not in idx, so idx['s'] = 3 (store first occurrence index).
Iteration 5: i = 4, char = 's'
freq['s'] becomes 2 (increment count, now s appears twice).
Iteration 6: i = 5, char = ' '
freq[' '] becomes 1 (it's encountered for the first time).
' ' is not in idx, so idx[' '] = 5 (store first occurrence index).
Iteration 7: i = 6, char = 'm'
freq['m'] becomes 1 (it's encountered for the first time).
'm' is not in idx, so idx['m'] = 6 (store first occurrence index).
Iteration 8: i = 7, char = 'i'
freq['i'] becomes 2 (increment count, now i appears twice).
Iteration 9: i = 8, char = 's'
freq['s'] becomes 3 (increment count, now s appears three times).
Iteration 10: i = 9, char = 's'
freq['s'] becomes 4 (increment count, now s appears four times).
Iteration 11: i = 10, char = 'i'
freq['i'] becomes 3 (increment count, now i appears three times).
Iteration 12: i = 11, char = 'p'
freq['p'] becomes 1 (it's encountered for the first time).
'p' is not in idx, so idx['p'] = 11 (store first occurrence index).
Iteration 13: i = 12, char = 'p'
freq['p'] becomes 2 (increment count, now p appears twice).
Iteration 14: i = 13, char = 'i'
freq['i'] becomes 4 (increment count, now i appears four times).
After the loop, the frequency and index maps would look like this:
freq (Frequency Map):
{'S': 1, 'w': 1, 'i': 4, 's': 4, ' ': 2, 'm': 1, 'p': 2}
idx (Index Map):
{'S': 0, 'w': 1, 'i': 2, 's': 3, ' ': 5, 'm': 6, 'p': 11}

Code Breakdown
# Finding the most repeated character
max_freq = max(freq.values())  # Find the highest frequency of any character
most_reptg = None              # Placeholder for the most repeated character
prev_idx = len(s)              # Set prev_idx to a large value, greater than any index in the string

# Loop through the frequency map to find the most repeated character
for char, count in freq.items():
    if count == max_freq:  # If the current character has the highest frequency
        # We want the character that appears first in the string
        if idx[char] < prev_idx:  # Check if the first occurrence index of the current character is less
            prev_idx = idx[char]  # Update the previous index to the current one
            most_reptg = char      # Update the most repeated character
Step-by-Step Explanation
1. max_freq = max(freq.values())
Purpose: This line finds the highest frequency of any character in the string.
freq.values() gives a list of all the frequency counts of the characters in the string.
max() finds the maximum value in that list, which is the highest frequency of any character.

Example:
For the input string "Swiss mississippi", the freq map looks like this:

{'S': 1, 'w': 1, 'i': 4, 's': 4, ' ': 2, 'm': 1, 'p': 2}

The max(freq.values()) would return 4, because the highest frequency is 4 (for characters 'i' and 's').

2. most_reptg = None and prev_idx = len(s)
Purpose:
most_reptg = None initializes a variable to hold the character with the highest frequency.
prev_idx = len(s) initializes a variable to hold the index of the first occurrence of the most frequent character.
len(s) is used to set prev_idx to a value that is guaranteed to be larger than any valid index in the string (since indices start from 0). This will allow us to update it to the first index of the character with the highest frequency during the loop.

Example:

For the input string "Swiss mississippi", len(s) would be 17 (because the string has 17 characters).
3. Loop: for char, count in freq.items():
Purpose: This loop goes through each character (char) and its frequency (count) in the frequency map (freq).
freq.items() gives pairs of characters and their frequencies (key-value pairs).

For example, the loop will iterate over these items in the freq map:

('S', 1), ('w', 1), ('i', 4), ('s', 4), (' ', 2), ('m', 1), ('p', 2)
4. Condition: if count == max_freq:
Purpose: This checks if the current character's frequency (count) m
atches the highest frequency (max_freq) found earlier.
If it does, we proceed to find out which of the characters 
with the highest frequency appears first in the string.
5. Sub-condition: if idx[char] < prev_idx:
Purpose: If the current character’s frequency is the highest 
(count == max_freq), we want to check which of these characters 
appears first in the string.
idx[char] gives the index of the first occurrence of the 
current character.
prev_idx is used to store the index of the most repeated 
character found so far. Initially, it's set to len(s), 
which is larger than any index in the string.
If the index of the current character (idx[char]) 
is smaller than prev_idx, this means the current character 
appears first in the string compared to the one stored in most_reptg.
Dry Run Example

Let's use the input string "Swiss mississippi" to walk through this section of the code:

First, we have max_freq = max(freq.values()):
max_freq = 4 (since 'i' and 's' both have a frequency of 4).
Initial Values:
most_reptg = None
prev_idx = 17 (since the length of the string is 17).
Loop through the frequency map:
For character 'S' (frequency 1):
count == max_freq → 1 == 4 (false), so we skip this iteration.
For character 'w' (frequency 1):
count == max_freq → 1 == 4 (false), so we skip this iteration.
For character 'i' (frequency 4):
count == max_freq → 4 == 4 (true), so we enter the inner condition.
idx['i'] = 2 (first occurrence of 'i' is at index 2).
prev_idx = 17 (previous index is larger than 2), so we update:
prev_idx = 2
most_reptg = 'i'
For character 's' (frequency 4):
count == max_freq → 4 == 4 (true), so we enter the inner condition.
idx['s'] = 3 (first occurrence of 's' is at index 3).
idx['s'] < prev_idx → 3 < 2 (false), so we don't update most_reptg or prev_idx.
Final Result:
After the loop finishes, the most repeated character is 'i', because it appeared first among the characters with the highest frequency (4).

Thus, the result after this part of the code would be:

most_reptg = 'i'
"""
