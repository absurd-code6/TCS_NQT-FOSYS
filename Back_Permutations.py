'''Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''
def Permutations(nums:list[int])->list[list[int]]:
    if len(nums)==1:
        return [nums.copy()]
    res=[]
    for i in range(len(nums)):
        n=nums.pop(0)
        perms=Permutations(nums)
        for j in perms:
            j.append(n)
        res.extend(perms)
        nums.append(n)
    return res

print(Permutations([1,2,3]))

'''Step-by-Step Logic
Pick & Remove: Take the first element out of the current list.

Delegate (Recurse): Find all permutations of the remaining elements.

Attach: Add the removed element to the end of each resulting sub-permutation.

Restore (Backtrack): Put the removed element back at the end of the 
original list so the loop can pick the next number in line.'''
#Dry Run
'''Level 1: Initial Call → Permutations([1, 2, 3])nums = [1, 2, 3], 
res = []Iteration $i = 0$:n = nums.pop(0) -> removes 1. nums is now [2, 3].
Calls perms = Permutations([2, 3]) -> (Jumps to Level 2)

Level 2: Sub-call → Permutations([2, 3])nums = [2, 3], res = []
Iteration $i = 0$:n = nums.pop(0) -> removes 
2. nums is now [3].Calls perms = Permutations([3]) -> Base Case Hit! 
Returns [[3]]. perms = [[3]].
Loop over perms: append 2 to [3], making it [3, 2].
res.extend([[3, 2]]) -> res = [[3, 2]].
nums.append(2) -> nums restored to [3, 2].

Iteration $i = 1$:n = nums.pop(0) -> removes 3. 
nums is now [2].
Calls perms = Permutations([2]) -> Base Case Hit! 
Returns [[2]].perms = [[2]].
Loop over perms: append 3 to [2], making it [2, 3].
res.extend([[2, 3]]) -> res = [[3, 2], [2, 3]].
nums.append(3) -> nums restored to [2, 3].
Level 2 Finish: Returns [[3, 2], [2, 3]] back to Level 1.

Back to Level 1: Permutations([1, 2, 3])Iteration $i = 0$ 
(continued):perms = [[3, 2], [2, 3]], n = 1.
Append 1 to each list in perms: [[3, 2, 1], [2, 3, 1]].
res.extend(...) -> res = [[3, 2, 1], [2, 3, 1]].
nums.append(1) -> nums becomes [2, 3, 1].

Iteration $i = 1$:n = nums.pop(0) -> removes 2. 
nums is now [3, 1].
Calls Permutations([3, 1]) -> through similar steps, 
returns [[1, 3], [3, 1]].
Append 2 to each item: [[1, 3, 2], [3, 1, 2]].
res.extend(...) -> res = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2]].
nums.append(2) -> nums becomes [3, 1, 2].

Iteration i = 2:n = nums.pop(0) -> removes 3. 
nums is now [1, 2].
Calls Permutations([1, 2]) -> returns [[2, 1], [1, 2]].
Append 3 to each item: [[2, 1, 3], [1, 2, 3]].
res.extend(...) -> res = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], 
[2, 1, 3], [1, 2, 3]].
nums.append(3) -> nums restored back to original order [1, 2, 3].

'''