'''Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets 
does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def three_sum(arr):
    res=[]
    arr.sort()
    for i,j in enumerate(arr):
        if i>0 and j==arr[i-1]:# the element isn't the 1st one and = prev element
            continue
        l=i+1
        r=len(arr)-1
        while l<r:
            sum=j+arr[l]+arr[r]
            if sum>0:
                r-=1
            elif sum<0:
                l+=1
            else:
                res.append([j,arr[l],arr[r]])
                l+=1
                while arr[l]==arr[l-1] and  l<r:
                    l+=1
    return res

arr=list(map(int,input().split()))
print(three_sum(arr))

#TC= O(nlogn)(for sorting) + O(n^2)(for 2 nested loops)=O(n^2)