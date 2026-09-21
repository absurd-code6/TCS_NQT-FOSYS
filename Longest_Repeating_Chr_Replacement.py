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
