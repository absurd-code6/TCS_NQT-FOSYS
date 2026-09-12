'''Given a string, split it into exactly 3 palindromic substrings. 
If it's not possible, print "Impossible". 
Input Format: • Single string 
Output Format: • Three lines: each palindromic substring, or 
"Impossible" 
Sample Input nayannamantenet 
Output nayan naman tenet'''

def split_three_palindromes(s):
    def isPalindrome(s):
        if s==s[::-1]:
            return 1
    
    n=len(s)
# We need at least 3 characters to make 3 substrings
    if n<3:
       print("Impossible")
# Loop for the first cut (i represents the end index of the 1st substring)
    for i in range(1,n-1):
#Optimize: If the first piece isn't a palindrome, don't bother 
# checking further
        Ist_piece=s[:i]
        if not isPalindrome(Ist_piece):
            continue
# Loop for the second cut (j represents the end index of the 2nd substring)
        for j in range(i+1,n):
            IInd_piece=s[i:j]
            IIIrd_piece=s[j:]
            # Check if both the second and third pieces are palindromes
            if isPalindrome(IInd_piece) and isPalindrome(IIIrd_piece):
                print(Ist_piece)
                print(IInd_piece)
                print(IIIrd_piece)
                return # Found a valid split, exit the function
    # If the loops finish without returning, no valid split exists        
    print("Impossible")

s=input() #"nayannamantenet"
split_three_palindromes(s)

'''To split a string into exactly 3 palindromic substrings, we are 
looking for two partition points (or cut marks) that divide 
the string into three pieces. Because we need exactly 3 pieces, 
we can simulate placing these cuts using a nested loop and 
verify if all three resulting pieces are palindromes.

Here is the mental blueprint and step-by-step logic to 
solve this problem efficiently.

1. The Mental BlueprintLet's use a shorter 
string like "ababa" as an example.
 
We want to place 2 cuts to make 3 pieces:
Piece 1: From the start to the first cut.
Piece 2: From the first cut to the second cut.
Piece 3: From the second cut to the end of the string.
We can try every possible combination of these two cuts. 

For example:
Try cuts at positions that give: a | b | aba.
We check each piece: "a" is a palindrome, 
"b" is a palindrome, and "aba" is a palindrome.
 
We found a valid split!If we try all combinations of cuts 
and none of them yield 3 palindromes, 
then it is Impossible.

2. Developing the Code LogicThe Outer Loop (First Cut): 
This cut index $i$ will go from position 1 up to the end of the string. 

The first piece will be s[:i].The Inner Loop (Second Cut): 
This cut index j will start right after the first cut (i + 1) 
and go up to the end of the string. The second piece will be s[i:j] 
and the third piece will be s[j:].

The Palindrome Check: Python makes checking for a palindrome 
incredibly easy with string slicing: substring == substring[::-1].

Why This Works Efficiently
For an interview context, this brute-force approach with pruning runs in
O(n^3) time in the worst case (where n is the length of the string), 
because we have two nested loops running up to n and a palindrome check 
taking O(n).

For typical interview string lengths (e.g., n≤1000), this loop
structure executes well within the time limit. The key optimization 
is the continue statement on line 12: if part1 is trash, we skip the 
entire inner loop completely, pruning a massive amount 
of unnecessary work!'''