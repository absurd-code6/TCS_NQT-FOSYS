'''Given two strings s and p, return an array of all the start indices 
of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
def findAllAnagrams1(*args):
    n,m=len(s),len(p)
    p_sorted=sorted(p)
    res=[]
    if m>n:
        return []
    for i in range(n):
        curr=s[i:i+m]
        if sorted(curr)==p_sorted:
            res.append(i)
    return res
    
# TC = O(N \times M \log M) — Slower, SC = O(M) — Creates new string slice each loop

def findAllAnagrams2(s,p):
    if len(p)>len(s):
        return []
    pCount,sCount={},{}
    for i in range(len(p)):
        pCount[p[i]]=1+pCount.get(p[i],0)
        sCount[s[i]]=1+sCount.get(s[i],0)
    res=[0] if sCount==pCount else []
    l=0
    for j in range(len(p),len(s)):
        sCount[s[j]]=1+sCount.get(s[j],0)
        sCount[s[l]]-=1
        if sCount[s[l]]==0:
            sCount.pop(s[l])
        l+=1
        if sCount==pCount:
           res.append(l)
    return res

#TC = O(N), SC = O(1)

s=input().strip()
p=input().strip()
print(findAllAnagrams1(s,p))
print(findAllAnagrams2(s,p))

