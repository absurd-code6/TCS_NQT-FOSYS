import java.util.*;

public class Dupli_Str{
public static String duplicate_remover(String s){
if(s.isEmpty())
    return "";

StringBuilder result =  new StringBuilder();
/*🧠 What is StringBuilder?

👉 StringBuilder is a class in Java used to create and modify strings efficiently.

Unlike normal strings, it lets you change the content without creating a 
new object every time.

🔑 Why not just use String?

In Java:

String s = "Hello";
s = s + " World";

👉 This does NOT modify the original string
👉 It creates a new string object every time

❗ Problem:
Slow if done repeatedly (like in loops)
Wastes memory
✅ Enter StringBuilder
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");

👉 This modifies the same object
👉 No unnecessary new objects

⚡ Simple Example
StringBuilder sb = new StringBuilder();

sb.append("H");
sb.append("i");

System.out.println(sb);  // Hi */

result.append(s.charAt(0));
for(int i=1;i<s.length();i++){
if(s.charAt(i) != s.charAt(i-1)){
result.append(s.charAt(i));
}
}
return result.toString();
}
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter your string:");
String str=sc.next();
System.out.println("\nString after removing duplicate characters:"+ 
duplicate_remover(str));
sc.close();
}
}


/*IN C++
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
diplicate_remover(string s){
if(s.empty())
return "";

string result;
result+=s[0];
for(size_t i=0;i<s.length();i++){
if(s[i] != s[i-1])
result+=s[i];
}
return result;
}

int main(){
string str;
cout<<"Enter your string:"<<endl;
cin>>str;
cout<<"String after removal of consecutive duplicate characters: "
<<duplicate_remover(str)<<endl;
return 0;
}*/