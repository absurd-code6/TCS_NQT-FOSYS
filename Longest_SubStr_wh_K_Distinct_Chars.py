'''You are given a string s and an integer k. Your task is to 
find the length of the longest substring within s that contains 
at most k distinct characters.

A substring is a contiguous sequence of characters within the string. 
For example, if s = "eceba" and k = 2, you need to find the 
longest substring that has no more than 2 different characters.

Let's break down what this means:

You need to examine all possible substrings of the input string s
Count the number of distinct/unique characters in each substring
Keep only those substrings where the distinct character count is at most k (less than or equal to k)
Return the length of the longest valid substring
For instance:

If s = "eceba" and k = 2, the substring "ece" has 2 distinct characters ('e' and 'c'), making it valid with length 3
If s = "aa" and k = 1, the entire string has only 1 distinct character ('a'), so the answer would be 2
'''
from collections import defaultdict
def Longest_String_K_Distinct_Chars(s,k):
    if s=="" or k==0 or k >= len(s):
       return 0
    seen=defaultdict(int)
    c=""
    l=0
    longest=0
    for r in range(len(s)):
        seen[s[r]]+=1
        while len(seen)>k:
            seen[s[l]]-=1
            if seen[s[l]]==0:
               del seen[s[l]]
            l+=1
        #longest=max(longest,r-l+1)
        if (r-l+1)>longest:
            longest=r-l+1
            c=s[l:r+1]
    return [longest,c]

s=input().strip()
k=int(input())
print(Longest_String_K_Distinct_Chars(s,k))