/*Write a program in java to determine whether a user-given string is 
palindrome or not */
import java.util.*;


public class String_Palindrome{

public static boolean palindrome_checker(String s){
s = s.replaceAll("\\s+", "").toLowerCase(); 
// remove spaces + normalize case
/*s = s.replaceAll("\\s+", "").toLowerCase();
s.replaceAll(...) → This method replaces parts of a string based on a regular expression (regex).
"\\s+" → This regex matches one or more whitespace characters (spaces, tabs, newlines).
"" → Replaces matched spaces with nothing, effectively removing them.
.toLowerCase() → Converts all letters in the string to lowercase.
s = ... → Stores the modified string back in s.

Purpose:
This line normalizes the input so that variations in case or spaces don’t affect the palindrome check.

Example:

Original s	After this line
"Nurses Run"	"nursesrun"
"Madam"	"madam"
"A man a plan"	"amanaplan" */
String reversed = new StringBuilder(s).reverse().toString();
/*String reversed = new StringBuilder(s).reverse().toString();
new StringBuilder(s) → Creates a mutable sequence of characters from the string s.
.reverse() → Reverses the sequence of characters in place.
.toString() → Converts the reversed sequence back into a String.
String reversed = ... → Stores the reversed string in the variable reversed.

Purpose:
This line generates the mirror image of the normalized string so it can be compared to the original. */
return s.equals(reversed);
/*s.equals(reversed) → Checks if the normalized string is exactly equal to its reversed version.
Returns true if the string reads the same forwards and backwards, otherwise false.

Purpose:
This line decides whether the string is a palindrome. */
}

public static void main(String[] args) {
Scanner sc= new Scanner(System.in);
System.out.println("Enter a string:");
String input = sc.nextLine();
if(palindrome_checker(input))
     System.out.println("The string is a palindrome");
else System.out.println("The string is not a palindrome");
}
}
