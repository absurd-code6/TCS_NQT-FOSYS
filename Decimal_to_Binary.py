N=int(input())
res=""
while N>0:
    res+=str(N%2)
    N//=2
binary=res[::-1]
print(binary)
