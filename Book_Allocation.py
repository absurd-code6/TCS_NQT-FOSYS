'''Given an array nums of n integers, where nums[i] represents the 
number of pages in the i-th book, and an integer m representing 
the number of students, allocate all the books to the 
students so that each student gets at least one book, 
each book is allocated to only one student, and the allocation is contiguous.

Allocate the books to m students in such a way that the 
maximum number of pages assigned to a student is minimized. 
If the allocation of books is not possible, return -1.
Example 1

Input: nums = [12, 34, 67, 90], m=2

Output: 113

Explanation: The allocation of books will be 12, 34, 67 | 90. 
One student will get the first 3 books and the other will get the last one.

Example 2

Input: nums = [25, 46, 28, 49, 24], m=4

Output: 71

Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.
'''
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

print(allocateMinPages([25,46,28,49,24],4))
