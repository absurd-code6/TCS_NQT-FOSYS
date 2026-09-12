'''Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted 
in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
def Sqaures_Arr(nums):
    res=[]
    n=len(nums)
    left=0
    right=n-1
    while left<=right:
        if nums[left]**2 > nums[right]**2:
            res.append(nums[left]**2)
            left+=1
        else:
            res.append(nums[right]**2)
            right-=1
#Currently the res contains the largest elements followed by 
#the smallest ones
    return res[::-1]
#We need to reverse the array to maintain the sorted(non-decreasing)order

nums=list(map(int,input().split()))
print(Sqaures_Arr(nums))
