'''Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''
def isPal(s):
    return s==s[::-1]

def LongPalSub(s):
    n=len(s)
    longest=""
    for ch in range(n):
        for j in range(ch+1,n+1):
            sub=s[ch:j]
            if isPal(sub):
                if len(sub) > len(longest):
                    longest=sub
    return longest
#Brute Force Approach[TC+O(n^3),for n iterations n^2 substrings are checked]

def LongPalSub1(s):
    res=""
    reslen=0
    for i in range(len(s)):
        #for odd length palindromes
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>reslen:
                res=s[l:r+1]
                reslen=r-l+1
            l-=1
            r+=1
        #for even length palindromes
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
                    if (r-l+1)>reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
    return res

s=input()
print(LongPalSub(s))
print(LongPalSub1(s))
#TC=O(n^2)

'''Core Idea: Expand Around Center
Instead of checking every possible section of the string, this code treats each 
character as a potential center of a palindrome and expands outward 
to the left (l) and right (r).

Because palindromes come in two forms, it checks both at every index:

Odd-length palindromes (e.g., "aba"): Starts with l and r at the exact 
same character (l = i, r = i).

Even-length palindromes (e.g., "abba"): Starts with l and r 
side-by-side (l = i, r = i + 1).

While s[l] == s[r], it keeps expanding (l -= 1, r += 1). If the current palindrome 
is longer than the previous best (reslen), it updates the result res.

Dry Run Example
Let's trace s = "babad" step-by-step.

Initial state: res = "", reslen = 0
Index i = 0 (s[0] = 'b')Odd Check (l=0, r=0):s[0] == s[0] ('b' == 'b') 
-> Length = $0 - 0 + 1 = 1 > 0$.res = "b", reslen = 1.
Expand: l becomes -1, loop stops (out of bounds).
Even Check (l=0, r=1):s[0] == s[1] ('b' == 'a') -> False, loop stops.

Index i = 1 (s[1] = 'a')Odd Check (l=1, r=1):
Step 1: s[1] == s[1] ('a' == 'a') -> Length 1 <= 1 (no length update).
Expand: l = 0, r = 2.Step 2: s[0] == s[2] ('b' == 'b') 
-> Length = 2 - 0 + 1 = 3 > 1. res = "bab", reslen = 3.
Expand: l = -1, r = 3, loop stops.
Even Check (l=1, r=2):s[1] == s[2] ('a' == 'b') -> False, loop stops.

Index i = 2 (s[2] = 'b')Odd Check (l=2, r=2):Step 1: s[2] == s[2] ('b' == 'b').
Expand: l = 1, r = 3.
Step 2: s[1] == s[3] ('a' == 'a') -> Length = 3 - 1 + 1 = 3. 
Not strictly greater than reslen ($3 > 3$ is False), so res stays "bab".
Expand: l = 0, r = 4.Step 3: s[0] == s[4] ('b' == 'd') -> False, loop stops.
Even Check (l=2, r=3):s[2] == s[3] ('b' == 'a') -> False, loop stops.
Indices i = 3 and i = 4
Further expansions fail to beat length 3.

Final Output: "bab" (Note: "aba" is also valid, but "bab" was found first).'''