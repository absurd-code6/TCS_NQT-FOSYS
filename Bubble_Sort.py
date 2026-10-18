def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

arr=list(map(int,input().split()))
print(*bubble_sort(arr))

'''No of passes= No swaps => O(n) BC TC
(n-1)+(n-2)+(n-3)+(n-4)+.....=> O(n^2) AC/WC TC'''
