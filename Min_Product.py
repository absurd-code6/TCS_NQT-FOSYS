#Greedy Algorithm Q1
#Given an array, we have to find minimum product possible with the 
#subset of elements present in the array. The minimum product can be a single #element also.
def min_sub_product(arr):
    if len(arr)==0:
        return 0
    neg_count=0
    zero_count=0
    max_neg=float('-inf')   # largest negative (closest to 0)
    min_pos=float('inf')    # smallest positive
    
    for num in arr:
        if num==0:
            zero_count+=1
            continue
        if num<0:
            neg_count+=1
            max_neg=max(neg_count,num)
            
        if num>0:
            min_pos=min(min_pos,num)
        prodt*=num
    if zero_count==len(arr):
        return 0
    if neg_count==0:
        return 0 if zero_count>0 else min_pos
    if neg_count%2==0:
        prodt=prodt//max_neg
    return prodt
        
arr = [ -1, -1, -2, 4, 3 ]
print("Minimum product subset is:", min_sub_product(arr))

'''We want the smallest possible product we can make using any subset of the array.
A subset can be:

One element
Some elements
Or all elements
💡 Key Observations
Negative numbers are powerful
Multiplying two negatives → positive
Multiplying odd negatives → negative (which is smaller)
Zero can ruin everything
Anything × 0 = 0
Sometimes 0 is the smallest possible answer
Positive numbers increase product
So we usually avoid taking too many positives unless needed

Problem Case: Even Negatives

Example:

arr = [-1, -2, -3, -4]
Negatives = 4 (even)
Product = (-1)×(-2)×(-3)×(-4) = 24 (positive ❌)

But we can do better:

Remove one negative:
(-2)×(-3)×(-4) = -24 ✅ (smaller!)
🎯 Which Negative Should We Remove?

We remove the least harmful negative, meaning:

👉 The negative number closest to zero

Example:

[-1, -2, -3, -4]
Closest to zero = -1

Why remove -1?

It affects the product the least
Keeps the result as small (negative) as possible
🔍 What is max_neg?
max_neg = max(max_neg, num)

This stores:
👉 The largest negative number
👉 i.e., the one closest to zero

Example:

[-5, -2, -8]
max_neg = -2
🧮 Why divide?

Earlier, we multiplied everything:

product *= num

So now product includes all numbers

To remove one number:
👉 We divide by it

Simple Example
arr = [-1, -2, -3, -4]

Step-by-step:

product = 24
neg_count = 4 (even)
max_neg = -1

Now:

product = 24 // (-1)

Result = -24 ✅ (minimum possible)'''