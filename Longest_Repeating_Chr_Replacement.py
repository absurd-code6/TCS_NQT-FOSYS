'''You are given a string s and an integer k. You can choose any 
character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same 
letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''
from collections import defaultdict

def CharReplacement(s,k):
    if s=="" or k==0:
        return 0
    
    seen = defaultdict(int)
    l = 0
    maxfreq = 0
    longest = 0
    max_char = ""
    start_idx = 0
    
    for r in range(len(s)):
        seen[s[r]] += 1
        if seen[s[r]] > maxfreq:
            maxfreq = seen[s[r]]
            max_char = s[r]
        
        while (r - l + 1) - maxfreq > k:
            seen[s[l]] -= 1
            l += 1
            
        if (r - l + 1) > longest:
            longest = r - l + 1
            start_idx = l
            
    res = max_char * longest
    return [longest,res]

#O(N) Time Complexity: Every character is processed at most twice 
# (once by r, once by l).
s=input().strip().upper()
k=int(input())
print(CharReplacement(s,k))

'''The Rule:
If the number of characters you need to change, (r - l + 1) - maxfreq, becomes 
greater than k, your window has become invalid—you don't have enough 
replacement points (k) to turn the whole window into a single character.

What the while loop does:
When the window breaks the rule, the while loop shrinks the window from 
the left (l) until it becomes valid again:

seen[s[l]] -= 1: Decrements the count of the character leaving the window.

l += 1: Moves the left side of the window one step to the right.

Step-by-Step Dry Run Example
Let's trace the code with:s = "AABABBA" k = 1 (You can change at most 1 character)
Initial State:l = 0, 
maxfreq = 0 Step 1: r = 0, character = 'A'seen = {'A': 1}
maxfreq = 1 Window length (r - l + 1): 0 - 0 + 1 = 1 

Replacements needed: 1 - 1 = 0 Is 0 > k (0 > 1)? No -> while loop does not run.
Current valid window: "A" (Length: 1)

Step 2: r = 1, character = 'A'seen = {'A': 2}
maxfreq = 2 Window length: 1 - 0 + 1 = 2 Replacements needed: 2 - 2 = 0 Is 0 > k (0 > 1)? 
No -> while loop does not run.
Current valid window: "AA" (Length: 2)Step 3: r = 2, character = 'B'
seen = {'A': 2, 'B': 1} maxfreq = 2 Window length: 2 - 0 + 1 = 3 
Replacements needed: 3 - 2 = 1 Is 1 > k (1 > 1)? No -> while loop does not run.
Current valid window: "AAB" (Length: 3, replace 1 'B' to make "AAA")

Step 4: r = 3, character = 'A'seen = {'A': 3, 'B': 1}

maxfreq = 3 Window length: 3 - 0 + 1 = 4 Replacements needed: 4 - 3 = 1 Is 1 > k (1 > 1)? 
No -> while loop does not run. Current valid window: "AABA" 
(Length: 4, replace 1 'B' to make "AAAA") 

Step 5: r = 4, character = 'B'
seen = {'A': 3, 'B': 2} maxfreq = 3 Window length: 4 - 0 + 1 = 5 ("AABAB") 
Replacements needed: 5 - 3 = 2 Now, notice: 

Replacements needed (2) is greater than k (1)!
The window "AABAB" is invalid because changing 2 'B's requires k = 2, 
but we only have k = 1.'''
