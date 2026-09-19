'''Find idx of 1st occurence and Lst occurence in a sorted array
Eg. arr=[2,4,6,8,8,8,11,13]
O/p:{3,5}'''

#What's lower bound -> smallest idx such that arr[i]>=k
#What's upper bound -> smallest idx such that arr[i]>k
def lowerBound(arr,k):
    l=0
    h=len(arr)-1
    lb=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>=k:
            lb=mid
            h=mid-1
        else:
            l=mid+1
    return lb

def upperBound(arr,k):
    l=0
    h=len(arr)-1
    ub=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>k:
            ub=mid
            h=mid-1
        else:
            l=mid+1
    return ub

def Fst_nLst(arr,n,k):
    lb=lowerBound(arr,n,k)
    if lb==n or arr[lb]!=k:
       return -1
    return {lb,upperBound(arr,n,k)-1}

#Alternative: Using BS & without LB UB

def Fst_BS(arr,k):
    l=0
    h=len(arr)-1
    first=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==k:
            first=mid
            h=mid-1
        elif arr[mid]<k:
            l=mid+1
        else:
            h=mid-1
    return first


def Lst_BS(arr,k):
    l=0
    h=len(arr)-1
    last=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==k:
            last=mid
            l=mid+1
        elif arr[mid]<k:
            l=mid+1
        else:
            h=mid-1
    return last

def countAllOccurences(arr,k):
    first=Fst_BS()
    if first==-1:
        return 0
    # If the element isn't in the array, first index will be -1
    last=Lst_BS()
    all_occ=last-first+1
    return all_occ
#TC=O(logn),SC=O(1)

n=int(input()) #8
arr=[int(input()) for _ in range(n)] #[2,4,6,8,8,8,11,13]
k=int(input())
print(f"{{{Fst_BS(arr,k)},{Lst_BS(arr,k)}}}")
print(countAllOccurences(arr,k))