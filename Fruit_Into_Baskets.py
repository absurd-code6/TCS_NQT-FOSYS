'''You are visiting a farm that has a single row of fruit trees 
arranged from left to right. The trees are represented by an 
integer array fruits where fruits[i] is the fruit_type of 
fruit the ith tree produces.

You want to collect as much fruit as possible. 
However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single fruit_type of fruit. 
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one 
fruit from every tree (including the start tree) while moving to the right. 
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your 
baskets, you must stop.
Given the integer array fruits, return the maximum number of 
fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''
#Breaking Down this problem to max length subarray with 2 fruit_types of numbers
from collections import defaultdict
def Max_Fruits(arr:list[int])->int:
    fruit_type=defaultdict(int)
    l=0
    maxlen=0
    for r in range(len(arr)):
        fruit_type[arr[r]]+=1
        while len(fruit_type)>2:
            fruit_type[arr[l]]-=1
            if fruit_type[arr[l]]==0:
               del fruit_type[arr[l]]
            l+=1
        maxlen=max(maxlen,r-l+1)
    return maxlen

n=int(input())
arr=[int(input()) for _ in range(n)]
print(Max_Fruits(arr))
#Time Complexity: O(N) — Each element is added once by r and removed 
# at most once by l.
#Space Complexity: O(1) — The dictionary holds at most 3 
# distinct keys at any given point before shrinking.
