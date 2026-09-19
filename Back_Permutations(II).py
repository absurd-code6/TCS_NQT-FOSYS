'''Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
def duplicatePermutations(nums):
    res=[]
    perms=[]
    count={n:0 for n in nums}
    for n in nums:
        count[n]+=1
    def dfs():
        if len(perms)==len(nums):
            res.append(perms.copy())
            return
        for n in count:
            if count[n]>0:
                perms.append(n)
                count[n]-=1
                dfs()
                count[n]+=1
                perms.pop()
    dfs()
    print(res)

duplicatePermutations([1,1,2])

'''Step-by-Step Dry Run for duplicatePermutations([1, 1, 2])
Initial State:

nums = [1, 1, 2]

count = {1: 2, 2: 1}

perms = []

Step 1: Pick first element

We run dfs(). perms length is 0.

We check key 1: count is 2 > 0.

Pick 1: perms = [1], count = {1: 1, 2: 1}.

Call dfs() recursively.

Step 2: Pick second element

Inside dfs(). perms length is 1.

We check key 1: count is 1 > 0.

Pick 1: perms = [1, 1], count = {1: 0, 2: 1}.

Call dfs() recursively.

Step 3: Pick third element

Inside dfs(). perms length is 2.

Check key 1: count is 0 (skip).

Check key 2: count is 1 > 0.

Pick 2: perms = [1, 1, 2], count = {1: 0, 2: 0}.

Call dfs() recursively.

Step 4: Save first solution & Backtrack

Inside dfs(). perms length is 3 (equals len(nums)).

Append [1, 1, 2] to res. Return to Step 3.

Backtrack in Step 3: Remove 2. perms = [1, 1], count = {1: 0, 2: 1}.

Step 3 loop finishes. Return to Step 2.

Step 5: Backtrack & Try alternate branch at second position

Backtrack in Step 2: Remove 1. perms = [1], count = {1: 1, 2: 1}.

Step 2 loop continues to next key 2: count is 1 > 0.

Pick 2: perms = [1, 2], count = {1: 1, 2: 0}.

Call dfs() recursively.

Step 6: Pick third element for second branch

Inside dfs(). perms length is 2.

Check key 1: count is 1 > 0.

Pick 1: perms = [1, 2, 1], count = {1: 0, 2: 0}.

Call dfs() recursively.

Step 7: Save second solution & Backtrack

Inside dfs(). perms length is 3.

Append [1, 2, 1] to res. Return to Step 6.

Backtrack: Remove 1. perms = [1, 2], count = {1: 1, 2: 0}.

Step 6 loop continues to key 2: count is 0 (skip).

Step 6 finishes. Return to Step 5.

Backtrack in Step 5: Remove 2. perms = [1], count = {1: 2, 2: 1}.

Step 1 loop finishes its check for key 1.

Step 8: Try starting with a different first element

Backtrack in Step 1: Remove 1. perms = [], count = {1: 2, 2: 1}.

Step 1 loop moves to key 2: count is 1 > 0.

Pick 2: perms = [2], count = {1: 2, 2: 0}.

Call dfs() recursively.

Step 9: Pick second element

Inside dfs(). perms length is 1.

Check key 1: count is 2 > 0.

Pick 1: perms = [2, 1], count = {1: 1, 2: 0}.

Call dfs() recursively.

Step 10: Pick third element

Inside dfs(). perms length is 2.

Check key 1: count is 1 > 0.

Pick 1: perms = [2, 1, 1], count = {1: 0, 2: 0}.

Call dfs() recursively.

Step 11: Save third solution & Clean up

Inside dfs(). perms length is 3.

Append [2, 1, 1] to res. Return to Step 10.

Backtrack through previous calls until all loops complete.'''