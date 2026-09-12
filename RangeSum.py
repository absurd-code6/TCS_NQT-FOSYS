def rangeSum(i,j):
  return ((j*(j+1))//2) - ((i*(i-1))//2)
print("Please enter 2 numbers in the range 1-9999")
i=int(input("Enter 1st No: "))
j=int(input("Enter 2nd No :"))

if i>=j or i<0 or j>=10000:
    print("Invalid")
else:
    print("SUM is : ", rangeSum(i,j))

'''Now there are three possible interpretations:

Range Type	Numbers Added	Result
Inclusive	3 + 4 + 5	12
Exclude i	4 + 5	9
Exclude both	4	4

Your formula must match the intended range.

If your goal is:

sum from i to j (inclusive)

Then:

S(j) - S(i) -> ((j*(j+1))//2) - ((i*(i+1))//2)

❌ is incorrect because it skips i

You need:

S(j) - S(i-1) -> ((j*(j+1))//2) - ((i*(i-1))//2)
🔹 Key Insight
Formula Used	Meaning
S(j) - S(i)	excludes i
S(j) - S(i-1)	includes i '''
