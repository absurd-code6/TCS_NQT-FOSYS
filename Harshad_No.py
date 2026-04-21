'''A Harshad number (or Niven number) is a positive integer that 
is divisible by the sum of its digits. Coined from Sanskrit 
meaning "joy-giving," these numbers (e.g., 18, 21, 1729) are 
divisible by the sum of their digits in a given base, usually base 10. 
For instance, 18 is a Harshad number because 1+8=9 and 18/9=2
Thus, 18%9=0'''

n=int(input("Enter a number:"))
sum=0 #it’s better not to use sum as a variable name since it 
#overrides Python’s built-in sum() function.
num=n
while n!=0 :
    digit=n%10
    sum=sum+digit
    n//=10
if num%sum==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")

    
    