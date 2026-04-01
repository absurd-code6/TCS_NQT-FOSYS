def printArray(arr,n):
  for i in range(n):
    print(arr[i])

n=int(input("Enter the size of the array"))
arr=[]
print("Enter the",n,"elements:")
for i in range(n):
    x=int(input())
    arr.append(x);
print("Given Array is:")
printArray(arr,n)
largest=second_largest=float('-inf')
smallest=second_smallest=float('inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
       second_smallest = num

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)

''' The easiest 3-line Python solution uses sorting.'''
'''print("Enter the array elements side by side:")
arr = list(map(int, input().split()))
arr.sort()
print("Second Smallest:", arr[1], "Second Largest:", arr[-2])'''
