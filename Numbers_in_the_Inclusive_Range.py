'''Given two non-negative integers n1 and n2, count how many numbers 
in the range [n1, n2] do not have repeated digits. 
Input Format: • 
Two integers: n1 n2 
Output Format: • Single integer: count of numbers 
without repeated digits 
Sample Input  1: 11 15 
Output 4 
Sample Input 2: 10 13'''

def non_repeating_digits(n1,n2):
    count=0
    for num in range(n1,n2+1):
        s=str(num)
        if len(s)==len(set(s)):
            count+=1
    return count

n1=int(input())
n2=int(input())
non_repeating_digits(n1,n2)

'''Approach

For every number from n1 to n2:

Convert the number to a string.
Check if the number of unique characters equals the string length.
If yes, increment the count.
Print the final count.'''

#Dry Run

'''Suppose the input is:

11 15

We check each number one by one.

Step 1: Number = 11
s = "11"
set(s) = {'1'}

len(s) = 2
len(set(s)) = 1

2 != 1

Digits are repeated.

count = 0
Step 2: Number = 12
s = "12"
set(s) = {'1','2'}

len(s) = 2
len(set(s)) = 2

Equal

No repeated digits.

count = 1'''