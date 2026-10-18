'''Given two numbers N and M, find the Nth root of M. The Nth root of a 
number M is defined as a number X such that when X is raised to the 
power of N, it equals M. If the Nth root is not an integer, return -1.

Example 1:
Input: N = 3, M = 27

Output: 3

Explanation: The cube root of 27 is equal to 3.

Example 2:
Input: N = 4, M = 69

Output:-1

Explanation: The 4th root of 69 does not exist. So, the answer is -1.
'''
def Nth_Root(n:int,m:int)->int:
    if n==0:
            return -1
    if m==0:
            return 0
    if n%2==0: #Even root of a negative number is not a real integer
            return -1
    for i in range(m+1):
        prod=1
        for _ in range(n):
            prod*=i
            if prod>m:
                return i-1
            if prod==n:
                return i
            if prod<0:
                return -1
    return -1        

def Nth_Root_BS1(n:int,m:int)->int:
    if n==0:
            return -1
    if m==0:
            return 0
    if n%2==0: #Even root of a negative number is not a real integer
            return -1
    l=1
    h=m
    ans=0
    while l<=h:
        mid=(l+h)//2
        
        if mid**n<=m:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans


def Nth_Root_BS2(n:int,m:int)->int:
    if n==0:
        return -1
    if m==0:
        return 0
    if n%2==0: #Even root of a negative number is not a real integer
        return -1
    l=1
    h=m
    ans=0
    while l<=h:
        mid=(l+h)//2
        prod=1
        for _ in range(n):
            prod*=mid
            if prod>m:
                break
        if prod<=m:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans

n=int(input())
m=int(input())
print(Nth_Root_BS1(n,m))
