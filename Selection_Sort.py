def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
               min_idx=j
        arr[j],arr[min_idx]=arr[min_idx],arr[j]
    return arr
arr=list(map(int,input().split()))
print(*selection_sort(arr))

'''Step-by-Step Example
Consider the array [5, 3, 1] on the first pass (i = 0):

Initial state: min_idx = 0 (assumes 5 is the smallest).

Check j = 1 (value 3): Since 3 < 5, min_idx updates to 1. 
We don't swap yet—we just remember that 3 at index 1 is 
currently the smallest.

Check j = 2 (value 1): Since 1 < 3, min_idx updates to 2. 
Now we know 1 at index 2 is the actual minimum.

Loop ends: The inner loop finishes, and min_idx points to 2.

Swap: We swap arr[i] (5) with arr[min_idx] (1). 
The array becomes [1, 3, 5].

Updating min_idx = j keeps track of the best candidate for the 
minimum element without making unnecessary or 
incorrect intermediate swaps.'''