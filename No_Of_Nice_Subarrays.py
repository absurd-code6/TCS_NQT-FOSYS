'''Given an array of integers nums and an integer k. A continuous subarray 
is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''
def Nice_Subarray(arr,k):
    if not arr:
             return -1
    def atMost(k):
        if k<0:
            return 0
        l = 0
        cur_sum = 0
        total_subarrays = 0
        for r in range(len(arr)):
            cur_sum+=(arr[r]%2)
            while cur_sum>k:
                cur_sum-=(arr[l]%2)
                l+=1
            total_subarrays += (r - l + 1)
        return total_subarrays
    
    return atMost(k) - atMost(k - 1)    

arr=list(map(int,input().split()))
k=int(input())
print(Nice_Subarray(arr,k))

