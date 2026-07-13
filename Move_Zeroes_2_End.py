'''Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
# Read the number of elements (not strictly needed, but given in input)
n = int(input().strip())

# Read the array elements as a list of integers
nums = list(map(int, input().split()))

# Pointer to track where the next non-zero element should go
insert_pos = 0

# Iterate through the list
for i in range(len(nums)):
    if nums[i] != 0:
        # Swap the non-zero element with the element at insert_pos
        nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
        insert_pos += 1

# Print the final list elements separated by spaces
print(*nums)

#Wrong Way to do it
'''def move_zeroes(nums):
    count=0
    for i in nums:
        if i==0:
            count+=1
            nums.remove(0)
    for j in range(count):
        nums.append(0)
    return nums'''
#This code works for some inputs, but it has a hidden bug that 
# will cause it to skip zeroes if they are right next 
# to each other (like [0, 0, 1])
#When you call nums.remove(0) inside a for i in nums: 
# loop, you are mutating (changing) the list while 
# iterating over it. 
# This shifts all the elements to the left, which throws off 
# Python's internal  index pointer.
'''For example, if you have [0, 0, 1]:

The loop looks at index 0 (which is 0), removes it, and count 
becomes 1.The list is now [0, 1].Next, the loop moves to index 1. 
But because the list shifted, index 1 is now 1. 
The second zero at index 0 got completely skipped.
remove(0) has to search the list from the beginning every 
single time it runs. This provided approach touches each element 
exactly once, making it significantly faster for large inputs.'''
#Dry Run
'''Step-by-Step Execution
i = 0: nums[0] is 0.

Condition nums[0] != 0 is False. Skip the swap.

Array State: [0, 1, 0, 3, 12] | insert_pos = 0

i = 1: nums[1] is 1.

Condition nums[1] != 0 is True.

Swap nums[insert_pos] (index 0) and nums[i] (index 1).

nums[0], nums[1] = nums[1], nums[0] (0 and 1 trade places).

insert_pos increments to 1.

Array State: [1, 0, 0, 3, 12] | insert_pos = 1

i = 2: nums[2] is 0.

Condition nums[2] != 0 is False. Skip the swap.

Array State: [1, 0, 0, 3, 12] | insert_pos = 1

i = 3: nums[3] is 3.

Condition nums[3] != 0 is True.

Swap nums[insert_pos] (index 1) and nums[i] (index 3).

nums[1], nums[3] = nums[3], nums[1] (0 and 3 trade places).

insert_pos increments to 2.

Array State: [1, 3, 0, 0, 12] | insert_pos = 2

i = 4: nums[4] is 12.

Condition nums[4] != 0 is True.

Swap nums[insert_pos] (index 2) and nums[i] (index 4).

nums[2], nums[4] = nums[4], nums[2] (0 and 12 trade places).

insert_pos increments to 3.

Array State: [1, 3, 12, 0, 0] | insert_pos = 3

Final Result
The loop finishes because it reached the end of the list.

nums is now [1, 3, 12, 0, 0].'''