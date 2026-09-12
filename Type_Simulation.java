/*Alice challenged Bob to write the same word as his on a typewriter. 
Both are kids and are making some mistakes in typing and are making 
use of the ‘#’ key on a typewriter to delete the last character printed on it. 
An empty text remains empty even after backspaces */ 
import java.util.*;
import java.util.function.Function;

public class Type_Simulation{
public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
String bob=sc.nextLine();
String alice=sc.nextLine();
String pros_bob=string_processed(bob);
String pros_alice=string_processed(alice);
/*if(pros_bob==pros_alice) //Gives wrong result
System.out.println("YES");

else System.out.println("No");*/
/*Why not ==?

In Java:

== → compares references (memory addresses)
.equals() → compares actual content (characters inside the string)
💡 What happens in your case?

When you do:

process(s)
process(t)

These return new String objects (created using StringBuilder).

So even if both results look the same, like "ac", they are:

stored in different memory locations
hence == will return false
✅ Conclusion

You must use:

.equals()

because you are comparing final typed words, not whether both variables 
point to the same object. */
if (isSame(alice, bob)) {
    System.out.println("YES");
} else {
    System.out.println("NO");
}
sc.close();
}
public static String string_processed(String s){
StringBuilder result = new StringBuilder();
for(char ch:s.toCharArray()){
if(ch=='#'){
    if(result.length()>0){
    result.deleteCharAt(result.length()-1);
/*This line removes the last character from the StringBuilder.

🧠 Why result.length() - 1?
result.length() gives the number of characters
Indexing in Java starts from 0
So the last character index = length - 1 */
    }
}
else{
result.append(ch);
}
}
return result.toString();
/*It converts a StringBuilder → String

Why is that needed?
result is a StringBuilder
But we want to:
compare strings
return a String

Java does NOT automatically treat StringBuilder as a String. */
}
// Function to compare both strings
    public static boolean isSame(String s, String t) {
        return string_processed(s).equals(string_processed(t));
    }
}
