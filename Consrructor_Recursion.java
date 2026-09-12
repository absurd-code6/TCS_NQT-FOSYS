class recur{
    recur(){
    System.out.println("Constructor Recursion");
    //new recur();//recursive object creation
    }
static recur a = new recur();//static keyword prevents stack overflow
}

public class Consrructor_Recursion {
public static void main(String[] args) {
new recur();
}
/*Stack Overflow: Java uses something called a call stack to keep track of 
function calls.

Every time:

a method is called, or
a constructor runs

👉 a new “frame” is added to the stack

⚠️ Problem:

The stack has limited memory

If calls keep happening like this:

Gfg() → Gfg() → Gfg() → Gfg() → ...

The stack fills up completely.

💥 Then Java throws:
Exception in thread "main" java.lang.StackOverflowError*/

}
