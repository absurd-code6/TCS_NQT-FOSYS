from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list) # adjacency list
        self.V=vertices
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
'''What does self.V = vertices mean?
This line says:
👉 “Create an attribute called V inside this object, and store vertices in it.”

Why no prior declaration is needed?

In Python, you don’t declare instance variables in advance.

They are created on the fly when you assign them.

So this:

self.V = vertices

does two things at once:

Creates a new attribute V inside the object
Assigns it the value of vertices
Intuition (very important)

Think of self like a dictionary attached to the object:

self.__dict__ = {}

When you do:

self.V = 5

it’s basically:

self.__dict__['V'] = 5

So Python is just dynamically adding a new key.

Example to make it click
class Test:
    def __init__(self):
        self.x = 10   # created here

Now:

t = Test()
print(t.x)   # works

But if you try:

print(t.y)

You’ll get:

AttributeError: 'Test' object has no attribute 'y'

Because y was never created.

Let’s break down this exact line very clearly:

self.graph[u].append(v)
Step-by-step meaning
1. self

Refers to the current object (your graph instance).

2. self.graph

This accesses an attribute of the object.

Earlier you wrote:

self.graph = defaultdict(list)

So:
👉 self.graph is a dictionary-like structure
👉 Each key maps to a list

Example:

{
  0: [1, 2],
  1: [3]
}
3. self.graph[u]

This means:
👉 “Get the list stored at key u”

Because it's a defaultdict(list):

If u does not exist, Python automatically creates:

u: []

So:

self.graph[0]

might return:

[]

(if it didn’t exist before)

4. .append(v)

This is a list operation.

👉 It adds v to the list

So:

[].append(1)

becomes:

[1]
Putting it all together
self.graph[u].append(v)

means:

👉 “Go to node u, and add v to its adjacency list”

Visual intuition

If you run:

g.add_edge(0, 1)
g.add_edge(0, 2)

Internally:

self.graph[0] → []
append 1 → [1]
append 2 → [1, 2]

Final structure:

{
  0: [1, 2]
}'''

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
print(g.graph)

#By User Input
V=int(input("Enter the no of vertices:"))
E=int(input("Enter the no of edges:"))
gr=Graph(V) #Creating Graph object
print("Enter edges in the format 'u v' (from u to v):")
for _ in range(E):
    u,v=map(int,input().split())
    gr.add_edge(u,v)
print("Graph Adjacency List:")
gr.display()

/temp = input().split() 
V = int(temp[0])
E = int(temp[1])
g = Graph(V)
temp = input().split()
for i in range(E):
    u = int(temp[2*i])
    v = int(temp[2*i+1])
    g.addEdge(u,v)/

#Enter the number of vertices: 3
#Enter the number of edges: 3
#Enter edges in the format 'u v' (from u to v):
#0 1
#0 2
#1 2

#This is a different, compact style of reading input, often used in c
# ompetitive programming or when all input is given in a single line.
#temp = input().split()
#input() reads a line of input as a string.
#.split() splits it into a list of strings by spaces.

'''Example:

Input: "3 3"
input() → "3 3" (string)
.split() → ["3", "3"] (list of strings)
2. V = int(temp[0]) and E = int(temp[1])
Converts the first element to integer → number of vertices V
Converts the second element to integer → number of edges E'''

#So with "3 3":

#V = 3
#E = 3
#3. g = Graph(V)
#Creates a new graph with V vertices.
'''Graph uses the adjacency list internally (like we discussed with 
defaultdict(list)).
4. temp = input().split() for edges
Here, all edges are given in a single line.
Example input:
0 1 0 2 1 2
.split() → ["0", "1", "0", "2", "1", "2"]

This is a flattened list of all edge pairs:

Edge 1: 0 → 1
Edge 2: 0 → 2
Edge 3: 1 → 2
5. for i in range(E):
Loops over the number of edges.'''
#6. u = int(temp[2*i]) and v = int(temp[2*i+1])
#Each edge takes two consecutive elements in the temp list.
#i = 0 → first edge: u = temp[0], v = temp[1] → 0, 1
#i = 1 → second edge: u = temp[2], v = temp[3] → 0, 2
#i = 2 → third edge: u = temp[4], v = temp[5] → 1, 2
#7. g.addEdge(u,v)
#Adds the edge from u to v to the graph’s adjacency list.
#✅ Example

'''Input:

3 3
0 1 0 2 1 2

Step by step:

temp = ["3", "3"] → V = 3, E = 3
temp = ["0","1","0","2","1","2"]
Loop:
i=0 → u=0, v=1
i=1 → u=0, v=2
i=2 → u=1, v=2'''

#Output adjacency list:

#0 -> [1, 2]
#1 -> [2]
        
'''self.graph = defaultdict(list)
Here's why this is key:
self.graph is an adjacency list representation of the graph.
defaultdict(list) means:
If a key (vertex) doesn't exist, it automatically creates an empty list 
for that vertex.
This avoids key errors when adding edges.
That means every time we try to access a key that doesn't exist, Python automatically creates an empty list as the value.

What happens internally
g.add_edge(0, 1)
self.graph[0] does not exist yet.
defaultdict automatically does: self.graph[0] = []
Then 1 is appended → self.graph[0] = [1]
g.add_edge(0, 2)
self.graph[0] already exists → [1]
Append 2 → [1, 2]
g.add_edge(1, 2)
self.graph[1] does not exist yet
defaultdict automatically creates self.graph[1] = []
Append 2 → [2]
Step 4: Output
0 -> [1, 2]
1 -> [2]

✅ Notice:

We never had to check if the key existed before appending.
If we used a normal dictionary, we would need:
if u not in self.graph:
    self.graph[u] = []
self.graph[u].append(v)
defaultdict(list) saves us from that extra check.''' 
      