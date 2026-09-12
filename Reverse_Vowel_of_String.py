'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear 
in both lower 
and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, 
s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''
'''def rev_vowel(s):
    s_list=list(s)
    vowels=set("aeiouAEIOU")
    left=0
    right=len(s_list)-1
    while left<right:
        if s_list[left] not in vowels:
            left+=1
            continue
        s_list[left],s_list[right]=s_list[right],s_list[left]
        left+=1
        right-=1
    print("".join(s_list))

s=input()
rev_vowel(s)'''

# Alternate(Easier) Approach
def reverse_vowels(s): 
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res=[]
    for ch in s:
        if ch in vowels:
            res.append(ch)
    res=res[::-1]
    s=list(s) #Since strings in python are immutable convert it into a 
#mutable list
    j=0
    for c in range(len(s)):
        if s[c] in vowels:
            s[c]=res[j]
#s[c] = res[c] will give wrong ans as the index c is the position 
#in the original string, but res contains only the vowels. 
#Their indices do not match.
            j+=1
    #print(s)
    print("".join(s))
s=input()
reverse_vowels(s)
reverse_vowels("leetcode")
