import java.util.*;

interface P1{
void display();
}

interface P2{
int add(int a,int b);
}

class Child implements P1,P2{
public void display(){
System.out.println("Multiple Inheritance");
}
public int add(int a,int b){
return a+b;
}
}

public class Inherit{
public static void main(String[] args) {
Child baby=new Child();
baby.display();
int sum=baby.add(4,5);
System.out.println(sum);

}
}