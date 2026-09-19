'''An integer array is called arithmetic if it consists of at least 
three elements and if the difference between any two 
consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] 
and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0
'''
def Arithmetic(nums):
    if len(nums)<3:
        return 0
    cur_slices,total_slices=0,0
    for i in range(2,len(nums)):
        if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
            cur_slices+=1
            total_slices+=cur_slices
        else: cur_slices=0
    return total_slices
#TC=O(n) SC=O(1)
nums=list(map(int,input().split()))
print(Arithmetic(nums))
