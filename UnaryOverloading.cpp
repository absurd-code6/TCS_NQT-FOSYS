//Write a program to increment and decrement using unary increment (++) and decrement (--) 
//operator overloading.
#include<bits/stdc++.h>
using namespace std;

class Overload{
private:
int n;
public:
void getNum(int x){
n=x;
}
void operator ++(void){
n++;
}
void operator --(void){
n--;
}
void display(void){
cout<<"Value of n is: "<<n<<endl;
}
};

int main(){
int n;
cout<<"Enter a number: "<<endl;
cin>>n;
Overload num;
num.getNum(n);
++num;
cout<<"After increment :"<<endl;
num.display();
--num;
cout<<"After decrement :"<<endl;
num.display();
return 0;
}