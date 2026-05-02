'''You are given an array of N numbers and an integer X. The task is to 
print all the numbers less than X in the array using min-heap. 
'''
# Skwz Soln:
'''import heapq
nodes=int(input())
heap_list=[]
temp = input().split()
for i in range(nodes):
  heap_list.append(int(temp[i]))
value=int(input())
result=[]
heapq.heapify(heap_list)


#write your code here
while heap_list and heap_list[0] < value:
  print(heapq.heappop(heap_list),end=" ")'''
  
import heapq
def print_less_than_X(arr,X):
    heapq.heapify(arr)  # Convert list into a min heap
    #Extracting elements 1 by 1
    while arr:
        smallest=heapq.heappop(arr)
        if smallest<X:
            print(smallest,end=" ")
        else:
            break

print("Enter an array:")
arr=list(map(int,input().split()))
 
'''This line is the culprit:

arr = map(int, input().split())

👉 map() in Python returns a map object (iterator), not a list.

But heapq.heapify() requires a list, not an iterator.

Just convert it into a list:

arr = list(map(int, input().split()))'''
#arr = [10, 4, 15, 20, 0, 3]
X=int(input("Enter the value of X:"))          
print_less_than_X(arr,X)

'''Key intuition

A Min-Heap always keeps the smallest element at the top.

So instead of scanning the array normally, we:

Insert all elements into a Min-Heap
Keep extracting the smallest element
Stop when the element is ≥ X

Why this works:

Heap gives us elements in sorted order (ascending)
So once we hit a number ≥ X, we can stop early
⚙️ 3. Step-by-step logic
Create a Min-Heap
Insert all array elements into the heap
While heap is not empty:
Extract the minimum element
If it is less than X → print it
Else → stop (because all next elements will be larger)

What is heapq in python?
heapq is a built-in Python module that lets you use a heap data structure.

👉 More specifically: it implements a Min-Heap.

💡 What is a Min-Heap?

A Min-Heap is a special tree where:

The smallest element is always at the root (top)
Every parent is ≤ its children

In Python’s heapq, the heap is stored as a list, not a tree.

⚙️ Key Operations in heapq
1. Convert list into heap
import heapq

arr = [10, 4, 15, 20, 0, 3]
heapq.heapify(arr)

print(arr)

👉 Rearranges list into heap form (not fully sorted!)

2. Get smallest element
print(arr[0])

👉 Always gives the minimum element

3. Remove smallest element
smallest = heapq.heappop(arr)

👉 Removes and returns the smallest element

4. Insert element
heapq.heappush(arr, 2)

👉 Adds element while maintaining heap property

🔍 Example
import heapq

arr = [10, 4, 15, 20, 0, 3]
heapq.heapify(arr)

print("Heap:", arr)

print("Pop:", heapq.heappop(arr))
print("After pop:", arr)

Output:

Heap: [0, 4, 3, 20, 10, 15]
Pop: 0
After pop: [3, 4, 15, 20, 10]
⚠️ Important points
It is a Min-Heap only
It does not fully sort the list
Internally uses a binary heap
Time complexity:
heapify() → O(N)
heappush() → O(log N)
heappop() → O(log N)
🔄 What if you need a Max-Heap?

Python doesn’t provide it directly, but you can trick it:

arr = [10, 4, 15]

max_heap = [-x for x in arr]
heapq.heapify(max_heap)

print(-heapq.heappop(max_heap))  # gives largest element
✅ When to use heapq?

Use it when you need:

Smallest / largest element quickly
Priority queues
K smallest / largest elements
Problems like your current one 😉'''
