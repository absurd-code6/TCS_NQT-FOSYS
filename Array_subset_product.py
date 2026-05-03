'''You are given an array of n elements consisting of only positive 
numbers and an integer i. You have to find the minimum product 
of all the possible subsets of size i in the given array. 
Since output could be large, hence do it modulus by (10^9+7) and 
then print the answer. '''

arr=list(map(int,input().split()))
i=int(input("Enter the value of i:"))
arr.sort()
mod=10**9 + 7
product=1
for j in range(i):
    product*=arr[j]
print(product%mod)
# for [1,2,3,4,5] output=6 & so on....