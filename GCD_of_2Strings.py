'''For two strings s and t, we say "t divides s" if and only if s is 
formed when t is concatenated with itself one or more times
Given two strings stri and str2, return the largest string x such that
x divides both strt and str2.
Example 1:
Input:
stri "ABCABC", str2= "ABC"
Output: "ABC"
Example 2:
Input: str1= "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:
Input:
stri "LEET", str2 "CODE"
Output: ""
'''
import math
def String_gcd(str1,str2):
#Check if they can be made from same base string
    if str1+str2!=str2+str1:
        return ""
    #Find gcd of lengths of the 2 strings
    gcd_of_length=math.gcd(len(str1),len(str2))
    return str1[:gcd_of_length]

str1=input()
str2=input()
print(String_gcd(str1,str2))

#Brute-Force Approach
def gcdOfStrings(str1,str2):
    for i in range(min(len(str1),len(str2)),0,-1):
        candidate=str1[:i]
        def builds(s,x):
            return len(s) % len(x) == 0 and x * (len(s) // len(x)) == s

        if builds(str1, candidate) and builds(str2, candidate):
            return candidate

    return ""
    
"""Why str1 + str2 == str2 + str1?

It checks whether both strings are built from the same repeating pattern.

Example:
str1 = "ABCABC"
str2 = "ABC"
str1 + str2 = "ABCABCABC"
str2 + str1 = "ABCABCABC"  ✔ same

So a common base string exists.

❌ Counterexample:
str1 = "LEET"
str2 = "CODE"
str1 + str2 = "LEETCODE"
str2 + str1 = "CODELEET"  ❌ different

So answer is ""(Empty string) 
If a string x divides both str1 and str2, then:

str1 = x + x + x + ...
str2 = x + x + ...

So the length of x must divide both lengths of the strings.

👉 That means:

The length of the answer must be a common divisor of len(str1) and len(str2).

And we want the largest such string, so we take:

👉 the Greatest Common Divisor (GCD) of the lengths

📌 Step-by-step Example 1
Input:
str1 = "ABCABC"   (length = 6)
str2 = "ABC"      (length = 3)
Step 1: Find GCD of lengths
gcd(6, 3) = 3

So candidate answer length = 3

Step 2: Take prefix of str1
str1[:3] = "ABC"
We are not relying on str1 specifically
👉 We just use it as a convenient reference string

Because if a valid answer exists, it must be a prefix of both strings

🔑 Key Fact (Very Important)

If a string x divides both str1 and str2, then:

👉 x must be equal to:

a prefix of str1
a prefix of str2

So:

str1 starts with x
str2 starts with x

That means:

It does NOT matter whether we pick str1 or str2 —
both will give the same result """
#Intuition to remember
#Think of it like tiles:

#str1 = ABC | ABC
#str2 = ABC

#The “tile size” is fixed (GCD), and both strings are built f
# rom the same tile.
#So the tile is already identical no matter which string you inspect.
