
#arr=[7,8,9,1,2,3,4,5,6] , target(t or k)=1

def Rotated_BS(arr,t): # Duplicates Allowed
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==t:
            return mid
        elif arr[l]<=arr[mid]:
            if arr[l]<=t and t<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=t and t<=arr[h]:
                l=mid+1
            else:
                h=mid-1
    return -1

n=int(input()) #9
arr=[int(input()) for _ in range(n)] #[7,8,9,1,2,3,4,5,6]
t=int(input())

def Rotated_BS2(arr,t):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==t:
            return True
        if arr[l]==arr[mid] and arr[mid]==arr[h]:
            l=mid+1
            h=mid-1
            continue
        if arr[l]<=arr[mid]:
            if arr[l]<=t and t<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=t and t<=arr[h]:
                l=mid+1
            else:
                h=mid-1
    return False

