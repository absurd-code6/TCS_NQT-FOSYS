'''Given a value V, we want to make change for V and we have infinite 
supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued notes, 
what is the minimum number of notes needed to make the change? 
You have to output all the denominations used to make this change. 
The biggest denomination should be displayed first followed 
by the smaller denominations. 

Suppose V = 93, the output should look like :- 

50 20 20 2 1 '''

def MinNotes(v,arr):
   for i in range(len(arr)-1,-1,-1):
       while v>=arr[i]:
           print(arr[i],end=" ")
           v-=arr[i]
           
arr= [1, 2, 5, 10, 20, 50, 100, 500, 1000]
# u can also use d(==denominations)= [1, 2, 5, 10, 20, 50, 100, 500, 1000]
v = int(input("Enter the value v:")) # 93
MinNotes(v,arr)
        
           
'''This code uses a greedy approach to make change with the minimum number of notes. The idea is simple: always pick the largest denomination possible first, then move to smaller ones.

🔧 How the code works
The list d contains denominations in ascending order.
The loop runs from the end to the start (len(d)-1 to 0), meaning it starts with the largest denomination (1000).
For each denomination d[i], it:
Keeps using it (while v >= d[i]) as long as it fits into the remaining value v.
Prints that denomination.
Subtracts it from v.

This ensures:

You always use the biggest note possible first.
You minimize the total number of notes.
🧪 Dry Run Example
Input:
v = 93
d = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
Execution:

Start from largest denomination:

Step 1: 1000, 500, 100
93 < 1000 → skip
93 < 500 → skip
93 < 100 → skip
Step 2: 50
93 ≥ 50 → use 50
Print: 50
Remaining v = 93 - 50 = 43
Step 3: 20
43 ≥ 20 → use 20
Print: 20
Remaining v = 23
23 ≥ 20 → use 20 again
Print: 20
Remaining v = 3
Step 4: 10, 5
3 < 10 → skip
3 < 5 → skip
Step 5: 2
3 ≥ 2 → use 2
Print: 2
Remaining v = 1
Step 6: 1
1 ≥ 1 → use 1
Print: 1
Remaining v = 0
✅ Final Output:
50 20 20 2 1'''       
  