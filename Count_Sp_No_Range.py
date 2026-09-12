




'''import math
l,r=map(int,input().split())
limit=math.isqrt(r)
if limit<2:
    print(r-l+1)
    exit() #return
prime=[True]*(limit+1)
prime[0]=prime[1]=False
for i in range(2,math.isqrt(limit)+1):
    if prime[i]:
        for j in range(i*i,limit+1,i):
            prime[j]=False
special_count=0
for p in range(2,limit+1):
    if prime[p]:
        if l<=p*p<=r:
            special_count+=1
total_nos=r-l+1
print(total_nos-special_count)
'''