'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''

#Follow up: What if the inputs contain Unicode characters? How would 
#you adapt your solution to such a case?

from collections import Counter
from collections import defaultdict

def Valid_Anagram(s,t):
    if len(s)!=len(t):
        return False
    #return Counter(s)==Counter(t) #Sneaky
    #return sorted(s)==sorted(t)

    count=defaultdict(int)
# Count frequency of each character in s
    for ch in s:
        count[ch]+=1
# Subtract frequency for each character in t
    for ch in t:
        count[ch]-=1
# If it's an anagram, all final counts must be 0
    for i in count.values():
        if i!=0:
           return False
    return True

s=input().strip()
t=input().strip()
print(Valid_Anagram(s,t))
#print(str(Valid_Anagram(s,t)).lower())

#Dry run
'''Inputs: s = "cat", t = "act"Length Check: len("cat") == 3 
and len("act") == 3 -> Lengths match, so proceed.
Dictionary State: counts = {}1.
Phase 1: Count characters in s =:Iterate through string s from left 
to right:Iteration 1 (char = 'c'):Key 'c' does not exist in counts. 
defaultdict initializes it to 0.
Increment count: counts['c'] += 1 -> counts['c'] = 1
State: {'c': 1}

Iteration 2 (char = 'a'):Key 'a' initialized to 0.
Increment count: counts['a'] += 1 -> counts['a'] = 1
State: {'c': 1, 'a': 1}
Iteration 3 (char = 't'):Key 't' initialized to 0.
Increment count: counts['t'] += 1 -> counts['t'] = 1
State: {'c': 1, 'a': 1, 't': 1}

Iteration 3 (char = 't'):Key 't' initialized to 0.
Increment count: counts['t'] += 1 -> counts['t'] = 1
State: {'c': 1, 'a': 1, 't': 1}

Phase 2: Subtract frequencies using t =:
Iterate through string t from left to right:
Iteration 1 (char = 'a'):Key 'a' exists with value 1.
Decrement count: counts['a'] -= 1 -> counts['a'] = 0
State: {'c': 1, 'a': 0, 't': 1}

Iteration 2 (char = 'c'):Key 'c' exists with value 1.
Decrement count: counts['c'] -= 1 -> counts['c'] = 0
State: {'c': 0, 'a': 0, 't': 1}

Iteration 3 (char = 't'):Key 't' exists with value 1.
Decrement count: counts['t'] -= 1 -> counts['t'] = 0
State: {'c': 0, 'a': 0, 't': 0}

3.Phase 3: Final Verification:Check all values in counts.values() 
-> [0, 0, 0]:Inspect counts['c'] (0) -> Equal to 0. 
Continue.Inspect counts['a'] (0) -> Equal to 0. 
Continue.Inspect counts['t'] (0) -> Equal to 0. 
Continue.All counts are 0. 

The function returns True.
'''
