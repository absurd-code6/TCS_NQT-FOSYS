/*Find the sum of  First N Prime Numbers*/
#include<bits/stdc++.h>
#include<math.h>
#include<string>
using namespace std;
bool prime(int N){
for(int i=2;i<=sqrt(N);i++){
if(N%i==0)
return false;
}
return true;
}

int main(){
int num,sum=0,count=0;
/*int sum=0,count=0;
string s ="num";
int num=stoi(s);*/
cout<<"Enter a prime number:";
cin>>num;
for(int i=2;count<num;i++){
if(prime(i))
sum+=i;
count++;
}
/*U can also use this loop:
for(int i=2;i<=num;i++){
above given condition
}*/
//else cout<<"\n Not a prime number!"<<endl;
cout<<"Sum is: "<<sum;
return 0;
}