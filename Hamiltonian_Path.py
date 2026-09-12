#Backtracking Problem(Skwz)
'''A Hamiltonian path is a path in an undirected or directed graph 
that visits each vertex exactly once. Given an undirected graph, 
the task is to check if a Hamiltonian path is present in it or not. 
If a hamiltonian path is present in the graph, then print 1 
otherwise print 0. '''

def ham(adj_list,curnode):
    global pointer,freq
    if all(freq):
        pointer=1
        return
    for nbr in adj_list[curnode]:
        if freq[nbr]==0:
            freq[nbr]=1
            ham(adj_list,nbr)
            freq[nbr]=0
            
#if __name__=="__main__":
global freq
global pointer
freq=[]
pointer=0
adj_list=[]
temp=input().split()
n=int(temp[0]) #no of vertices v
m=int(temp[1]) #no of edges e
for i in range(0,n):
    freq.append(0)
    adj_list.append([])
temp=input().split()
for i in range(0,m):
    a=int(temp[2*i])
    b=int(temp[2*i+1])
    a-=1
    b-=1
    adj_list[a].append(b)
    adj_list[b].append(a)
freq[0]=1
ham(adj_list,0)
print(pointer)


'''This code checks whether an undirected graph contains a Hamiltonian 
path using backtracking (DFS).

🔧 Core Idea

A Hamiltonian path must:

Visit every vertex exactly once

The code:

Builds an adjacency list (ar)
Uses a freq array to track visited nodes
Recursively explores all possible paths using DFS
If all nodes are visited (all(freq)), it sets pointer = 1
🧠 Function Breakdown
ham(ar, s)
s = current node
For each neighbor of s:
If not visited:
Mark visited
Recurse
Backtrack (unmark)
Key condition:
if all(freq):
    pointer = 1

If all nodes are visited → Hamiltonian path found.

📥 Input Format
n m
u1 v1 u2 v2 ... um vm
n = number of vertices
m = number of edges
▶️ Dry Run Example
Input:
4 3
1 2 2 3 3 4
Graph:
1 — 2 — 3 — 4
Step 1: Initialization
freq = [0, 0, 0, 0]
pointer = 0

Start DFS from node 0 (vertex 1):

freq[0] = 1
Step 2: DFS Traversal
Call: ham(ar, 0) (node 1)
Neighbor: node 2 (1)
Mark visited → freq = [1,1,0,0]
Recurse → ham(ar,1)
Call: ham(ar, 1) (node 2)
Neighbor: node 3 (2)
Mark visited → freq = [1,1,1,0]
Recurse → ham(ar,2)
Call: ham(ar, 2) (node 3)
Neighbor: node 4 (3)
Mark visited → freq = [1,1,1,1]

✅ Now:

all(freq) = True
→ pointer = 1
Step 3: Backtracking

After finding one valid path:

1 → 2 → 3 → 4

The recursion unwinds.

Final Output:
1
❌ Example Without Hamiltonian Path
Input:
4 2
1 2 3 4

Graph:

1 — 2     3 — 4

No way to visit all nodes in one path.

Output:
0
⚠️ Important Notes
Starts DFS only from node 0 → may miss paths starting elsewhere
Time complexity is O(N!) (tries all permutations)
Works well for small graphs

The “current node” changes because of this line:

ham(ar, nei)

Here, nei (a neighbor of the current node s) is passed into the next recursive call. So instead of incrementing s like s+1, the code moves to whatever neighbor is connected in the graph.

🔁 Step-by-step clarification

Inside the function:

for nei in ar[s]:
ar[s] = list of neighbors of node s
So nei takes values from the adjacency list

Then:

ham(ar, nei)
This means: “Go to that neighbor and continue DFS from there”
🧪 Concrete Example

Graph:

1 — 2 — 3 — 4

Internally (0-based):

0 — 1 — 2 — 3

Adjacency list:

ar = [
  [1],        # neighbors of 0
  [0,2],      # neighbors of 1
  [1,3],      # neighbors of 2
  [2]
]
Execution flow

Start:

ham(ar, 0)
Call 1:
s = 0
ar[0] = [1]
nei = 1

Call:

ham(ar, 1)
Call 2:
s = 1
ar[1] = [0,2]
nei = 0 → already visited ❌
nei = 2 → not visited ✅

Call:

ham(ar, 2)
Call 3:
s = 2
ar[2] = [1,3]
nei = 3

Call:

ham(ar, 3)
🚨 Key Insight

The sequence:

0 → 1 → 2 → 3

comes from:

Following edges in the graph
Not from incrementing like 0 → 1 → 2 → 3 numerically
⚡ Bottom line
s does NOT increase automatically

The “next node” is chosen from:

for nei in ar[s]
The recursion moves along graph connections, not numeric order

Declare global variables
global freq
global pointer
Makes these variables accessible inside functions like ham()
freq → tracks visited nodes
pointer → result flag (1 = path exists, 0 = not)
2. Initialize variables
pointer = 0
freq = []
ar = []
pointer = 0 → assume no Hamiltonian path initially
freq = [] → empty visited array
ar = [] → adjacency list (graph)
3. Read number of nodes and edges
temp = input().split()
n = int(temp[0])
m = int(temp[1])
Input like: 4 3
n = number of vertices
m = number of edges
4. Initialize graph structure
for i in range(0, n):
    freq.append(0)
    ar.append([])

After this:

freq = [0, 0, 0, 0] → all nodes unvisited
ar = [[], [], [], []] → empty adjacency list
5. Read edges
temp = input().split()
for i in range(0, m):
    a = int(temp[2*i])
    b = int(temp[2*i+1])
Input example: 1 2 2 3 3 4
Reads edges in pairs:
(1,2), (2,3), (3,4)
6. Convert to 0-based indexing
a -= 1
b -= 1
Python lists start at index 0
So node 1 (means) -> 0, 2 → 1(2 means 1), etc.
7. Build adjacency list (undirected graph)
ar[a].append(b)
ar[b].append(a)
Adds both directions because the graph is undirected

Example result:

ar = [
  [1],      # node 0 connected to 1
  [0,2],    # node 1 connected to 0,2
  [1,3],    # node 2 connected to 1,3
  [2]
]
8. Start DFS from node 0
freq[0] = 1
ham(ar, 0)
Mark node 0 as visited
Start recursive search from node 0

⚠️ Important limitation:

It only starts from node 0
Might miss Hamiltonian paths starting elsewhere
9. Print result
print(pointer)
1 → Hamiltonian path exists
0 → does not exist

The Code
for i in range(0, m):
    a = int(temp[2*i])
    b = int(temp[2*i+1])
🧠 What temp looks like

Earlier, you did:

temp = input().split()

If the input is:

1 2 2 3 3 4

Then:

temp = ['1', '2', '2', '3', '3', '4']

👉 It's a flat list, not grouped into pairs.

🔁 How the loop works

You want to read edges like:

(1,2), (2,3), (3,4)

Instead of grouping beforehand, the code uses indexing:

i	2*i	2*i+1	Edge(After a-=1 and b-=1)
0	0	1	(1,2)
1	2	3	(1,2)
2	4	5	(3,4)

Why 2*i?

Because:

Each edge uses 2 numbers
So every new edge starts 2 steps ahead
⚠️ Important assumption

This only works if:

len(temp) == 2 * m

(i.e., exactly 2 numbers per edge)
The lines
ar[a].append(b)
ar[b].append(a)
🧠 What is ar?

ar is an adjacency list.

That means:

ar[i] stores all neighbors of node i

Example:

ar = [[], [], [], []]

This means:

Node 0 → no neighbors yet
Node 1 → no neighbors yet
Node 2 → no neighbors yet
Node 3 → no neighbors yet
🔗 Suppose we read an edge: 1 2

After converting to 0-based:

a = 0
b = 1
🔁 What happens now?
Line 1:
ar[a].append(b)

👉 Add b as a neighbor of a

So:

ar[0].append(1)

Now:

ar = [[1], [], [], []]
Line 2:
ar[b].append(a)

👉 Add a as a neighbor of b

So:

ar[1].append(0)

Now:

ar = [[1], [0], [], []]
🎯 Why do we add both?

Because the graph is undirected.

If:

1 — 2

Then:

From 1, you can go to 2
From 2, you can go to 1

So both must be stored.

🔍 Full Example

Input:

1 2
2 3
Step-by-step:
Edge 1: (1,2) → (0,1)
ar[0].append(1)
ar[1].append(0)
ar = [[1], [0], []]
Edge 2: (2,3) → (1,2)
ar[1].append(2)
ar[2].append(1)
ar = [[1], [0,2], [1]]
📌 Final structure
ar = [
  [1],      # node 0 connected to 1
  [0, 2],   # node 1 connected to 0 and 2
  [1]       # node 2 connected to 1
]
🔁 How this helps DFS

Later, when you do:

for nei in ar[s]:

It means:
👉 “Go through all neighbors of node s”

⚡ Simple analogy

Think of:

ar[a].append(b)

as:
👉 “Write down that a can go to b”

and:

ar[b].append(a)

as:
👉 “Write down that b can go to a”

🚫 What if you remove one line?

If you only keep:

ar[a].append(b)

Then the graph becomes directed:

You can go a → b
But NOT b → a

That would break this problem.'''  
  