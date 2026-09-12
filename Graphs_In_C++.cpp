//Creating Directed & Undirected Graphs in C++
#include<bits/stdc++.h>
using namespace std;

class Graph{
vector<vector<int>>adj_list;
int V;
public: Graph(int V){
this->V=V;
adj_list.resize(V);
}
void add_edge(int u,int v){
adj_list[u].push_back(v);
adj_list[v].push_back(u);
}
void display(){
for(int i=0;i<V;i++){
cout<<i<<"->";
for(int v: adj_list[i]){
cout<<v<<" ";
}
cout<<endl;
}
}
};

int main(){
int V;
cout<<"Enter the no of vertices:"<<endl;
cin>>V;
Graph g(V);
int E;
cout<<"Enter the no of edges:"<<endl;
cin>>E;
for(int i=0;i<E;i++){
int u,v;
cin>>u>>v;
g.add_edge(u,v);
}
g.display();
return 0;
}