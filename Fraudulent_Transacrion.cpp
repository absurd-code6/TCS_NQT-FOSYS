//The question asks for the implementation of Hash Maps

#include<bits/stdc++.h>
using namespace std;


int main()
{
int n;
cout<<"Enter no of transactions:"<<endl;
cin>>n;
vector<string>sender(n),receiver(n);
vector<long long> timestamp(n);
vector<double>amt(n);

for(int i=0;i<n;i++){
cout<<"Transaction "<<i+1<<"(sender receiver timestamp amt): ";
cin>>sender[i]>>receiver[i]>>timestamp[i]>>amt[i];
}
unordered_map<string,int>seen;//Duplicate_Check by unordered_map(HashMap)
for(int i=0;i<n;i++){
string key = sender[i] + "|" + receiver[i];
if(seen.count(key)){
cout<<"Error: Fradulent Transaction"<<endl;
return 0;
}
seen[key] = i;
}
for(int i=1;i<n;i++){//Fraud Detection
long long diff= abs(timestamp[i]-timestamp[i-1]);
if(diff>60){
cout<<"Fraud Detected!"<<endl;
return 0;
}
}
cout<<"All Transactions are Valid"<<endl;
return 0;
}
