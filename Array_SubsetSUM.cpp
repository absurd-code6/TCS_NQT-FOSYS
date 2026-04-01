#include<bits/stdc++.h>
#include<math.h>
using namespace std;

bool subset_sum(vector<int>& arr,int h,int tempsum,int idx){
if(h==tempsum)
return true;

if(idx>=arr.size())
return false;

bool c1=subset_sum(arr,h,tempsum+arr[tempsum],idx+1);
bool c2=subset_sum(arr,h,tempsum,idx+1);

return c1 || c2;// T or F is returned
}

int main()
{
//Quesn_4_Arr_SubsetSUM.png
int n,h/*target*/;
cout<<"Enter the size of array:";
cin>>n;
vector<int>arr(n);
cout<<"\nEnter the elements:"<<endl;
for(int i=0;i<n;i++){
cin>>arr[i];
}
cout<<"Enter the target sum:"<<endl;
cin>>h;
//Input array:3 5 7 2
if(subset_sum(arr,h,0,0))
cout<<"Yes"<<endl;

else cout<<"No"<<endl;
/*Difference b/w subsequence & subsets of an array:
subseq follows order i.e. 3,5 3,7 are valid subseqces but 7,3 & 2,5 are not
2 (Single element) & {} (empty set) are also subsequences
subsets do not follow such order

NOTE: There are 3 ways to find subseqces of an array:
1) Power Set (workd on bits)
2) Recursion -----> Here we'll use recursion tree approach
3) Dynamic Programming (DP)*/

return 0;
}
/*In JAVA
public static boolean subset_sum(int[] arr,int n,int target){
if(n==0) return false;

if(arr[n-1]>target){
return subset_sum(arr,n-1,target);
}
return subset_sum(arr,n-1,target) || subset_sum(arr,n-1,target-arr[n-1]);
}*/