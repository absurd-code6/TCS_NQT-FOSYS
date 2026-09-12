/*Dijkstra Algorithm using Sets(Faster Method)*/
#include<bits/stdc++.h>
#include<math.h>
using namespace std;

vector<int>dijkstraSet(int V,vector<vector<int>>adj[],int src){
set<pair<int,int>>st;
vector<int>dist(V,INT_MAX/*OR 1e9*/);
dist[src]=0;
st.insert(0,src);
while(!st.empty()){
auto it=*(st.begin());
int node=it.second;
int path_cost=it.first;
st.erase(it);
for(auto it:adj[node]){
int adjnode=it[0];
int edge_node=it[1];
if(path_cost + edge_node < dist[adjnode]){
    if(dist[adjnode]!=INT_MAX){
st.erase({dist[adjnode],adjnode});//erase if it already existed
dist[adjnode]=path_cost + edge_node;
st.insert(adjnode,dist[adjnode]);
}
}
}
return dist;
}
}

int main(){
//Set stores unique values & the smallest @ the top
//Set DS erases already existing paths from the min-heap
return 0;
}
