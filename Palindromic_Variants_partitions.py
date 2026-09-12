'''1. The "Count Only" VariationThe Prompt: "Given a string s 
return the number of valid palindrome partitions, rather than the 
partitions themselves."'''

def Pal_Count(s):
    def isPalindrome(sub):
        return sub==sub[::-1]
    def backtrack(start):
     if start==len(s):
        return 1
     count=0
     for i in range(start+1,len(s)+1):
         sub=s[start:i]
         if isPalindrome(sub):
             count+=backtrack(i)
     return count
    return backtrack(0)
#OR
#Instead of passing a path list and mimicking a knife slicing the 
# string, you change the function to return an integer. 
# You don't need path.append() or path.pop() anymore, 
# which optimizes space.

'''def partition(s,partitions):
    def isPalindrome(sub):
       return sub==sub[::-1]
    def backtrack(start,path):
        if start==len(s):
            partitions.append(path[:]) #partitions.append("".join(path))
            return
        for end in range(start+1,len(s)+1):
            sub=s[start:end]
            if isPalindrome(sub):
                path.append(sub)
                backtrack(end,path)
                path.pop()
    backtrack(0,[])
    count=0
    for i in partitions:
        count+=1
    print(count)'''

    
if __name__=="__main__":
    s=str(input("Enter a string:"))
    print(Pal_Count(s))   

'''If an interviewer asks you to find all unique combinations of 
palindromes, standard Python lists ([]) won't help you 
filter duplicates automatically. Here is the breakdown of 
why we convert the path to a tuple and store it in a 
set:Lists are Mutable (Unhashable): 

In Python, 
you cannot add a regular list directly into a set ({}). 
Sets require their elements to be immutable and "hashable" s
o they can guarantee uniqueness. 

A tuple () is simply an 
immutable version of a list, making it perfectly safe for a set.
Order Matters vs. Order Doesn't Matter: * 
If the interviewer says: 

"The order of elements in the partition matters, 
but I want to avoid duplicate identical paths" $\rightarrow$ we use tuple(path).If the interviewer says: "The order doesn't matter, ['a', 'aa'] is the same combination as ['aa', 'a']
" $\rightarrow$ we use tuple(sorted(path)).Below, we 
will implement the variation where order matters 

but we want to filter out duplicate paths (which often happens if the input string itself contains repeating identical characters, like "aaaa").

def unique_palindrome_partitions(s):
    # A set to store unique partitions automatically
    partitions = set()

    def isPalindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            # Convert the list 'path' to an immutable tuple so it can be added to the set
            partitions.add(tuple(path))
            return
        
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if isPalindrome(sub):
                path.append(sub)        # Choose
                backtrack(end, path)    # Explore
                path.pop()              # Un-choose (Backtrack)

    # Start the backtracking process
    backtrack(0, [])
    
    # Convert the set of tuples back into a list of lists for standard output format
    return [list(p) for p in partitions]


if __name__ == "__main__":
    # Example using a string with heavy duplicates to show the set in action
    sample_string = "aaa"
    result = unique_palindrome_partitions(sample_string)
    
    print(f"Unique partitions for '{sample_string}':")
    for partition in result:
        print(partition)'''
