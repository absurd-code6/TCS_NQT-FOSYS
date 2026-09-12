/**/
#include<bits/stdc++.h>
#include<math.h>
#include<string>
using namespace std;
vector<pair<int,int>>adj[1000];//Global Data Structure used in funcn to store
/*Nodes with thier wts.1st int is for node 2nd int is for wt*/


vector<int>dijkstra(int n,int src,vector<int>& parent
/*,vector<pair<int,int>> adj[]*/){
/*&parent means address of parent.So it isn't a copy & all the changes are
made in the original parent*/
vector<int>dist(n+1,INT_MAX);
dist[src]=0;//initializing dist frm src to source=0,in tis quesn source is 1
priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;

/*In Priority Queue we store in the reverse format i.e. {wt,node/vertice}*/

pq.push({0,src});
while(!pq.empty()){
int d = pq.top().first;//distance
//& its corresponding node
int u= pq.top().second;
pq.pop();
if(d>dist[u])
continue;
for(auto edge:adj[u]){
int v=edge.first;
int wt=edge.second;
if(dist[u]+wt<dist[v]){
dist[v]=dist[u]+wt;
parent[v]=u;
pq.push({dist[v],v});
}
}
}
return dist;
}

void print_path(const vector<int>& parent,int dest){
if(parent[dest]==-1){
cout<<dest;
return;
}
print_path(parent,parent[dest]);
cout<<"-->"<<dest;
}
int main(){
int n,m; // n vertices & m edges
cout<<"Enter the number of vertices: ";
cin>>n;
cout<<"\n Enter the number of edges: ";
cin>>m;

string s="vector<int>adj[n+1];";
/*An array of vector type,of integers  starting frm 0 to n thus of size n+1,rep+nts 
the adjacency list.*/

string str="vector<pair<int,int>> adj[n+1]"; // adjacency list with weight
//(By pair DS).It's a {node, weight} pair


for(int i=0;i<m;i++){
int u,v,w;
cin>>u>>v>>w;
// adj[u].push_back(v);
// adj[v].push_back(u);
adj[u].push_back({v,w}); //Pair Data Structure
adj[v].push_back({u,w});
}
int src,dest;//source & destination
cout<<"Enter source and destination: ";
cin>>src>>dest;
vector<int>parent(n+1,-1);/*Indexing always starts frm 0 but here its starting 
from 1 so we take a size of n+1 & 0th idx  always has value 
infinity(=INT_MAX) & is ignored,-1 is the initialized value @ every idx of
the array at the starting*/
vector<int>dist=dijkstra(n,src,parent/*,adj*/);
cout<<"Shortest path from source "<<src<<"to destination "<<dest<<"is ";
print_path(parent,dest);
cout<<"\n";
cout<<"Total distance is "<<dist[dest]<<endl;
return 0;
}