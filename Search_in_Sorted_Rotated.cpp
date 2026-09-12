/*Given a sorted and rotated array arr[] of distinct elements, find the index of given key in the array. If the key is not present in the array, return -1.

Examples:  

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is present at index 8.

Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: 6 is not present.

Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1*/
#include<bits/stdc++.h>
using namespace std;

int search(vector<int>& arr,int key){
for(int i=0;i<arr.size();i++){
if(arr[i]==key)
return i;
}
return -1;
}

int main()
{
int n;
cout<<"Enter the size of array:"<<endl;
cin>>n;
vector<int>arr(n);
cout<<"Enter "<<n<<" elements"<<endl;
for(int i=0;i<n;i++)
{
cin>>arr[i];
}
int key;
cout<<"Enter the element u would like to search :"<<endl;
cin>>key;
cout<<"The element is found @ index "<<search(arr,key)<<endl;
return 0;
}
