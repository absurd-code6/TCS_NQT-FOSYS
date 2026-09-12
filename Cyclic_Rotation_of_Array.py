'''Given an array Arr[] of N integers and a positive integer K, cyclically 
rotate the array clockwise by K. Input Format: • 
First line: N (number of elements) • 
Second line: N space-separated integers (array elements) • 
Third line: K (number of rotations) Output Format: • 
Rotated array as space-separated integers 
Example Sample Input 5 10 20 30 40 50 2 
Output 40 50 10 20 30 
Sample Input 5 1 2 3 4 5 
Output 3'''

def Cyclic_rotation(N,arr,K):
    # Handle rotations greater than array size
    K=K%N
    rotated_arr=arr[-K:] + arr[:-K]
    #return rotated_arr
    return ' '.join(map(str,rotated_arr))#3 4 5 1 2 for 1 2 3 4 5
    
N=int(input())
arr=list(map(int,input().split()))
K=int(input())
print(Cyclic_rotation(N,arr,K))

'''
What does rotation mean?

Rotation means shifting the elements of the array while keeping 
the same order, and the elements that go out from one end come 
back from the other end.

For a clockwise (right) rotation, the last elements move to the front.

For example:

Array:  [10, 20, 30, 40, 50]

Rotate clockwise by 1:

Last element (50) comes to the front.

[50, 10, 20, 30, 40]

Rotate clockwise by 2:

Step 1:
[50, 10, 20, 30, 40]

Step 2:
[40, 50, 10, 20, 30]

This is the final answer.

To cyclically rotate an array clockwise by K positions:

Compute K = K % N (to handle cases where K > N).
Take the last K elements and move them to the front.
Append the remaining elements.

K = K % N

Why do we do this?

Suppose

N = 5
K = 7

Rotating 7 times is the same as rotating

7 % 5 = 2

times.

So,

K = 7 % 5 = 2

This avoids unnecessary rotations.

The main line
rotated = arr[-K:] + arr[:-K]

This is the important part.

Let's understand each slice.

Our array is

Index: 0   1   2   3   4
Value:10  20  30  40  50
arr = [10,20,30,40,50]

and

K = 2
First slice
arr[-K:]

means

arr[-2:]

Negative indexing:

-5  -4  -3  -2  -1
10  20  30  40  50

Starting from -2 means starting from 40 until the end.

So,

arr[-2:]

= [40,50]

These are the last 2 elements.

Second slice
arr[:-K]

becomes

arr[:-2]

It means

"Take everything before the last two elements."

So,

arr[:-2]

= [10,20,30]
Concatenation

Now,

arr[-2:] + arr[:-2]

becomes

[40,50] + [10,20,30]

Result

[40,50,10,20,30]

Exactly the required rotated array.'''