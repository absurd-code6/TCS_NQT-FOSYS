'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more 
than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
#Follow-up: Could you solve the problem in linear time and in O(1) space?

from collections import defaultdict
def Majority(nums):
    n=len(nums)
    seen=defaultdict(int)
    for i in nums:
        seen[i]+=1
    for j in seen:
        if seen[j] > n//2:
            return j

nums=list(map(int,input().split()))
print(Majority(nums))

#You can also loop over key-value pairs directly using .items():
'''from collections import defaultdict
def Majority(nums):
  n = len(nums)
  seen = defaultdict(int)

  for i in nums:
    seen[i] += 1

  for element, count in seen.items():
    if count > n // 2:
      return element'''
#TC=SC=O(n)
#By Boyer-Moore Voting Algorithm (For SC=O(1))
def majorityElement(nums: list[int]) -> int:
  candidate = None
  count = 0

  for num in nums:
      # Pick a new candidate whenever count drops to 0
      if count == 0:
          candidate = num

      # Increment if same as candidate, decrement if different
      count += 1 if num == candidate else -1

  return candidate

nums=list(map(int,input().split()))
print(majorityElement(nums))