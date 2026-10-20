'''Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.
Return the kth positive integer that is missing from this array.
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. 
The 2nd missing positive integer is 6.
'''
def Missing_Integer_BF(arr:list[int],k:int):
    '''Brute Force Approach. A clever O(n) linear scan approach that is correct 
    and passes all test cases!'''
    if not arr:
        return -1
    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k

def Missing_Integer_BS(arr:list[int],k:int):
    '''Optimised O(logn) Binary Search Approach'''
    if not arr:
        return -1
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        missing_nos=arr[mid]-(mid+1)
        if missing_nos<k:
            l=mid+1
        else:
            h=mid-1
    # Once binary search finishes, the answer is always l + k
    return l + k

print(Missing_Integer_BF([2,3,4,7,11],k=5))
print(Missing_Integer_BS([1,2,3,4],k=2))

'''How the Brute Force code works:
Instead of generating every single missing number one by one, it iterates 
through the array and checks if the current element arr[i] is less 
than or equal to k.If it is, it means at least one missing number exists 
at or before this point, so we shift our target k up by 1 (k += 1).
The moment arr[i] exceeds k, it means our target k-th missing number falls 
before this element, so we stop and return k.'''

'''HoW  Binary Search code works:
 The Big Idea
Imagine you are lining up the numbers that should be there: 1, 2, 3, 4, 5, 6...
If your array is [2, 3, 4, 7, 11], look at what is missing:

At index 0, the number is 2. (We expected 1, so 1 number is missing).

At index 1, the number is 3. (We expected 2, so 1 number is missing).

At index 3, the number is 7. (We expected 4, so 3 numbers are missing: 1, 5, and 6).

Instead of checking every single number one by one, Binary Search lets us 
quickly jump to the middle of the array and ask: "How many numbers are missing 
up to this point?"
The Secret FormulaFor any index mid, we can calculate how many numbers are 
missing before or at that index using this formula:missing_count = arr[mid] - (mid + 1)
arr[mid] is the actual number in the array.
mid + 1 is what the number should be if nothing was ever 
missing (since arrays start at index 0).

Step-by-Step Dry Run Example:

Let's trace: arr = [2, 3, 4, 7, 11] and k = 5 (We want the 5th missing number).
Initial Setup:l = 0 (left pointer at index 0)h = 4 
(right pointer at index 4, the last index)
k = 5
Iteration 1:Find mid:
mid = (0 + 4) // 2 = 2
arr[2] is 4.

Calculate missing_count:
$$\text{missing\_count} = \text{arr}[2] - (2 + 1) = 4 - 3 = 1
$$(Only 1 number is missing so far: 1)Compare with k:
Is missing_count (1) < k (5)? Yes!This means we haven't found enough missing 
numbers yet. 
We need to look further to the right.
Update pointer:$$l = \text{mid} + 1 = 3$$Iteration 2:Current state: l = 3, h = 4, k = 5
Find mid:$$\text{mid} = (3 + 4) // 2 = 3$$arr[3] is 7.
Calculate missing_count:$$\text{missing\_count} = \text{arr}[3] - (3 + 1) = 7 - 4 = 3$$
(3 numbers are missing so far: 1, 5, 6)

Compare with k:Is missing_count (3) < k (5)? Yes! Still not enough missing numbers. 
Look right.Update pointer:$$l = \text{mid} + 1 = 4$$
Iteration 3:Current state: l = 4, h = 4, k = 5
Find mid:$$\text{mid} = (4 + 4) // 2 = 4$$arr[4] is 11.
Calculate missing_count:$$\text{missing\_count} = \text{arr}[4] - (4 + 1) = 11 - 5 = 6
(6 numbers are missing so far: 1, 5, 6, 8, 9, 10)

Compare with k:Is missing_count (6) < k (5)? No!This means we've overshot our target. 
The 5th missing number hides before index 4. We need to look to the left.
Update pointer:$$h = \text{mid} - 1 = 3

End of Loop:
Now l = 4 and h = 3.

The condition l <= h (4 <= 3) is False, so the loop stops.

The Final Answer (l + k):
l ends up at 4.

We return l + k 
→ 4 + 5 = 9.

Output: 9 (The 5th missing number is indeed 9).
'''