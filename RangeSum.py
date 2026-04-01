def rangeSum(i,j):
  return ((j*(j+1))//2) - ((i*(i-1))//2)
print("Please enter 2 numbers in the range 1-9999")
i=int(input("Enter 1st No: "))
j=int(input("Enter 2nd No :"))

if i>=j or i<0 or j>=10000:
    print("Invalid")
else:
    print("SUM is : ", rangeSum(i,j))