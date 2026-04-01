/*Priority Queue Concepts & Implementation*/
#include<bits/stdc++.h>
#include<math.h>
using namespace std;


int main()
{
/*There are 2 kinds of Priority Queue Implementation:
1.Max Heap
2.Min Heap 
The 5 funcns of PQ are:
push(),pop(),top(),empty(),size()*/
priority_queue<int>pq;//Declaration(Max Heap By Default)
pq.push(1);//Current Instance: 1
pq.push(2);//2,1
pq.push(3);//3,2,1
pq.push(5);//5,3,2,1
cout<<pq.size()<<endl;//4
while(!pq.empty()){//Iterating thrh PQ
int val=pq.top();
cout<<val<<"";
//O/p is 55555555555555555555555........float('inf')(Since PQ is never empty)
pq.pop();//So we pop each element after displaying it.O/p : 5321
}
cout<<endl;
priority_queue<int,vector<int>,greater<int>>pq1;//Min Heap Implementation
//Note That we're storing single elements i.e. we aren't using pair
pq1.push(1);//Current Instance: 1
pq1.push(2);//1,2
pq1.push(3);//1,2,3
pq1.push(5);//1,2,3,5
while(!pq1.empty()){
int val1=pq1.top();
cout<<val1<<"";
pq1.pop();
}
/*🔍 What This part means in Dijkstra:
greater<pair<int,int>>

👉 Tells C++:

“Give me the smallest element first”

So now:

pq.top()

returns the pair with the smallest distance

📦 Example

If PQ contains:

(4,2), (2,1), (3,3)
With greater (min-heap):
pq.top() → (2,1) ✅
Without greater (default max-heap):
pq.top() → (4,2) ❌*/
return 0;
}