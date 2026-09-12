/*Given a value V, we want to make change for V and we have infinite 
supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued notes, 
what is the minimum number of notes needed to make the change? 
You have to output all the denominations used to make this change. 
The biggest denomination should be displayed first followed 
by the smaller denominations. 

Suppose V = 93, the output should look like :- 

50 20 20 2 1 */

import java.util.*;

public class Min_Notes {
public static void MinNotes(int v,int[] d){
for(int i=d.length-1;i>=0;i--){
while(v>=d[i]){
System.out.println(d[i]);
v-=d[i];
}
}
}
public static void main(String[] args) {
int[] d={1,2,5,10,20,50,100,500,1000};
Scanner sc=new Scanner(System.in);
System.out.println("Enter the value v:");
int v=sc.nextInt();
MinNotes(v,d);
sc.close();
}
}
