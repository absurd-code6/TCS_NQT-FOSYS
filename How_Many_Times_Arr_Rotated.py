'''arr=[3,4,5,1,2,3], ans=3 times'''
def Rotation_Times(arr):
        if not arr:
            return []
        l=0
        h=len(arr)-1
        minm=float("inf")
        times=-1
        while l<=h:
            mid=(l+h)//2
            if arr[l]<=arr[h]:
               if arr[l]<minm:
                minm=arr[l]
                times=l
                break
            if arr[l]<=arr[mid]:
               if arr[l]<minm:
                  minm=arr[l]
                  times=l
                  l=mid+1
            else:
                h=mid-1
                if arr[l]<minm:
                   minm=arr[l]
                   times=l
        return times

arr=list(map(int,input().split()))
print(Rotation_Times(arr))
