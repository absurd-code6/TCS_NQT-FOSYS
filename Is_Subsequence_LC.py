'''Given two strings s and t, return true if s is a subsequence of t, or 
false otherwise.
A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (i.e., "ace" is a 
subsequence of "abcde" while "aec" is not).
 
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''
s=input()
t=input()
i=0
j=0
while i<len(s) and j<len(t):
    if s[i]==t[j]:
      i+=1
    j+=1

if i==len(s):
    print("true")
else:
    print("false")

#As a Function
def is_subsequence(s,t):
    i=0
    j=0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)

s=input()
t=input()
print(*str(is_subsequence(s,t)).lower())


'''This code determines whether a string s is a subsequence of another string t.

A subsequence means you can find all the characters of string s inside string t, 
in the exact same relative order, though not necessarily right next to each 
other (meaning there can be other characters scattered in between).

How It Works: The Two-Pointer Approach
The code uses a classic two-pointer technique, where two independent markers 
(i and j) scan through the strings at the same time.

Here is the step-by-step breakdown:

Initialization: i starts at the beginning of string s (index 0), and j starts 
at the beginning of string t (index 0).

The Loop: The while loop runs as long as neither pointer has run off the end 
of its respective string.

The Matching Logic:

if s[i] == t[j]: If the characters match, it means we found the next 
letter we were looking for in s. The pointer i moves forward (i += 1) 
to look for the next character of s.

j += 1: Regardless of whether there was a match or not, the pointer j 
moves forward to scan the next character in t.

The Evaluation: return i == len(s)

If i successfully reached the very end of string s, it means every single 
character was found in order, so it returns True.

If the loop finishes and i hasn't reached the end, it returns False.

Example Walkthrough
Let's say s = "abc" and t = "ahbgdc".

Step 1: s[0] is 'a', t[0] is 'a'. Match! i becomes 1, j becomes 1.

Step 2: s[1] is 'b', t[1] is 'h'. No match. j becomes 2.

Step 3: s[1] is 'b', t[2] is 'b'. Match! i becomes 2, j becomes 3.

Step 4: s[2] is 'c', t[3] is 'g'. No match. j becomes 4.

Step 5: s[2] is 'c', t[4] is 'd'. No match. j becomes 5.

Step 6: s[2] is 'c', t[5] is 'c'. Match! i becomes 3, j becomes 6.

The loop ends because j reached the end of t. Since i equals 3 
(the length of "abc"), the function returns True.

What does the final print line do?
Python
print(*str(is_subsequence(s,t)).lower())
This is a quirky way to format the output.

is_subsequence(s,t) returns a boolean like True.

str(...) converts it to the text "True".

.lower() changes it to "true".

The asterisk * unpacks the string into individual characters separated by spaces.

So instead of printing True, it prints: t r u e'''