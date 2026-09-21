'''In a binary array find the subarray with the maximum number of consecutive 
ones given that u can flip atmost k 0s where k=int'''
#arr=[1,1,1,0,0,0,1,1,1,1,0]

arr=[1,1,1,0,0,0,1,1,1,1,0]
k=int(input())
l=0
count=0
maxlen=0
for r in range(len(arr)):
    if arr[r]==0:
        count+=1
    while count>k:
        if arr[l]==0:
            count-=1
        l+=1
    #maxlen=max(maxlen,r-l+1)
    if (r - l + 1) > maxlen:
        maxlen = r - l + 1
        start = l

subarray = arr[start : start + maxlen]
print(subarray)
subarray = [1 if x == 0 else x for x in subarray]
print(subarray)