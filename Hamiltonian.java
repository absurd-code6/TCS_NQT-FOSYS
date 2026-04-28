/*A Hamiltonian path is a path in an undirected or directed graph 
that visits each vertex exactly once. Given an undirected graph, 
the task is to check if a Hamiltonian path is present in it or not. 
If a hamiltonian path is present in the graph, then print 1 
otherwise print 0 */

import java.util.*;

public class Hamiltonian{
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt(); // number of nodes
int e = sc.nextInt(); // number of edges
freq=new int[n];
List<List<Integer>> graph = new ArrayList<>();
for(int i=0;i<n;i++){
graph.add(new ArrayList<>());
}
        // read edges
        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            a--; // convert to 0-based
            b--;

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        // start from node 0
        freq[0] = 1;
        ham(graph, 0, n);

        System.out.println(pointer);

}
static int pointer = 0;   // 1 if Hamiltonian path exists
static int[] freq;     // or visited[]

public static void ham(List<List<Integer>>graph,int s,int n){
boolean allvisited=true;
for(int i=0;i<n;i++){
if(freq[i]==0){
allvisited=false;
break;
}
}
if(allvisited){
pointer=1;
return;
}
for (int nbr :graph.get(s)){
if(freq[nbr]==0){
freq[nbr]=1;
ham(graph,nbr,n);
freq[nbr]=0;
}
}
}
}


/*The code
List<List<Integer>> graph = new ArrayList<>();

for (int i = 0; i < n; i++) {
    graph.add(new ArrayList<>());
}
🧠 What is this creating?

This builds an adjacency list for a graph.

👉 Think of it as:

“For every node, create a list to store its neighbors.”

🧪 Example: n = 3

We have 3 nodes:

0, 1, 2
Step 1:
List<List<Integer>> graph = new ArrayList<>();

Now:

graph = []

👉 Empty list (no nodes yet)

Step 2: Loop runs n = 3 times
Iteration 1 (i = 0)
graph.add(new ArrayList<>());

Now:

graph = [ [] ]

👉 Node 0 has an empty neighbor list

Iteration 2 (i = 1)
graph.add(new ArrayList<>());

Now:

graph = [ [], [] ]

👉 Node 1 added

Iteration 3 (i = 2)
graph.add(new ArrayList<>());

Now:

graph = [ [], [], [] ]

👉 Node 2 added

📌 Final structure
Index:   0     1     2
graph = [[],  [],  []]

👉 Each index = a node
👉 Each inner list = its neighbors (currently empty)

🔗 Now let’s add edges

Suppose input edges:

1 2
2 3

After converting to 0-based:

0–1
1–2
Add edge (0,1)
graph.get(0).add(1);
graph.get(1).add(0);

Now:

graph = [ [1], [0], [] ]
Add edge (1,2)
graph.get(1).add(2);
graph.get(2).add(1);

Now:

graph = [ [1], [0,2], [1] ]
🎯 What this means
graph.get(0) → neighbors of node 0 → [1]
graph.get(1) → neighbors of node 1 → [0,2]
graph.get(2) → neighbors of node 2 → [1]
⚡ Simple analogy

Think of:

graph.add(new ArrayList<>());

as:

“Create an empty notebook page for this node to write its connections later.”

🚨 Why not just do this?
List<List<Integer>> graph = new ArrayList<>(n);

👉 That only sets capacity, not actual elements
👉 You still need the loop to add lists */


/*Open Command Prompt as Administrator
Press Win + S, type cmd, right-click Command Prompt, select Run as administrator.

Start Diskpart

diskpart

You’ll see DISKPART> prompt.

List all drives

list disk
Identify your USB drive by size. Be very careful, choosing the wrong 
disk can erase your hard drive.
Example: if your USB is 32 GB, it might show as Disk 2.

Select your USB drive

select disk 2

Replace 2 with the number of your USB.

Clean the drive

clean
This deletes all partitions and Tails OS from the USB.

Create a new partition

create partition primary

Format the USB (FAT32)

format fs=fat32 quick

Assign a drive letter

assign

Exit Diskpart

exit */