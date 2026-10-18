'''Given a binary array nums and an integer goal, return the number of 
non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4

Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
'''
def Binary_Subarray_Sum(arr:list[int],k:int)->int:
 if not arr:
         return -1
 def atMost(k):
    
    if k<0:
        return 0
    l = 0
    cur_sum = 0
    total_subarrays = 0
    for r in range(len(arr)):
        cu_sum+=arr[r]
        while cur_sum>k:
            cur_sum-=arr[l]
            l+=1
        total_subarrays += (r - l + 1)
    return total_subarrays

 return atMost(k) - atMost(k - 1)    

