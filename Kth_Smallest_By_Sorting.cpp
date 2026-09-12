
#include<bits/stdc++.h>
using namespace std;
int Kth_Smallest(vector<int>& arr,int k){
sort(arr.begin(),arr.end());
return arr[k-1];
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
int k;
cout<<"Enter the value of k :"<<endl;
cin>>k;
cout<<"The"<<k<<"th smallest element is "<<Kth_Smallest(arr,k)<<endl;
return 0;
}