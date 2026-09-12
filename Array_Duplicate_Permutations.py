#What if the input array contains duplicates? 
''' When the input array contains duplicates—for example, 
arr = [1, 1, 2]—our previous logic hits a massive roadblock.

If you use the previous code, two things go wrong:

The duplicate check breaks: The line if i in current_path: continue will completely break down because 
the algorithm won't be able to 
distinguish between the first 1 and the second 1. 
It will think you're trying to reuse the same exact element.

We get duplicate permutations: Even if we bypass that, 
we will end up generating identical paths (e.g., listing [1, 1, 2] 
multiple times), which interviewers do not want.

To fix this, we need to sort the array first and 
track elements by their unique positions (indices) 
rather than their values.

The Mental Blueprint for Duplicates
Imagine you have three blocks: [1a, 1b, 2]. 
They look identical to the naked eye, 
but they are in different positions.

To avoid generating the same permutation twice, 
we follow a golden rule: Never start a branch with a 
duplicate number if its twin was already used at this exact same level.

If we sort the array, identical numbers will 
sit right next to each other. As we loop through 
the numbers to pick our next choice, we can look backward. 
If the current number is the same as the previous number 
(arr[i] == arr[i-1]), and the previous number is not 
currently being used in our path, it means that branch was 
already fully explored. We must skip it.

The Code Implementation
Instead of checking if i in current_path, we use a 
companion list called visited (filled with True/False) 
to track exactly which indices we have picked. '''

def Unique_Permute(arr,permutations):
    arr.sort()
    def backtrack(current_path):
      if len(current_path)==len(arr):
          permutations.append(list(current_path))
          return
      visited=[False]*len(arr)
      for i in range(len(arr)):
          if visited[i]:
              continue
          if i>0 and arr[i]==arr[i-1] and not visited[i-1]:
              continue
          #CARDINAL RULE FOR DUPLICATES:
            # If this number is the same as the previous one, AND the previous
            # one is NOT being used right now, skip it to avoid a duplicate branch.
          visited[i]=True
          current_path.append(arr[i])
          backtrack(current_path)
          #Undo choice (Backtrack)
          visited[i]=False
          current_path.pop()
    backtrack([])
    return permutations
print(Unique_Permute([1,2,1],[])) 
          
          