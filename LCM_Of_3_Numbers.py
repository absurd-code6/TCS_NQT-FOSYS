# Write a python program to find lcm of 2 numbers
def LCM_Of_2(n1,n2):
    if n1==0 or n2==0:
        return 0
    nmax=max(n1,n2)
    while True:
        if nmax%n1==0 and nmax%n2==0:
            return nmax
        nmax+=1
#        OR
import math
def GCD_Of_2(n1,n2): #For finding gcd/HCF of 2 numbers
    # Euclidean algorithm to find GCD of two numbers
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
     
def LCM_Two(n1,n2):
    return abs(n1 * n2) // math.gcd(n1, n2) # Or GCD_Of_2(n1,n2)

# Write a python program to find lcm of 3 numbers
def LCM_Of_3(n1,n2,n3):
    if n1==0 or n2==0 or n3==0:
            return 0
    return LCM_Of_2(LCM_Of_2(n1,n2),n3)

line=list(map(int,input().split()))
n1=line[0]
n2=line[1]
n3=line[2]
print(LCM_Of_3(n1,n2,n3))
