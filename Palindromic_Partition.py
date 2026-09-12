#Backtracking Problem
'''Given a string S, partition S such that every string of the 
partition is a palindrome. Print all possible palindrome partitioning 
of S. A single character is also considered palindromic.'''

def partition(s,partitions):
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
    for line in partitions:
        #print(line)
        print(" ".join(line))

#if __name__=="__main__":
s=input()
partitions=[]
partition(s,partitions)        
print(partitions)


'''This code solves the palindrome partitioning problem using 
backtracking (DFS). The idea is to try every possible way 
to split the string and only keep those splits where every 
substring is a palindrome.

🔧 How the code works
1. Palindrome check
def isPal(sub):
    return sub == sub[::-1]
Checks if a substring is equal to its reverse.
2. Backtracking function
def backtrack(start, path):
start: current index in string s
path: list of substrings chosen so far
3. Base case
if start == len(s):
    v.append(" ".join(path))
    return
If we've reached the end of the string, we found a valid partition.
Add it to result list v.
4. Try all partitions
for end in range(start+1, len(s)+1):
    sub = s[start:end]
Try every substring starting at start.
5. Choose only palindromes
if isPal(sub):
    path.append(sub)
    backtrack(end, path)
    path.pop()
If substring is palindrome:
Add to path
Recurse for remaining string
Backtrack (remove last choice)
🧪 Dry Run Example

Let's take:

s = "aab"
Step-by-step recursion tree:
Start:
backtrack(0, [])
🔹 First level choices:
1. sub = "a" (0:1) ✅ palindrome
path = ["a"]
backtrack(1, ["a"])
🔹 Second level:
1. sub = "a" (1:2) ✅
path = ["a", "a"]
backtrack(2, ["a", "a"])
🔹 Third level:
1. sub = "b" (2:3) ✅
path = ["a", "a", "b"]
backtrack(3, ["a", "a", "b"])

Now:

start == len(s)
→ add "a a b" to result

Backtrack:

path = ["a", "a"]

Backtrack again:

path = ["a"]
2. sub = "ab" (1:3) ❌ not palindrome → skip

Backtrack:

path = []
🔹 First level (continue):
2. sub = "aa" (0:2) ✅
path = ["aa"]
backtrack(2, ["aa"])
🔹 Next:
sub = "b" (2:3) ✅
path = ["aa", "b"]
backtrack(3, ["aa", "b"])

Add:

"aa b"

Backtrack:

path = []
3. sub = "aab" ❌ not palindrome
✅ Final Output:
a a b
aa b
🧠 Key Insight
The algorithm explores all possible partitions
It prunes early by rejecting non-palindromes
Uses backtracking to efficiently explore combinations'''
