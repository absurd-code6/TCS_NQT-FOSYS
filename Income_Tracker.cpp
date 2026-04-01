/*Write a program to manage expenses from a given total income.
Input:
1.Total Income:Integer Value
2.For each expense enter the following inputs repeatedly until the users enters
"done":
Cateogory/Type Of Expense:String value(eg. "food", "shopping")
Expense:Integer value for the amt spent.
Output:
1.Print Total Income
2.Total sum of expenses
3.Total Savings = Total Income - Total Expenses
Print the breakdown of expenses for each category*/

#include<iostream>
#include<math.h>
#include<string>
#include<unordered_map>//You need to include these coz u're using iostream
#include<vector>//& not bits/stdc++.h
using namespace std;
int main(){
int total_inc=0;
/*total_exp contains garbage—whatever happened to be in that memory location.
Using it in calculations without initializing can give nonsense results.

Later in the program, you do:
total_exp += exp;
This adds each new expense to total_exp.
If total_exp isn’t initially zero, your running total would be wrong.*/
int total_exp=0;
cout<<"Total Income: ";
cin>>total_inc;
cin.ignore();

/*When u insert an int dtype followed by the insertion of string, in b/w u need
to insert cin.ignore() jst like sc=nextInt() in java. Otw there can be input
mismatch.*/

unordered_map<string,int>mp;//using map data structure
/*NOTE:Map DS whether unordered or ordered does not maintain insertion order.
This means that it does'nt print the output corresponding to the insertion 
orderof inputs.

But we need to maintain order eg. food,shopping,bill
So we will use a vector to store the index of the input value*/
vector<string>v;
while(true){
string cat="";//string variable for category
int exp;//integer variable for expenses 
cout << "Enter category (or 'done' to finish): ";
getline(cin,cat);
if(cat=="done")
break;
cin>>exp;
cin.ignore();
if(mp.find(cat)==mp.end())
/*mp is an unordered_map<string, int> storing expense totals by category.
mp.find(cat) searches for the category cat in the map.
If the category is not found, it returns mp.end().
So mp.find(cat) == mp.end() checks if this is the first time 
this category appears.
If it is a new category,then only we add it to the vector v.*/
v.push_back(cat);
mp[cat]+=exp;
/*This adds the expense exp to the total for the category cat in the map.
How it works:
If cat is already in the map, it adds exp to the existing value.
If cat is not in the map, mp[cat] automatically initializes it to 0, 
then adds exp.
mp["Food"] += 50;  if Food wasn't there, it's now 50
mp["Food"] += 30;  now Food is 80*/
total_exp+=exp;
/*Adds the expense exp to the running total of all expenses.
This variable is separate from category totals and is used to calculate total savings:
Total Savings = total_inc - total_exp*/
}
cout<<total_inc<<endl;
cout<<total_exp<<endl;
cout<<"Total Savings: "<<total_inc-total_exp<<endl;

cout << "\nExpenses by Category:\n";
for(string s : v)
cout<<s<<":"<<mp[s]<<endl;
return 0;
}