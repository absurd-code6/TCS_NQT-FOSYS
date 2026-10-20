'''Given an array arr[] and an integer k, where the array represents the boards 
and each element denotes the length of a board, and k painters are available to 
paint these boards. Each unit length of a board takes 1 unit of time to paint. 
Find the minimum time required to paint all the boards such that each painter 
paints only contiguous sections of the array. A painter can paint boards 
like [2, 3, 4], [1], or even no board, but cannot paint non-contiguous boards 
like [2, 4, 5].

Examples:

Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The most optimal way will be: 
Painter 1 allocation : [5,10], 
Painter 2 allocation : [30], 
Painter 3 allocation : [20, 15], 
Job will be done when all painters finish i.e. at time = max(5 + 10, 30, 20 + 15) = 35

Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: The most optimal way to paint: 
Painter 1 allocation : [10, 20, 30], 
Painter 2 allocation : [40], Job will be complete at time = 60
'''

#Also known as Split Array - Largest Sum
'''(Hard)'''
'''Given an integer array nums and an integer k, split nums into k non-empty subarrays 
such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum 
among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum 
among the two subarrays is only 9.
'''
#This problem is of the same type as Allocate Minimum Pages

def countStudents(nums, pages):
    students = 1
    pages_student = 0
    for pages_in_book in nums:
        if pages_student + pages_in_book <= pages:
            pages_student += pages_in_book
        else:
            students += 1
            pages_student = pages_in_book
    return students

def allocateMinPages(nums,m):
    if len(nums)<m:
        return -1
    low=max(nums)
    high=sum(nums)
    while low<=high:
        mid=(low+high)//2
        no_of_students_req=countStudents(nums,mid)
        if(no_of_students_req>m):
            low=mid+1
        else:
            high=mid-1
    return low

def count_painters(arr,mxtime):
    '''This funcn calculates how many painters are required provided no painter is allowed
    to work more than max_time'''
    painters=1
    board_sum=0
    for i in arr:
        if board_sum+i<=mxtime:
            board_sum+=i
        else:
            painters+=1
            board_sum=i
    return painters

def Painters_mintime(arr,k):
    if not arr:
        return -1
    low=max(arr)
    high=sum(arr)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if count_painters(arr, mid) <= k:
            ans = mid        
            high = mid - 1   
        else:
            low = mid + 1    
            
    return ans

print(Painters_mintime([5, 10, 30, 20, 15],3))
print(count_painters.__doc__)
