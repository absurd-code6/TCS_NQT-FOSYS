//Complex No program using Operator Overloading.
/*In CPP there are some operators which cannot be overloaded:
The operators :: (scope resolution), . (member access), . * (member access through pointer to member), and ?: (ternary conditional) 
cannot be overloaded. New operators such as ** , <> , 
or &| cannot be created.*/
#include<bits/stdc++.h>
using namespace std;

class Complex{
private: int real,img;
public:
Complex(int r=0,int i=0){
real=r;
img=i;
}
Complex operator +(Complex const& obj){
Complex res;
res.real=real + obj.real;
res.img=img + obj.img;
return res;
}
void print(){
cout<<real<<" + "<<img<<"i"<<endl;
}
};

int main()
{
Complex c1(6,2);
Complex c2(5,3);
Complex c=c1 + c2;
c.print();
return 0;
}