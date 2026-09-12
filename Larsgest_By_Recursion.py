def Findlargest(arr):
    if len(arr)==1:
      return arr[0]
    return max(arr[0],Findlargest(arr[1:]))

#arr=[]
print("Enter the array elements side by side:")
arr=list(map(int , input().split()))
largest=Findlargest(arr)
print("Largest is:",largest)
