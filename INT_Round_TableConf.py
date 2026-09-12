'''An international round table conference will be held in india. 
Presidents from all over the world representing their respective 
countries will be attending the conference. 
The task is to find the possible number of ways(P) to make the N 
members sit around the circular table such that.

The president and prime minister of India will always 
sit next to each other.

Example 1:

Input :

4   -> Value of N(No. of members)

Output : 

12  -> Possible ways of seating the members

Explanation:

2  members should always be next to each other. 

So, 2 members can be in 2!ways

Rest of the members can be arranged in (4-1)! ways.(1 is subtracted because 
the previously selected two members will be considered as single members now).

So total possible ways 4 members can be seated around the circular table 2*6= 12.

Hence, output is 12.

Example 2:

Input:

10  -> Value of N(No. of members)

Output :

725760 -> Possible ways of seating the members 

Explanation:

2 members should always be next to each other.

So, 2 members can be in 2! ways 

Rest of the members can be arranged in (10-1)! Ways. (1 is subtracted because 
the previously selected two members will be considered as a single member now).

So, total possible ways 10 members can be seated around a round table is 

2*362880 = 725760 ways.

Hence, output is 725760.

The input format for testing

The candidate has to write the code to accept one input 

First input - Accept value of number of N(Positive integer number)

The output format for testing 

The output should be a positive integer number or print the message(if any) 
given in the problem statement(Check the output in example 1, example2)

Constraints :

2<=N<=50
'''
N=int(input("Enter the number of members:"))
fact=[0]*(N+1)
'''This creates a list of size n+1
All values are initially 0

👉 For n = 5, this becomes:

fact = [0, 0, 0, 0, 0, 0]

(6 elements because of n + 1)'''
fact[0]=1
'''We know:
0! = 1, so we store it

👉 Now:

fact = [1, 0, 0, 0, 0, 0]'''
for i in range(1,N+1):
    fact[i]=fact[i-1]*i
'''This loop calculates factorials step by step using:

i! = (i-1)! × i
Iteration by iteration:
i = 1
fact[1] = fact[0] * 1 = 1 * 1 = 1
→ [1, 1, 0, 0, 0, 0]
i = 2
fact[2] = fact[1] * 2 = 1 * 2 = 2
→ [1, 1, 2, 0, 0, 0]
i = 3
fact[3] = fact[2] * 3 = 2 * 3 = 6
→ [1, 1, 2, 6, 0, 0]
i = 4
fact[4] = fact[3] * 4 = 6 * 4 = 24
→ [1, 1, 2, 6, 24, 0]
i = 5
fact[5] = fact[4] * 5 = 24 * 5 = 120
→ [1, 1, 2, 6, 24, 120]'''
print(fact[N-1]*2)#No of possible seating arrangements
'''fact[n - 1] = (n-1)!
Then multiplied by 2

👉 For n = 5:

fact[4] = 24
Output = 24 * 2 = 48'''
