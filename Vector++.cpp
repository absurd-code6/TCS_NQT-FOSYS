#include<bits/stdc++.h>
#include<math.h>
using namespace std;

void printInfo(vector<int> &vr){
for(int i=0;i<vr.size();i++){
cout<<vr[i]<<" ";
}
cout<<endl;
}

bool comparator(pair<int,int>p1,pair<int,int>p2)
{
return p1<p2;
}

int main()
{
/*Vector is a dynamic array.We can keep inserting elements in
the array & it will manage it's size.*/
vector<int>vr;
int element,size;
cout<<"Enter the size of the vector:"<<endl;
cin>>size;
for(int i=0;i<size;i++){
cout<<"Enter element at position "<<i<<endl;
cin>>element;
vr.push_back(element);
}
printInfo(vr);
vector<int> :: iterator itr = vr.begin();
vr.insert(itr,666);

// vr.insert(itr+1,666);

vr.insert(itr+1,250,666);// 250 copies of 666 will be printed
vr.pop_back();
printInfo(vr);

//Pairs
/*This is the coordinate compression / ranking technique.

Given:

arr = {10,16,7,14,5,3,12,9}

Sorted order:

3 5 7 9 10 12 14 16

The program replaces each element with its rank in the sorted array.

Output:

4 7 2 6 1 0 5 3*/
pair <int,char>pr;
pr.first=115;
pr.second='R';
int arr[]={10,16,7,14,5,3,12,9};
vector<pair<int,int>>v;
for(int i=0;i<(sizeof(arr)/sizeof(arr[0]));i++){
/*sizeof(arr) / sizeof(arr[0])

This calculates the number of elements in the array.

sizeof(arr) → total size of the array in bytes

sizeof(arr[0]) → size of one element

Example:

arr = {10,16,7,14,5,3,12,9}

sizeof(arr) = 8 * 4 = 32 bytes (assuming int = 4)

sizeof(arr[0]) = 4

So:

32 / 4 = 8

➡️ The loop runs 8 times (once for each element).*/
v.push_back(make_pair(arr[i],i));
}
/*This adds the pair to the vector v.

After the loop finishes:
v = {(10,0), (16,1), (7,2), (14,3), (5,4), (3,5), 
(12,6), (9,7)}
4️⃣ Why store the index?

Because later you sort the vector. Sorting changes the order, but the original index is preserved.

Example after sorting:

(3,5)
(5,4)
(7,2)
(9,7)
(10,0)
(12,6)
(14,3)
(16,1)

Now you still know where each value originally came from.*/
sort(v.begin(),v.end(),comparator);
for(int j=0;j<v.size();j++){
arr[v[j].second]=j;
}
/*This is the main step that replaces each element in the 
original array with its rank after sorting
j is the position in the sorted array, which represents the rank.

j = 0 → smallest number
j = 1 → 2nd smallest
j = 2 → 3rd smallest
...
3️⃣ What v[j].second means

v[j].second = original index of that element in arr

Example:

v[0] = (3,5)

value = 3

original index = 5
What this line does:go to the original position of the element
and store its sorted rank
5️⃣ Step-by-step example
j	v[j]	operation	result in arr
0	(3,5)	arr[5]=0	smallest element
1	(5,4)	arr[4]=1	
2	(7,2)	arr[2]=2	
3	(9,7)	arr[7]=3	
4	(10,0)	arr[0]=4	
5	(12,6)	arr[6]=5	
6	(14,3)	arr[3]=6	
7	(16,1)	arr[1]=7	

Final array becomes:

arr = {4,7,2,6,1,0,5,3}
This loop:

takes the sorted order

goes back to the original positions

stores the rank of each number*/
for(int i=0;i<v.size();i++){
cout<<arr[i]<<" ";
}
cout<<endl;
return 0;
}
//https://cplusplus.com/reference/vector/vector/?kw=vector