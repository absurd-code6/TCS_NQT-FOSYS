'''Given a string s and an integer k, return the maximum number of vowel 
letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.'''

# Read input from standard input
s = input().strip()
k = int(input().strip())# u may or may not use strip() it's jst 
#a safe programming habit of developers.

vowels = {'a', 'e', 'i', 'o', 'u'}

# Count vowels in the first window of size k
current_vowels = sum(1 for char in s[:k] if char in vowels)
#This line of code is a compact, elegant Python shortcut. 
# It counts how many vowels are in the first k letters of the string s.
#To understand how it works, we can break it down into three parts:

'''. The Slice: s[:k]This gets a portion of your string.[:k] 
tells Python to start at the very beginning (index 0) and 
stop right before index k.If s = "abeco" 
and k = 3, then s[:3] gives us the substring "abe".
2. The Generator Expression: (1 for char in s[:k] if char in vowels)
This is a loop squeezed into a single line. 
It says:"Go through each character in our sliced string. 
If that character is a vowel, yield the number 1.
"Let's look at how it processes "abe" 
step-by-step:'a': Is it in vowels? Yes,Yields a 
1.'b': Is it in vowels? No,Yields nothing.
'e': Is it in vowels? Yes ,Yields a 1.
By the end of this loop, we have generated a stream of ones: 1, 1.
3.The Outer Function: sum(...)T he sum() function takes 
that stream of generated ones and adds them up -> {sum}(1, 1) = 2
So, current_vowels is set to 2.'''

'''The "Plain English" Equivalent
If you wrote this out using a standard for loop, it would look l
ike this:'''
#current_vowels = 0

# Grab the first k characters
#first_window = s[:k] 

# Loop through and count
#for char in first_window:
    #if char in vowels:
        #current_vowels += 1  
# This is the "+= 1" that the "sum(1 for...)" does!
#The single-line version is faster to write and highly 
# optimized in Python.

max_vowels = current_vowels

# Slide the window across the string
for i in range(k, len(s)):
    # Add the new character entering the window
    if s[i] in vowels:
        current_vowels += 1
    # Remove the old character leaving the window
    if s[i - k] in vowels:
        current_vowels -= 1
        
    # Keep track of the maximum found
    if current_vowels > max_vowels:
        max_vowels = current_vowels

print(max_vowels)

'''Let's use a simple example:

s = "abeco"

k = 3 (our window is 3 letters wide)

Our vowels are: {'a', 'e', 'i', 'o', 'u'}

Part 1: The First Window (Indices 0 to 2)
The code starts by looking at the very first window of 
size k (the first 3 letters): "abe".

Letters inside: 'a' (vowel), 'b' (not), 'e' (vowel).

current_vowels = 2

max_vowels = 2

Part 2: Sliding the Window
Now, we slide the window to the right, one step at a time. 
The loop starts at index i = k (which is index 3).

Step 1: Slide to index i = 3 (letter 'c')
Our window shifts from "abe" to "bec".

Who is entering? The letter at index i (s[3] → 'c').

Is 'c' a vowel? No. current_vowels stays at 2.

Who is leaving? The letter at the very back of the 
old window (s[i - k] → s[3 - 3] → s[0] → 'a').

Is 'a' a vowel? Yes! Since a vowel left our window, we subtract 1.

current_vowels becomes 1 (2-1).

Compare: Is our new count (1) higher than our maximum record (2)? No.

max_vowels stays 2.

Step 2: Slide to index i = 4 (letter 'o')
Our window shifts from "bec" to "eco".

Who is entering? The letter at index i (s[4] → 'o').

Is 'o' a vowel? Yes! We add 1.

current_vowels becomes 2 (1+1).

Who is leaving? The letter at the back of the old window 
(s[i - k] → s[4 - 3] → s[1] → 'b').

Is 'b' a vowel? No. We do not subtract anything.

current_vowels stays 2.

Compare: Is our new count (2) higher than our maximum record (2)? 
No, it's a tie.

max_vowels stays 2.

Final Output
The loop ends because we reached the end of the string. 
The program prints max_vowels, which is 2 
(found in our first window "abe" and our last window "eco").'''