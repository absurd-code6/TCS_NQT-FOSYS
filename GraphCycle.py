#Given a directed graph, write a program to check if there is a cycle in 
#the #graph. If there is a cycle in the graph print 1, otherwise print 0. 

from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isCyclicUtil(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True
        for nbr in self.graph[v]:
            if visited[nbr]==False:
                if self.isCyclicUtil(nbr,visited,recstack)==True:
                    '''Step-by-step Example
                    Graph:
0 → 1 → 2 → 3
      ↑     ↓
      └─────┘

Cycle: 1 → 2 → 3 → 1

Execution Flow
1. Start at node 0
isCyclicUtil(0)
2. Go to 1
isCyclicUtil(1)
3. Go to 2
isCyclicUtil(2)
4. Go to 3
isCyclicUtil(3)
🚨 At node 3:
Neighbor = 1
1 is already in recStack

So this triggers:

return True
🔁 Now comes the important part
Backtracking (returning up):
In isCyclicUtil(2):
if self.isCyclicUtil(3, ...) == True:
    return True

👉 Receives True → returns True

In isCyclicUtil(1):
if self.isCyclicUtil(2, ...) == True:
    return True

👉 Receives True → returns True

In isCyclicUtil(0):
if self.isCyclicUtil(1, ...) == True:
    return True

👉 Receives True → returns True

📦 Final Result

The True value travels all the way back to:

g.isCyclic()

So the program concludes:

Cycle exists
⚡ Why this line is necessary

Without this line:

You might detect a cycle deep inside
But the information wouldn’t reach the top

👉 This line ensures:

“If any recursive call finds a cycle, stop everything and report it immediately.”'''
                    return True
            elif recstack[nbr]==True:
                return True
        recstack[v]=False
        return False
    def isCyclic(self):
        visited=[False]*self.V
        recstack=[False]*self.V
        for node in range(self.V):
            if visited[node]==False:
                if self.isCyclicUtil(node,visited,recstack)==True:
                    return True
        return False

temp = input().split()
V = int(temp[0])
E = int(temp[1])
g = Graph(V)
temp = input().split()
for i in range(E):
  u = int(temp[2*i])
  v = int(temp[2*i+1])
  g.addEdge(u,v)

if g.isCyclic() == 1: 
	print (1)
else: 
	print (0)

'''Input:
4 4
0 1 1 2 2 3 3 1
Meaning:

Edges are:

0 → 1
1 → 2
2 → 3
3 → 1   ← cycle here
Output:
1
Graph WITHOUT cycle)
Input:
4 3
0 1 1 2 2 3
Meaning:
0 → 1 → 2 → 3

No cycle.

Output:
0'''

'''#include <iostream>
#include <vector>
using namespace std;

class Graph {
    int V;
    vector<vector<int>> graph;

public:
    Graph(int V) {
        this->V = V;
        graph.resize(V);
    }

    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    bool isCyclicUtil(int v, vector<bool>& visited, vector<bool>& recStack) {
        visited[v] = true;
        recStack[v] = true;

        for (int neighbour : graph[v]) {
            if (!visited[neighbour]) {
                if (isCyclicUtil(neighbour, visited, recStack))
                    return true;
            }
            else if (recStack[neighbour]) {
                return true;
            }
        }

        recStack[v] = false;
        return false;
    }

    bool isCyclic() {
        vector<bool> visited(V, false);
        vector<bool> recStack(V, false);

        for (int node = 0; node < V; node++) {
            if (!visited[node]) {
                if (isCyclicUtil(node, visited, recStack))
                    return true;
            }
        }
        return false;
    }
};

int main() {
    int V, E;
    cin >> V >> E;

    Graph g(V);

    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
    }

    if (g.isCyclic())
        cout << 1;
    else
        cout << 0;

    return 0;
}'''
