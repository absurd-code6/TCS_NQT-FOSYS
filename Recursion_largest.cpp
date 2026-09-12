#include<bits/stdc++.h>
using namespace std;

int find_largest_rec(int arr[],int size){
if(size==1) //Base Case
return arr[0];
return max(arr[size-1],find_largest_rec(arr,size-1));
}

int main()
{
int n;
cout<<"Enter the size of the array:"<<endl;
cin>>n;
int arr[n];
cout<<"Enter "<<n<<" elements:"<<endl;
for(int i=0;i<n;i++){
cout<<"Enter element "<<i<<":";
cin>>arr[i];
}
cout<<"Largest Element found by recursion is\t"<<find_largest_rec(arr,n)<<endl;
return 0;
}