'''Problem: "Quick Sort Pivot Indexing"
This focuses specifically on the PARTITION step of Quick Sort:
given an array, choose the LAST element as the pivot, rearrange
the array so all elements smaller than the pivot come before it
and all elements larger come after it, and report the pivot's
FINAL INDEX after partitioning (this is the index the pivot would
occupy in the fully-sorted array too, which is why Quick Sort's
recursion splits the problem around exactly this index).
'''
def Quick_Sort_Pivot_Index(arr):
    n=len(arr)
    pivot=arr[n-1]
    items_lower=[]
    items_greater=[]
    for i in range(n):
        if arr[i]<pivot:
            items_lower.append(i)
        elif arr[i]>pivot:
            items_greater.append(i)
#Modify the input array in place to reflect the partition
    arr[:]=items_lower + [pivot] + items_greater
# The pivot's final index is equal to the number of elements smaller than it
    print(pivot)
    return len(items_lower)
    
arr=list(map(int,input().split())) #[10, 80, 30, 90, 40, 50, 70]
print(Quick_Sort_Pivot_Index(arr))