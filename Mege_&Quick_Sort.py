'''Write a program to take input of an array
Then press 1 to perform quick sort by defining one user defined function
Or press 2 to perform merge sort by defining another user defined function 
At the end print sorted array in main()'''


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        l = arr[:mid]
        r = arr[mid:]
        
        mergesort(l)
        mergesort(r)
        
        i =j=k= 0       
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
            k = k + 1
            
        while i < len(l):
            arr[k] = l[i]
            i = i + 1
            k = k + 1
            
        while j < len(r):
            arr[k] = r[j]
            j = j + 1
            k = k + 1

def quickSort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        
        j = low
        while j < high:
            if arr[j] < pivot:
                i = i + 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j = j + 1
            
        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp
        
        p = i + 1
        
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

def QuickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr.pop() # or arr[-1]
    items_lower=[]
    items_greater=[]
    for no in arr:  #or arr[:-1]:
        if no<pivot:
            items_lower.append(no)
        else:
            items_greater.append(no)
    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)  

'''The square brackets create a list containing a single element.

In this line:

return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)
QuickSort(items_lower) returns a list.
QuickSort(items_greater) also returns a list.
pivot is just a single integer (or whatever type your array contains), 
not a list.

Python allows you to concatenate lists with +, but all 
operands must be lists:

[1, 2] + [3] + [4, 5]
# Result: [1, 2, 3, 4, 5]

If you wrote:

QuickSort(items_lower) + pivot + QuickSort(items_greater)

and pivot was 3, Python would try to do:

[1, 2] + 3

which raises:

TypeError: can only concatenate list (not "int") to list

So [pivot] converts the single value into a one-element list:

pivot = 3

[pivot]
# Result: [3]

Then the concatenation works:

[1, 2] + [3] + [4, 5]
# Result: [1, 2, 3, 4, 5]'''
#why not list(pivot)?
'''Because list() expects an iterable (something you can loop over), 
while pivot is usually just a single value like an integer.

For example:

pivot = 5

list(pivot)

This gives:

TypeError: 'int' object is not iterable

On the other hand:

[pivot]

creates a list containing that one value:

[5]
When does list() work?

It works with iterables such as strings, tuples, sets, 
and other lists:

list("abc")      # ['a', 'b', 'c']
list((1, 2, 3))  # [1, 2, 3]
list({1, 2, 3})  # [1, 2, 3] (order may vary)

But not with a single integer or float:

list(5)      # TypeError
list(3.14)   # TypeError

So in QuickSort, if pivot is an integer:

pivot = arr[-1]

you should use:

[pivot]

because you want a list containing one element, 
not to convert an iterable into a list.'''

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print("Press 1 to sort by Quick Sort")
    print("Press 2 to sort by Merge Sort")
    key = input()
    if key == "1":
        quickSort(arr, 0, len(arr) - 1)
        print(arr)
    elif key=="2":
        mergesort(arr)
        print(arr)