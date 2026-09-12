/*Alice challenged Bob to write the same word as his on a typewriter. 
Both are kids and are making some mistakes in typing and are making 
use of the ‘#’ key on a typewriter to delete the last character printed on it. 
An empty text remains empty even after backspaces*/
#include<bits/stdc++.h>
#include<string>
using namespace std;

string string_processed(string s){
stack<char>word;
for(char ch :s){
if(ch=='#'){
if(!word.empty()){
word.pop();
}
}
else word.push(ch);
}
//Building the final string from the stack
string final_str="";
while(!word.empty()){
final_str=word.top() + final_str;
word.pop();
}
return final_str;
}

int main()
{
string bob,alice;
cout<<"Bob's string"<<endl;
getline(cin , bob);
string alice;
cout<<"Alice's string"<<endl;
getline(cin,alice);
string pros_bob=string_processed(bob);
string pros_alice=string_processed(alice);
if(pros_bob==pros_alice)
cout<<"YES"<<endl;
else cout<<"NO"<<endl;
return 0;
}