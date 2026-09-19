'''Given a string s, find the length of the longest substring 
without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. 
Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" 
is a subsequence and not a substring.
'''

def length_of_longest_non_repeating_substr(s):
    charset=set()
    l=0
    longest=0
    res=""
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l+=1
        charset.add(s[r])
        longest=max(longest,r-l+1)
    return [longest]

s=input().strip()
print(length_of_longest_non_repeating_substr(s))
