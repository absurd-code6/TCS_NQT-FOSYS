/*This program first accepts an array. Assume there 
are 4 elements in an array. It takes 2 element as a 
first element in an array and so on till the last element of the given array. 
Now here first element of an array becomes last element in an array during cyclical permutation.
 i.e. the content of A1 become that of A2. And A2 contains
that of A3 & so on as An contains A1*/
#include<iostream>
#include<math.h>
#include<string>
using namespace std;

int main(){
int n;
cout<<"Enter size of array:"<<endl;
cin>>n;
/*1. Create a one-dimentional array of some fixed size (lets say n), defining 
all its elements.*/
int arr[n];
cout<<"Enter the numbers:"<<endl;
for(int i=0;i<n;i++)
cin>>arr[i];

arr[n]=arr[0];//Reserve the first element of the array by 
//assigning its value to the nth position of the array.
for(int i=0;i<n;i++){
arr[i]=arr[i+1];
}
cout<<"The array after cyclic permutation is: ";
for(int i=0;i<n;i++)
cout<<arr[i]<<"";
return 0;
}