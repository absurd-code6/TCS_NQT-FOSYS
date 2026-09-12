'''LeetCode #26
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears 
only once. The relative order of the elements should be kept the same.
'''
def Remove_Duplicates(nums):
  j=1
  for i in range(1,len(nums)):
     if nums[i] != nums[i-1]:
          nums[j]=nums[i]
          j+=1
  return arr[:j]

print("Enter the duplicate array:")
arr=list(map(int, input().split()))
ans=Remove_Duplicates(arr)
for i in len(arr):
    print(i)     

''' This code solves a classic problem: removing duplicate 
numbers from a sorted list in-place (meaning we modify the 
original list without creating a new one) and returning the length 
of the list with unique numbers.'''

'''Here is the step-by-step dry run for nums = [8, 7, 8, 6].
If [8, 7, 8, 6] is sorted first -> [6, 7, 8, 8]$: Duplicate values are adjacent, 
so duplicates are removed correctly

Step-by-Step Execution:
Step 1: i = 1Current Element nums[1]: 7
Previous Element nums[0]: 6 Condition Check: Is nums[1] != nums[0]?->7!=6 (True)
Action:Copy nums[1] to index j: nums[1] = 7 Increment j: j becomes 2 
Array State: [6, 7, 8, 8] Step 2: i = 2 Current Element nums[2]: 8 Previous Element nums[1]: 7Condition Check: Is nums[2] != nums[1]?->8!=7$ (True) 
Action:Copy nums[2] to index j: nums[2] = 8 Increment j: j becomes 3 
Array State: [6, 7, 8, 8] 
Step 3: i = 3 Current Element nums[3]: 8 Previous Element nums[2]: 8 
Condition Check: Is nums[3] != nums[2]?->8!=8 is False
Action: Do nothing (it's a duplicate!).

Array State: [6, 7, 8, 8]

return arr[:j]=arr[:3]=[6,7,8]
'''
#Using set
arr = list(map(int, input().split()))
# sorted() removes duplicates and explicitly sorts the result
print(sorted(set(arr)))

#Pythonic Approach (Returns a new list)
def remove_duplicates(arr):
    # dict.fromkeys preserves order while removing duplicates
    return list(dict.fromkeys(arr))

# Example usage:
nums = [1, 1, 2, 2, 3, 4, 4, 5]
unique_nums = remove_duplicates(nums)

print("Original:", nums)
print("Unique:  ", unique_nums)
