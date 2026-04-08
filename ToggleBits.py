"""Joseph is learning digital logic subject which will be for his 
next semester. He usually tries to solve unit assignment problems 
before the lecture. Today he got one tricky question. 
The problem statement is “A positive integer has been given as an input. 
Convert decimal value to binary representation. Toggle all bits 
of it after the most significant bit including the most significant bit. 
Print the positive integer value after toggling all bits”.

Constraints-

1<=N<=100

Example 1:

Input :

10  -> Integer

Output :

5    -> result- Integer

Explanation:

Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”."""

n=int(input())
#Find no of bits in n
bits=n.bit_length() #gives number of bits needed to represent n
#Create mask with all bits set to 1
mask=(1<<bits)-1
#Toggle all bits
result = mask-n
print(result)

"""Why (1 << bits) - 1 gives 111...
Step-by-step
👉 What does 1 << bits mean?
Left shift (<<) moves bits to the left
Each shift = multiply by 2

Example for bits = 4:

1 << 4  →  10000  (binary)

That is:

2^4 = 16
👉 Now subtract 1:
10000
-    1
------
01111

So:

(1 << 4) - 1 = 01111 (which is 15)

💡 General idea:"""
#(1<<k)-1=2.pow(k)-1= a number with k ones in binary

"""Examples:

k	Binary result	Decimal
3	111	7
4	1111	15
5	11111	31
🔹 2. Why mask - n flips all bits

Let’s take your example:

👉 n = 10
n    = 1010
mask = 1111

Now subtract:

  1111   (15)
- 1010   (10)
-------
  0101   (5)
💡 What’s actually happening?

Each bit is being flipped:

Bit position	mask	n	result
1	1	1	0
2	1	0	1
3	1	1	0
4	1	0	1

So:

1010 → 0101
🔥 Key Insight

When you subtract from 111..., you are effectively doing:"""

#result=(2.pow(k)-1)-n

"""Which behaves exactly like bit flipping 
Connection to XOR

This is why:

mask - n   ≡   n ^ mask

Both give the same result:

1010 → 0101"""

'''One-liner Trick (Clean & Interview-Friendly)'''
#n = int(input())
#print((1 << n.bit_length()) - 1 - n)

'''Idea:
(1 << n.bit_length()) - 1 → creates a mask like 111...
Subtracting n flips all bits'''

'''XOR Approach (Very Important Concept)
Code:'''
#n = int(input())

#mask = (1 << n.bit_length()) - 1
#result = n ^ mask

#print(result)
'''Why XOR works?

XOR rule:

1 ^ 1 = 0
0 ^ 1 = 1
So when you XOR a number with 111..., all bits get flipped
🧪 Example (n = 10)

Binary:

n     = 1010
mask  = 1111
---------------
XOR   = 0101 → 5'''

#Intuition to remember
#(1 << k) - 1 → builds a “mirror” of all 1s
#Subtracting from it → flips bits
#XOR with it → also flips bits
