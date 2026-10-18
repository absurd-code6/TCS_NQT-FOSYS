'''Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
from collections import defaultdict
def MinWindowSub(s,t):
    if not s or len(s)<len(t):
        return ""
    count=defaultdict(int)    
    window=defaultdict(int)
    l=0
    for c in t:
        count[c]+=1
    have=0
    need=len(count)
    res=[-1,-1]
    reslen=float('inf')
    for r in range(len(s)):
        c=s[r]
        window[c]+=1
        if c in count and window[c]==count[c]:
            have+=1
        while have==need:
            if (r-l+1)<reslen:
                res=[l,r]
                reslen=r-l+1
            window[s[l]]-=1 #popping from the left of our window
            if s[l] in count and window[s[l]]<count[s[l]]:
                have-=1
            l+=1
    l,r=res
    return s[l:r+1] if reslen != float('inf') else ""

#            Easier Alternative

def contains(count,window):
    for char, qty in count.items():
            if qty>window[char]:
                return False
    return True
def Min_Window_Substr(s,t):
    if not s or len(s)<len(t):
        return ""
    count=defaultdict(int)
    window=defaultdict(int)
    for c in t:
        count[c]+=1
    l=0
    minlen,minstart=float('inf'),0
    for r in range(len(s)):
        window[s[r]]+=1
        while(contains(count,window)):
            if r-l+1<minlen:
                minlen=r-l+1
                minstart=l
            window[s[l]]-=1
            l+=1
    return s[minstart:minstart+minlen] if minlen!=float('inf') else ""