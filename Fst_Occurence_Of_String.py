'''Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is 
not part of haystack.
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
def Fst_Occ(n, h):
    if n == "":
        return 0
    if len(n) > len(h):
        return -1

    for i in range(len(h) - len(n) + 1):
        if h[i : i + len(n)] == n:
            return i
    return -1

needle = input().strip()
haystack = input().strip()
print(Fst_Occ(needle, haystack))

#    OR

'''def Fst_Occ1(n,h):
    if n=="":
        return 0
    for i in range(len(h) + 1 - len(n)):
        for j in range(len(n)):
            if h[i+j]!=n[j]:
                break
            if j==len(n)-1:
                return i
    return -1

needle=input().strip()
haystack=input().strip()
print(Fst_Occ1(needle,haystack))'''

'''Dry Run Example
Let's trace the execution step-by-step with an example:
haystack (h) = "sadbutsad" (length = 9)needle (n) = "sad" (length = 3)
Setup & Early Checks
n == "" is False (needle is not empty).
len(n) > len(h) is 3 > 9, which is False.
Loop range: range(9 - 3 + 1) -> range(7), which checks indices 0, 1, 2, 3, 4, 5, 6.Iteration 1 (i = 0):
Extract slice: h[0 : 0 + 3] -> h[0:3], which is "sad".
Check: Is "sad" == "sad"? Yes!
Action: return 0 immediately and exit.
Output: 0 (1st idx)

Dry Run Example 2 (Failed Match)
haystack (h) = "leetcode" (length = 8)
needle (n) = "leeto" (length = 5)
Loop range: range(8 - 5 + 1) -> range(4) (indices 0, 1, 2, 3)

i = 0: Slice h[0:5] is "leet" != "leeto"
i = 1:  Slice h[1:6] is "eetco" != "leeto"
i = 2: Slice h[2:7] is "etcod" != "leeto"
i = 3: Slice h[3:8] is "tcode" != "leeto"
Loop ends with no match found
Output: -1'''
