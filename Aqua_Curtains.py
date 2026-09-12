'''A furnishing company is manufacturing a new collection of curtains. 
The curtains are of two colors aqua(a) and black (b). 
The curtains color is represented as a string(str) 
consisting of a's and b's of length N. Then, they are 
packed (substring) into L number of curtains in each box. 
The box with the maximum number of 'aqua' (a) color curtains 
is labeled. 
The task here is to find the number of 'aqua' color curtains 
in the labeled box.

Note :

If 'L' is not a multiple of N, the remaining number of curtains 
should be considered as a substring too. In simple words, after 
dividing the curtains in sets of 'L', any curtains left will 
be another set(refer example 1)

Example 1:

Input :

bbbaaababa -> Value of str

3    -> Value of L

Output:

3   -> Maximum number of a's

Explanation:

From the input given above.

Dividing the string into sets of 3 characters each 

Set 1: {b,b,b}

Set 2: {a,a,a}

Set 3: {b,a,b}

Set 4: {a} -> leftover characters also as taken as another set

Among all the sets, Set 2 has more number of a's. 
The number of a's in set 2 is 3.

Hence, the output is 3.

Example 2:

Input :

abbbaabbb -> Value of str

5   -> Value of L

Output:

2   -> Maximum number of a's

Explanation:

From the input given above,

Dividing the string into sets of 5 characters each.

Set 1: {a,b,b,b,b}

Set 2: {a,a,b,b,b}

Among both the sets, set 2 has more number of a's. 
The number of a's in set 2 is 2.

Hence, the output is 2.

Constraints:

1<=L<=10

1<=N<=50

The input format for testing 

The candidate has to write the code to accept two inputs s
eparated by a new line.

First input- Accept string that contains character a and b only

Second input- Accept value for N(Positive integer number)

The output  format for testing

The output should be a positive integer number of print 
the message(if any) given in the problem statement.
(Check the output in Example 1, Example 2).
'''
curtain=str(input("Enter the string:"))
L=int(input("Enter the value of L:"))
count=0
max_val=0
for i in range(len(curtain)):
    if i%L==0:
        #This checks: “Is this index the start of a new 
        # group of size n?”
#Because every group starts at multiples of n:
#If n = 3, groups start at indices: 0, 3, 6, 9, ...
        max_val=max(count,max_val)
        #What it means
#count → number of 'a' in the previous group
#max_val → best (maximum) count found so far
#This line keeps the larger value
        count=0
#Since a new group starts, reset 'a' count
    if curtain[i]=='a':
        count+=1
if count>max_val:
    max_val=count
#The last group may not trigger i % n == 0 again
#So we manually check it after the loop      
'''Core Idea

During the loop, we update max_val only when a new group starts 
(i % n == 0).

👉 But the last group ends at the end of the loop,
so it doesn’t get a chance to update max_val inside the loop.

🧪 Example to Understand
Input:
str = "bbbaaababa"
n = 3
Groups:
bbb | aaa | bab | a
🚶 Step-by-step
🔹 Group 1: "bbb"
count = 0
Next group starts → we update max_val = 0
🔹 Group 2: "aaa"
count = 3
Next group starts → we update max_val = 3
🔹 Group 3: "bab"
count = 1
Next group starts → we update max_val = 3
🔹 Group 4 (LAST): "a"
count = 1

🚨 Now the loop ends here

No next group start
So i % n == 0 condition never triggers again

👉 That means this group's count is never compared with max_val
So that fix ensures: check the last group too before finishing!'''
print(max_val)

''' As an introverted military brat, I learned to ask FORM 
questions in order to quickly make friends to play with and 
to eat lunch with. "F" stands for friends/ family/ function. 
"O" stands for occupation/ observations/ obsessions. 
"R" stands for recreation/ relationships/ region/ religion. 
"M" stands for movies/ motivations/ memories/ message.
Remembering F.O.R.M. helps me get over the awkwardness of talking 
to new people.'''