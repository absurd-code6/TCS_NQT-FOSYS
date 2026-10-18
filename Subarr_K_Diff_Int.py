'''Given an integer array nums and an integer k, return the number of 
good subarrays of nums.
A good array is an array where the number of different integers 
in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], 
[2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], 
[1,3,4].
'''
#Brute-Force Approach
arr=[1,2,1,2,3]
k=2
count=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        curr=arr[i:j+1]
        print(curr)
        if len(set(curr))==k:
            count+=1
print(count)

#2 Pointers Sliding-Window Approach
def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    def atMost(k: int) -> int:
        if k <= 0:
            return 0
        
        l = 0
        total_subarrays = 0
        freq = {}
        
        for r in range(len(nums)):
            # Add element to frequency map
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            
            # Shrink window until we have at most k distinct elements
            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            
            # All subarrays ending at r with start index from l to r are valid
            total_subarrays += (r - l + 1)
            
        return total_subarrays

    return atMost(k) - atMost(k - 1)

print(subarraysWithKDistinct(arr,k))
