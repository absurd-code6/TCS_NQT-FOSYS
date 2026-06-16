'''Given an array arr[] of n integers, convert it into its reduced form. 
In the reduced form, each element is replaced by its rank. 
The smallest element should be replaced with 0, the second smallest 
with 1, and so on, until the largest element is replaced with n - 1.

The relative positions of the elements in the array must remain unchanged.
For repeating elements, the element appearing earlier 
in the original array must be of smaller rank than 
the one appearing later.
You need to modify the array in-place and do not return anything.
Examples:

Input: arr[] = [10, 40, 20]
Output: [0, 2, 1]
Explanation: The elements in sorted order are [10, 20, 40]. 
Therefore, 10, 20, and 40 are assigned ranks 0, 1, and 2 respectively.

Input: arr[] = [0, 2, 1]
Output: [0, 2, 1]
Explanation: The array is already in reduced form.
The elements 0, 1, and 2 are the smallest, second smallest, 
and largest elements respectively.

Input: arr[] = [1, 5, 3, 4, 3]
Output: [0, 4, 1, 3, 2]
Explanation: The elements of the array in sorted order are [1, 3, 3, 4, 5]. 
Assigning ranks from 0 to n - 1 gives 1 as rank 0, the 
first 3 as rank 1, the second 3 as rank 2, 4 as rank 3 
and 5 as rank 4.'''


def Replace_by_rank(arr):
    n=len(arr)
    res=[0]*n
    rank=0 #setting rank=0 here is not going to help
    for i in range(n):
        rank=0 #reset rank = 0 at the start of each outer loop iteration. 
        #Otherwise, rank just keeps accumulating across 
        #different elements, which will give you wildly incorrect, 
        #ever-increasing numbers.
        for j in range(n):
            if arr[j]<arr[i]:
                rank+=1
            elif arr[j]==arr[i] and j<i:
                rank+=1
        res[i]=rank
    for i in range(n):
        arr[i]=res[i]
    return arr


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
print(Replace_by_rank(arr))
