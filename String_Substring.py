#Check if a string is substring of another
'''
Given two strings txt and pat, the task is to find if pat is 
a substring of txt. If yes, return the index of 
the first occurrence, 
else return -1.

Examples : 

Input: txt = "geeksforgeeks", pat = "eks"
Output: 2
Explanation: String "eks" is present at index 2 and 10, so 2      
is the smallest index.

Input: txt = "geeksforgeeks", pat = "xyz"
Output: -1.
Explanation: There is no occurrence of "xyz" in "geeksforgeeks" '''

#Shortcut

txt = "geeksforgeeks"
pat = "eks"

# 1. To get the index (matches your function's behavior)
index = txt.find(pat)  # Returns idx, or -1 if not found

# 2. To just get a True/False check
is_substring = pat in txt  # Returns True
print(index)
print(is_substring)

txt="geeksforgeeks"
pat="eks"

def Substring(txt,pat):
    n=len(txt)
    m=len(pat)
    for i in range(n-m+1):
        #Why n - m + 1? > If the text has 13 characters and the 
        # pattern has 3, there is no point in checking 
        # starting positions beyond index 10. A 3-character pattern cannot 
        # physically fit into the last 2 characters of a string. 
        # This optimization prevents unnecessary checks and 
        # out-of-bounds errors.
        j=0
        while j<m and txt[i+j]==pat[j]:
            j+=1
        if j==m:
            return i #idx of 1st occurence
    return -1

print(Substring(txt,pat))#O/p=2
'''Step 2: Sliding the Window (The Outer Loop)
The variable i represents the current starting position 
in txt where we are trying to match the pattern.

When i = 0, we are comparing pat against the substring "gee".

When i = 1, we slide right and compare pat against "eek".

When i = 2, we slide right and compare pat against "eks".

Step 3: Character-by-Character Verification (The Inner Loop)
At each position i, the code resets a pointer j = 0. 
This pointer tracks our progress inside the pattern pat.
The while loop checks two things before moving forward:

j < m: Have we looked past the end of the pattern yet?

txt[i + j] == pat[j]: Does the character in the text match 
the corresponding character in our pattern?

Notice the index i + j. As j increments to look at the 
next character in the pattern, i + j ensures we look at the 
next character in the text relative to our current 
starting position i.

Step 4: Checking for Success or Failure
If the inner while loop finishes, there are two r
easons why it stopped:

A mismatch occurred: The characters didn't match, so j 
stopped incrementing early (j < m). The code moves to the 
next iteration of the outer loop (i increases), sliding 
the window forward.

A perfect match was found: The loop checked every single 
character successfully, meaning j reached the value of m (3). 
If j == m, it means the pattern was fully found, and the code 
immediately returns i (the starting index in the text).'''
