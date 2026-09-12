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

/*Class Definition
class Complex{

This defines a class named Complex to represent complex numbers like:

a+bi
🔹 4. Data Members
private:
int real, img;
real → stores the real part
img → stores the imaginary part

Example:

3 + 4i → real = 3, img = 4
🔹 5. Constructor
Complex(int r=0,int i=0){
    real=r;
    img=i;
}
What it does:
Initializes object values
Has default arguments
Meaning:
If no values are passed → 0 + 0i
If values are passed → assign them
Example:
Complex c1(3,4);  // real=3, img=4
Complex c2;       // real=0, img=0
🔹 6. Operator Overloading
Complex operator +(Complex const& obj)
What is happening here?

You are overloading the + operator for objects of class Complex.

📌 Syntax Breakdown
Complex → return type
operator + → operator being overloaded
(Complex const& obj) → parameter (another object)

👉 const& means:

Pass by reference (no copying → efficient)
const ensures it won’t be modified
What is const and obj and what are their purpose?
Let’s break Complex const& obj into its three parts:

🔹 1. What is obj?
obj
It’s just a parameter name (a variable)
It represents the second complex number being added
Example:
Complex c1(2,3);
Complex c2(4,5);

c1 + c2;

👉 Inside the function:

c1 → current object (this)
obj → c2

So:

obj = c2 (4 + 5i)
🔹 2. What is & (reference)?
Complex const& obj

The & means pass by reference.

Without &:
Complex obj
A copy of the object is made
Extra memory + slower
With &:
Complex& obj
No copy is made
Works directly with the original object

👉 More efficient, especially for large objects

🔹 3. What is const?
Complex const& obj

const means:
👉 “Do NOT modify this object inside the function”

Why is const needed?

Inside operator+, we only read values, not change them.

res.real = real + obj.real;
res.img  = img  + obj.img;

We never do:

obj.real = something;  // ❌ not allowed

So marking it const:

Prevents accidental modification
Makes code safer
🔹 Putting it all together
Complex const& obj

Means:

👉 “A reference to a Complex object that cannot be modified”

🔹 Full Meaning in Simple Words
Complex operator +(Complex const& obj)

👉 “This function takes another Complex object by reference (without copying), does not modify it, and uses it to perform addition.”

🔹 Dry Run with This Concept
Complex c1(2,3);
Complex c2(4,5);

Complex c3 = c1 + c2;
Internally:
c1.operator+(c2);

So:

this → c1 (2 + 3i)
obj  → c2 (4 + 5i)
🔹 Why all three are important?
Part	Purpose
obj	Holds the second operand
&	Avoids copying (efficient)
const	Prevents modification (safe)
🔹 What happens if we remove them?
❌ Without &
Complex obj
Makes unnecessary copy → slower
❌ Without const
Complex& obj
You could accidentally modify obj
Bad practice for operator like +

Function Body
Complex res;
res.real = real + obj.real;
res.img  = img  + obj.img;
return res;
What happens:
Create a new object res
Add corresponding parts:
real + real
imaginary + imaginary
Return the result
🔹 7. Print Function
void print(){
    cout<<real<<" + "<<img<<"i"<<endl;
}
Purpose:

Displays the complex number in standard form.

🔹 8. How the Code Works (Conceptually)

If you write:

Complex c1(2,3);
Complex c2(4,5);
Complex c3 = c1 + c2;

👉 This actually becomes:

Complex c3 = c1.operator+(c2);
🔹 9. Dry Run Example
Input:
Complex c1(2,3);
Complex c2(4,5);
Complex c3 = c1 + c2;
c3.print();
Step-by-Step Execution
Step 1: Object Creation
c1 → real=2, img=3
c2 → real=4, img=5
Step 2: Operator Call
c1 + c2

Calls:

c1.operator+(c2)
Step 3: Inside Operator Function
res.real = 2 + 4 = 6
res.img  = 3 + 5 = 8
Step 4: Return Value
res → 6 + 8i

Assigned to:

c3 → 6 + 8i
Step 5: Printing
c3.print();

Output:

6 + 8i
real = r;
img  = i;

Let’s unpack what this initialization/assignment means and why it’s needed.

🔹 What is happening here?

Inside the constructor:

Complex(int r=0,int i=0){
    real = r;
    img  = i;
}
r and i are parameters (inputs to the constructor)
real and img are member variables of the class

👉 So these lines mean:

Assign the value of r to real
Assign the value of i to img
🔹 Why do we need this?

When an object is created, its member variables do NOT automatically get meaningful values.

Without initialization:
Complex c1;
real and img would contain garbage values (random memory data)
With initialization:
Complex c1(2, 3);
real = 2
img = 3

Now the object correctly represents:

2 + 3i
🔹 Simple Analogy

Think of the class as a form:

real, img → empty fields
Constructor → fills the form
Before:
real = ?
img  = ?

After:
real = 2
img  = 3
🔹 Step-by-step Example
Complex c1(5, 7);
Step 1: Constructor is called
Complex(int r=5, int i=7)
Step 2: Assignment happens
real = r → real = 5
img  = i → img  = 7
Final object:
c1 → 5 + 7i
🔹 What if we don’t do this?

If you remove:

real = r;
img  = i;

Then even if you write:

Complex c1(5,7);

👉 real and img will NOT store 5 and 7
👉 They remain uninitialized (garbage) */