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

Without defaultdict, you’d have to write something like this:

freq = {}
if char in freq:
    freq[char] += 1
else:
    freq[char] = 1

With defaultdict(int), this becomes:

from collections import defaultdict
freq = defaultdict(int)
freq[char] += 1  # Automatically handles missing keys"""