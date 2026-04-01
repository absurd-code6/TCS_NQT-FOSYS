'''LeetCode #26
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears 
only once. The relative order of the elements should be kept the same.
'''
def Remove_Duplicates(nums):
  j=1
  for i in (1,len(nums)):
     if nums[i] != nums[i-1]:
          nums[j]=nums[i]
          j+=j
  return j

print("Enter the duplicate array:")
arr=list(map(int, input().split()))
ans=Remove_Duplicates(arr)
for i in len(arr):
    print(i)     
