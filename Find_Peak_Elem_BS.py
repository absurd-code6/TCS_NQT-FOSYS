'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index 
number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element 
is 2, or index number 5 where the peak element is 6.
'''
def Peak_Element_BS(nums):
    if not nums:
        return -1
    l=0
    h=len(nums)-1
    while l<h: #Critical! Don't use l<=h! -> Infinite Loop
        mid=(l+h)//2
        if nums[mid] < nums[mid+1]:
            l=mid+1
        else:
            h=mid
    return l

def Peak_Element_BS1(nums):
    if not nums:
        return -1
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]>nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    l=1
    h=n-2
    while l<=h:
        mid=(l+h)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid]>nums[mid-1]:
            l=mid+1
        else:
            h=mid-1
    return -1

print(Peak_Element_BS([1,2,1,3,5,6,4]))
print(Peak_Element_BS1([1,2,1,3,5,6,4]))


'''Walkthrough with Example 1: nums = [1, 2, 3, 1]
Start: l = 0, h = 3

First iteration:

mid = (0 + 3) // 2 = 1

nums[1] is 2, and nums[2] is 3.

Since 2 < 3, the ground slopes up to the right. We move l: l = mid + 1 
→ l = 2.

Second iteration:

l = 2, h = 3

mid = (2 + 3) // 2 = 2

nums[2] is 3, and nums[3] is 1.

Since 3 > 1, the ground slopes down to the right. We move h: h = mid 
→ h = 2.

Loop ends because l == h (2 == 2).

Returns 2 (which points to the value 3, our peak element).

Clean, elegant, and runs in 
O(logn) time!'''
