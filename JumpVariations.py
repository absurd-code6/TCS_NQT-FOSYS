'''def minJumps(arr):
    if len(arr)==1:
        return 0
    if arr[0]==0:
        return -1
    reach=arr[0]
    steps=arr[0]
    jumps=1
    
    for i in range(1,len(arr)):
        if i==len(arr)-1:
            return jumps
        reach=max(reach,i+arr[i])
        steps-=1
        if steps==0:
            jumps+=1
            if i>=reach:
                return -1
            steps=reach-i
    return -1'''
# Variations
'''Can Reach End or Not (Jump Game I)

Instead of minimum jumps:

Return True/False whether reaching the end is possible.

Example:

[3,2,1,0,4]

Output:

False'''
def reachable(arr):
    if arr[0]==0:
        return False
    reach=0
    for i in range(len(arr)):
        if i>reach:
            return False
        reach=max(reach,i+arr[i])
    return True

arr=[3,2,1,12,4]
#arr=[1] #last index is reachable -> True
print(reachable(arr))

'''Print the Actual Path(Minimum Jump Path)

Instead of minimum count:

Print indices used in optimal jumps.

Example:

[1,3,5,8,9]

Possible output:

0 → 1 → 4
Twist

Now you must store:

parent indices
chosen jump positions

Usually solved using:

BFS
DP
path reconstruction'''
def jumpPath(arr):
    n=len(arr)
    if arr[0]==0:
        return -1
    path=[0] # a list for storing the indices(0 as usual will be there)
    pos=0
    while pos<n-1:
        if pos + arr[pos]>=n-1: # in case we can directly reach end
            path.append(n-1)
            break
        best=pos
        farthest=0
        
        for i in range(pos+1,pos+arr[pos]+1):
            if i+arr[i]>farthest:
                farthest=i+arr[i]
                best=i
        if best==pos: #Stuck condition
            return -1
        path.append(best)
        pos=best
    return path
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = jumpPath(arr)

print("Path:", result)
print("Minimum jumps:", len(result) - 1)

'''Exact Jump Length

Instead of:

up to arr[i]

Question becomes:

exactly arr[i]
Example
[2,3,1,1,4]

From index 0, must jump exactly 2.

Twist

Now:

graph traversal
cycle detection
BFS/DFS

may be needed.

6. Maximum Jumps Possible

Question:

Find maximum jumps before reaching end.

Twist

Greedy changes completely.

Need:

DP
recursion
memoization
7. Count Number of Ways to Reach End

Instead of minimum jumps:

How many different ways exist?

Example
[2,3,1]

Possible paths:

0→1→2
0→2

Answer:

2
Twist

Classic DP counting problem.

8. Weighted Jump Game

Each jump has:

energy
penalty
reward

Need:

minimum energy
maximum score
Twist

Transforms into:

graph shortest path
DP optimization
9. Circular Jump Array

Array becomes circular.

Example:

[2,1,2]

Can wrap around.

Twist

Need:

visited tracking
cycle handling
10. 2D Jump Game

Grid instead of array.

Example:

[
 [2,1,0],
 [1,3,1],
 [0,1,2]
]
Twist

Moves in:

right
down
multiple directions

Usually:

BFS
shortest path
11. Minimum Jumps With Obstacles

Some cells blocked.

Example:

[-1 means blocked]
Twist

Need:

BFS
graph traversal
12. Jump Game with Backward Jumps

Can jump:

forward
backward
Twist

Greedy fails completely.

Need:

BFS
visited states
13. Multi-Query Version

You get many queries:

minimum jumps from i to j
Twist

Need preprocessing:

segment trees
sparse tables
graph preprocessing
14. Online Streaming Version

Array elements arrive one by one.

Need:

Continuously determine reachability.

Twist

Tests:

incremental greedy logic
streaming algorithms
15. Interview Follow-Up Questions

Interviewers often ask:

A. Why does greedy work?

Expected answer:

We always expand the farthest reachable range.
Delaying jumps gives optimal jump count.
B. Why not DP?

Expected:

DP = O(n²)
Greedy = O(n)
C. What is the intuition behind steps?

Expected:

Remaining range of current jump.
D. Why steps = reach - i?

Expected:

New jump range length.
16. Hidden Edge Cases Interviewers Love
Case 1
[0]

Answer:

0

Already at destination.

Case 2
[0,1]

Answer:

-1

Cannot move.

Case 3
[1,0,1]

Answer:

-1

Get stuck at index 1.

Case 4
[2,0,0]

Answer:

1

Direct jump possible.'''
