from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def display(self):
        for i in self.graph:
            print(f"{i}->{self.graph[i]}")



        
'''s=input()
t=input()
lis=[]
from itertools import zip_longest'''

        
'''fib = lambda n: (lambda f: f(f, n)[0])(lambda s, k: (0, 1) if k == 0 else (lambda a, b: (a * ((b << 1) - a), a * a + b * b) if not k & 1 else (a * a + b * b, a * ((b << 1) - a) + a * a + b * b))(*s(s, k >> 1)))'''        

def digit_game(arr):
    single_sum=sum(i for i in arr if i<10)
    double_sum=sum(j for j in arr if 10<j and j<100)
    if single_sum!=double_sum:
        print("true")
    return -1

def increasing_triplets(nums):
    first=float('inf')
    second=float('inf')
    for i in nums:
        if i<=first:
            first=i
        elif i <=second:
            second=i
        else:
            return True
    return False

def max_rainwater(arr):
    n=len(arr)
    for i in range(1,n-1):
        left=arr[i]
        for j in range(i):
            left=max(left,arr[j])
        right=arr[i]
        for j in range(i+1,n):
            right=max(right,arr[j])
        max_water=0
        max_water+=(min(left,right)-arr[i])
    return max_water

def remove_duplicates(arr):
    j=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[j]=arr[i]
            j+=1
    return arr[:j]

def Product_except_itself(arr):
    n=len(arr)
    ans=[1]*n
    prefix=1
    suffix=1
    for i in range(n):
        ans[i]=prefix
        prefix*=arr[i]
    for i in range(n-1,-1,-1):
        ans[i]*=suffix
        suffix*=arr[i]
    return ans

def min_denominations(v,notes):
    for i in range(len(notes)-1,-1,-1):
        while v>=notes[i]:
            print(notes[i],end=" ")
            v-=notes[i]
notes=[1,2,5,10,20,50,100,500,1000]
min_denominations(int(input()),notes)
        
arr=list(map(int,input().split()))

def isSubseq(s,t):
    i=0
    j=0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    if i==len(s):
        print("True")
    else:
        print("False")
#   return i==len(s)

def isSubstring(txt,pat):
    n=len(txt)
    m=len(pat)
    for i in range(n-m+1):
        j=0
        while j<m and txt(i+j)==pat[j]:
            j+=1
        if j==m:
            return i
    return -1

def all_routes(cities,start,finish,fuel):
    def dfs(cur_city,rem_fuel):
        if rem_fuel<0:
            return 0
        elif cur_city==finish:
            res=1
        else:
            res=0
        for nxt_city in range(len(cities)):
            if cur_city!=nxt_city:
                cost=abs(cities[cur_city]-cities[nxt_city])
                rem_fuel-=cost
                res+=dfs(nxt_city,rem_fuel)
        return res % (10**9+7)
    return dfs(start,fuel)


def value_equal_substrings(s):
    i=0
    two_count=0
    while i<len(s):
        j=i
        while j<len(s) and s[j]==s[i]:
            j+=1
        length=j-i
        if length%3==2:
            two_count+=1
        if length== 1 or length == 4 or length == 7:
            print("Impossible")
        if length%3==1:
            return False
        i=j
    return two_count==1

def stock_buy_n_sell(prices):
    max_profit=0
    min_price=prices[0]
    for p in prices:
        if p<min_price:
            min_price=p
            profit=p-min_price
        max_profit=max(max_profit,profit)
    return max_profit

profit=0
 
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        profit=max(prices[j]-prices[i])
print(profit)

    


