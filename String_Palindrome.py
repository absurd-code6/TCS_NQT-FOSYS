# Python version of the palindrome checker
def palindrome_checker(s):
    s=s.replace(" ","").lower()
    # Remove spaces and convert to lowercase
    reversed=s[::-1]
    # Check if the string is the same forwards and backwards
    return s==reversed

string=str(input("Enter a string:"))
if palindrome_checker(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
