'''A Hamiltonian path is a path in an undirected or directed graph 
that visits each vertex exactly once. Given an undirected graph, 
the task is to check if a Hamiltonian path is present in it or not. 
If a hamiltonian path is present in the graph, then print 1 
otherwise print 0.'''

# Skwz solution:

def ham(ar, s):
    	global pointer
	global freq
	flag=0
	for x in freq:
		if x==0 :
			flag=1
			break
	if flag==0 :
		pointer=1
	else :
		for x in ar[s] :
			if freq[x]==0 :
				freq[x]=1
				ham(ar,x)
				freq[x]=0
                
                
if __name__=="__main__":
	global freq
	global pointer
	pointer=0
	freq=[]
	ar=[]
	temp = input().split()
	n=int(temp[0])
	m=int(temp[1])
	for i in range(0,n):
		freq.append(0)
		ar.append([])
	temp = input().split()
	for i in range(0,m):
		a=int(temp[2*i])
		b=int(temp[2*i+1])
		a-=1
		b-=1
		ar[a].append(b)
		ar[b].append(a)


	freq[0]=1
	ham(ar,0)
	print(pointer)


'''his version of the code is essentially the same algorithm as before, 
just written a bit more explicitly. Let’s break down what changed and 
how it works.

🔹 Key difference from previous version

Earlier you had:

if all(freq):
    pointer = 1

Now it’s replaced with:

flag = 0
for x in freq:
    if x == 0:
        flag = 1
        break

if flag == 0:
    pointer = 1
🧠 What this means

This is just a manual way of checking:

👉 “Are all nodes visited?”

If any 0 exists in freq → not all visited
If no 0 exists → all visited → Hamiltonian path found

So:

Condition	Meaning
flag = 1	Some node is unvisited
flag = 0	All nodes visited ✅
🔁 Function Flow
Function:
def ham(ar, s):
Step 1: Check if all nodes are visited
flag = 0
for x in freq:
    if x == 0:
        flag = 1
        break
Loop through freq
If any node is unvisited → stop early
Step 2: If all visited
if flag == 0:
    pointer = 1

👉 Hamiltonian path found

Step 3: Otherwise, continue DFS
else:
    for x in ar[s]:
        if freq[x] == 0:
            freq[x] = 1
            ham(ar, x)
            freq[x] = 0

This is standard backtracking:

Try a neighbor
Mark visited
Recurse
Undo (backtrack)
🔍 Important Observation

This version is actually slightly less efficient than the previous 
one because:

It checks the entire freq list every recursive call
Even when you’re far from finishing

Whereas:

if all(freq):

is shorter and cleaner (but still O(n))

⚠️ Same limitation still exists
freq[0] = 1
ham(ar, 0)

👉 It only starts from node 0

So it may miss valid Hamiltonian paths that start from other nodes.

🧪 Quick Example

Graph:

1 — 2 — 3

Steps:

freq = [1,0,0]  (start at node 0)

→ go to 1 → freq = [1,1,0]
→ go to 2 → freq = [1,1,1]

Now:
no 0 in freq → flag = 0 → pointer = 1 ✅
⚡ Bottom Line
This version = same logic, just written manually
flag replaces all(freq)
DFS + backtracking still drives the solution
Works correctly for small graphs
Still only starts from node 0 (limitation)'''