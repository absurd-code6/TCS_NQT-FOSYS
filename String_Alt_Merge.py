'''You are given two strings voril and word2. Merge the strings by 
adding letters in alternating order, starting with wordt. 
If a string is longer than the other, append the additional letters 
onto the end of the merged string.
Return the merged string.
Example 1:
Input: word "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:abc

word2:pqr
merged: apbqcr
Example 2:
Input: words "ab", word "pqrs"
Output: apbqrs
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1: ab
word2: pqrs
morged: apbqrs
'''
#Zip Version
def mergeAlternately(word1: str, word2: str) -> str:
    res = []

    # merge common length part
    for a, b in zip(word1, word2):
        res.append(a)
        res.append(b)

    # append remaining parts
    res.append(word1[len(word2):])
    res.append(word2[len(word1):])

    return "".join(res)

#Recursive version
'''This builds the string by taking one character at a time recursively:'''
def mergeAlternately(word1: str, word2: str) -> str:
    if not word1:
        return word2
    if not word2:
        return word1

    return word1[0] + word2[0] + mergeAlternately(word1[1:], word2[1:])

#Using zip_longest (cleanest “one-liner” solution)
from itertools import zip_longest

def mergeAlternately(word1: str, word2: str) -> str:
    return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue="") if a or b)

# Longer Approach
def mergeAlternately(word1: str, word2: str) -> str:
    res = []
    i = j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1

    return "".join(res)