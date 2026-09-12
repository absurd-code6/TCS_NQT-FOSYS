#include<bits/stdc++.h>
#include<math.h>
using namespace std;
/*Implementing Dijkstra's Algorithm using Priority Queue*/
//TC= O(ElogV)
vector <int> dijkstra(int V,vector<vector<int>>adj[],int src){
/*vector<vector<int>>adj[]: This works, but is not very clean or safe.

✅ Better Approach:

Use pair<int,int>:

vector<pair<int,int>> adj[]*/
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
//creating a PQ
vector<int>dist(V);//creating a distance vector of size = no of vertices
for(int i=0;i<V;i++){
dist[i]=INT_MAX; // initializing every element to infinity
}
dist[src]=0;
pq.push({0,src});
while(!pq.empty()){
int wt=pq.top().first;//fetching the top element in PQ using top()
int node = pq.top().second;
pq.pop();
for(auto i:adj[node]){//iterating through the adjList of given node to find nbrs
/*auto i is not an int but a vector storing 2 elements*/
int adj_path_cost=i[1];//bcoz indexing starts from 0 & its in 2nd posn
int adjNode=i[0];//bcoz it's in 1st posn
if(wt+adj_path_cost<dist[adjNode]){
dist[adjNode]=wt+adj_path_cost;
pq.push({dist[adjNode],adjNode});
}
}
}
return dist;
}

int main()
{
/*We'll be using a min-heap here ---> the node with the shortest path cost 
will be @ the top & in case of conflict the earlier node will be preferred*/

/*We'll always have a distance array to keep a track of how much distance we're
taking in a path */

/*We'll be using an adjacency list to tell us what are the 
neighbouring nodes we can visit from our current node 

This loop does NOT choose the minimum node. The priority queue does.
👉 This loop is only responsible for relaxing edges (updating distances of neighbors).

Let’s break it down clearly with an example.

🔍 What This Code Actually Does
for(auto i: adj[node]) {
    int adjNode = i[0];
    int adj_path_cost = i[1];

    if (wt + adj_path_cost < dist[adjNode]) {
        dist[adjNode] = wt + adj_path_cost;
        pq.push({dist[adjNode], adjNode});
    }
}
💡 Meaning:
You are currently at node with distance wt
You check all its neighbors
You try to see:
👉 “Can I reach this neighbor cheaper through this node?”

This is called edge relaxation.

🧠 Important Insight

✔ The priority queue ensures minimum distance node is picked
✔ The loop only updates neighbors

📊 Example Graph

Consider this graph:

        (2)
   0 --------> 1
   |           |
 (4)|           |(1)
   v           v
   2 --------> 3
        (3)
Adjacency List:
0 → {(1,2), (2,4)}
1 → {(3,1)}
2 → {(3,3)}
3 → {}
🚀 Step-by-Step Execution
Step 1: Start at source 0
dist = [0, ∞, ∞, ∞]
pq = {(0,0)}
Step 2: Pop (0,0)

Now:

node = 0, wt = 0
Loop runs:

Neighbor 1:

new distance = 0 + 2 = 2 < ∞ → update
dist[1] = 2
push (2,1)

Neighbor 2:

new distance = 0 + 4 = 4 < ∞ → update
dist[2] = 4
push (4,2)

Now:

dist = [0, 2, 4, ∞]
pq = {(2,1), (4,2)}*/
return 0;
}
/*In Python:
# Dijkstra's algorithm to find the shortest path from the source node to all other nodes

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    # graph is represented as an adjacency list, where graph[u] is a list of (neighbor, weight) pairs
    # source is the starting node
    
    # Initialize distance dictionary where all distances are set to infinity initially
    dist = {node: float('inf') for node in graph}
    dist[source] = 0  # The distance to the source node is 0
    
    # Priority queue to keep track of the node with the smallest distance, initialized with the source node
    pq = []
    pq.append((0, source))  # (distance, node)
    
    while pq:
        # Step 2: Get the node with the smallest distance from the 
        priority queue
        current_distance, current_node = pop_min(pq)
        
        # If the current distance is greater than the recorded distance, 
        skip processing this node
        if current_distance > dist[current_node]:
            continue
        
        # Step 3: Iterate over each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate the tentative distance through the current node
            distance = current_distance + weight
            
            # Step 4: If a shorter path to the neighbor is found, update 
            the distance and add it to the priority queue
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                pq.append((distance, neighbor))
    
    # Return the shortest distances from the source to all nodes
    return dist

# Helper function to pop the node with the smallest distance
def pop_min(pq):
    # In a real implementation, we would use a priority queue, 
    but for simplicity, we assume we pop the smallest element here
    pq.sort()  # Sort the queue by distance (ascending)
    return pq.pop(0)  # Pop the first element (smallest distance)*/
