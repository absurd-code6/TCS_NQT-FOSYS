/*Constructing Directed and Undirected Graphs in Java*/

import java.util.*;

class Graph{
int V;//Vertices
ArrayList<ArrayList<Integer>>adj_list;

public Graph(int V){
this.V=V;
adj_list = new ArrayList<>();
for (int i = 0; i < V; i++) {
    adj_list.add(new ArrayList<>());
}
}
void add_edge(int u,int v){
adj_list.get(u).add(v); //1 direction edge for Directed Graph
adj_list.get(v).add(u); //Reverse direction edge for Undirected Graph
}
void display(){
for(int i=0;i<V;i++){
System.out.println(i + "-> "+ adj_list.get(i));
}
}
}

public class Graphs_IN_JAVA {
public static void main(String[] args) {
Graph g = new Graph(4);
g.add_edge(0,1);
g.add_edge(1,2);
g.add_edge(2,3);
g.display();

// By User Input
Scanner sc=new Scanner(System.in);
System.out.println("Enter the number of vertices:");
int v=sc.nextInt();
Graph graph = new Graph(v);
System.out.println("Enter the number of edges:");
int E=sc.nextInt();
for(int i=0;i<E;i++){
    int a = sc.nextInt();
    int b = sc.nextInt();
    graph.add_edge(a,b);

}
graph.display();
}
}
