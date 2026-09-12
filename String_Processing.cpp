/*Write a program that processes a given 
string to determine:
The 1st non-repeating character(if +nt)

The most repeated character in the string

If multiple characters hv the same highest freq, 
print the 1st non-repeating character 1st,then 
the repeating character.

If the input string is empty,print 'Invalid input'

If all characters in the string are repeating,
print "None" followed by the 1st 
repeating character

Eg. of input string: Swiss mississippi

Note: In quesns where u hv to determine frequency, use map DS*/

#include<bits/stdc++.h>
#include<string>
using namespace std;

void findchar(const string &s){
if(s.empty()){
cout<<"Invalid String!"<<endl;
return;
}
unordered_map<char,int>freq;
unordered_map<char,int>idx;

for(int i=0;i<s.length();i++){
freq[s[i]]++;
if(idx.find(s[i])==idx.end())
idx[s[i]]=i;
}
// finding non-repeating char
char first_non_reptg='\0';
bool has_non_repeted=false;
for(int i=0;i<s.length();i++){
char c=s[i];
if(freq[c]==1){
first_non_reptg=c;
has_non_repeted=true;
break;
}
}
//findg most repeated character
char most_reptg='\0';
int max_freq=0;
for(auto &pair:freq){
if(pair.second > max_freq)
max_freq=pair.second;
}
int prev_idx=s.length();

for(auto &it:freq){
char c=it.first;
int f=it.second;
if(f==max_freq){
int ind=idx[c];
if(ind<prev_idx){
prev_idx=ind;
most_reptg=c;
}
}
}
//findg the 1st repeating char
char first_reptg='\0';
bool has_repeted=false;
for(int i=0;i<s.length();i++){
char c=s[i];
if(freq[c]>1){
first_reptg=c;
has_repeted=true;
break;
}
}
if(!has_non_repeted){
cout<<"None";
if(has_repeted)
cout<<""<<first_reptg;
cout<<endl;
}
else{
cout<<first_non_reptg<<endl;
cout<<most_reptg<<endl;
}
}

int main(){
string s;
cout<<"Enter a string: ";
cin>>s;

/*In the cin >> s part, it's only reading a single word (because cin stops 
at whitespace), which may not be the desired behavior if the string contains 
spaces. You should use getline(cin, s) to allow spaces.*/

// getline(cin,s);

findchar(s);
return 0;
}
