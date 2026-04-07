"""Alice challenged Bob to write the same word as his on a typewriter. Both are kids and are making some mistakes in typing and are making use of the ‘#’ key on a typewriter to delete the last character printed on it. An empty text remains empty even after backspaces. 

Input Format
The first line contains a string typed by Bob.

The second line contains a string typed by Alice.

Output Format
The first line contains ‘YES’ if Alice is able to print the exact words as Bob, otherwise ‘NO’.

Constraints
1 <= Bob.length

Alice.length <= 100000

Bob and Alice only contain lowercase letters and '#' characters."""

def string_processed(s:str) -> str:
    word=[]
    for char in s:
        if char=='#':
            if word:
                word.pop()
        else:
            word.append(char)
    return ''.join(word)

""" The line return ''.join(result) in Python is used to join a sequence of strings (in this case, the list result) into a single string, with no separator between the elements.

Breakdown of ''.join(result):
result is a list that contains individual characters as strings. For example, result might look like this: ['a', 'b', 'c'].
''.join(result):
''.join() is a string method that concatenates all the elements of the iterable (like a list) into a single string.
'' is the separator for joining the elements. Since it’s an empty string, it means no space or separator is inserted between the characters as they are joined together.

So, if result = ['a', 'b', 'c'], then:

''.join(result)

returns the string:

"abc"
Why ''.join(result) is used:
Efficiency: Concatenating strings using + in a loop can be inefficient because strings are immutable in Python. Every time you concatenate, a new string is created. Using ''.join(result) is more efficient because it directly joins the elements in one pass.
Example Walkthrough:
result = ['H', 'e', 'l', 'l', 'o']
final_string = ''.join(result)
print(final_string)

Output:

Hello
What happens if you use a different separator?

You can use a different separator instead of an empty string ''. For example, if you wanted to join the characters with a space, you could do this:

' '.join(result)  # Joins with a space between characters

This would produce:

'H e l l o' """

bob=input().strip()
alice=input().strip()
'''The strip() function in Python is a built-in string method 
that removes leading and trailing whitespace characters from a string. 
Whitespace characters include spaces, tabs (\t), and newlines (\n).

How strip() works:
Leading whitespace: Any spaces, tabs, or newlines at the beginning
of the string.
Trailing whitespace: Any spaces, tabs, or newlines 
at the end of the string.
Syntax:
string.strip()
strip() returns a new string with the whitespace removed from both ends.
The original string remains unchanged '''

#Strings are immutable in Python .

'''Example:
text = "   Hello, World!   "
cleaned_text = text.strip()

print(f"Original: '{text}'")
print(f"Cleaned: '{cleaned_text}'") '''

pros_bob=string_processed(bob)
pros_alice=string_processed(alice)
if pros_bob==pros_alice:
    print("YES")
else:
    print("NO")
'''Other way to concatenate strings:
Using the + Operator

The + operator is the simplest and most straightforward way to concatenate strings in Python.

Example:
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"
Pros:
Very simple and easy to understand.
Cons:
Inefficient for large numbers of concatenations: Each time you concatenate two strings using +, a new string is created. This can become inefficient if you're concatenating strings in a loop or doing multiple concatenations.'''