'''Given the roots of two binary trees p and q, write a function 
to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
def sameTree(p : TreeNode ,q : TreeNode) -> bool:
    if not p and not q:
        return True #2 two empty(Null) trees are technically identical
    if not p or not q or p.val!=q.val: # If any one tree is empty and the oth is not
        return False      # or the values of their root nodes are not equal

    return sameTree(p.left,q.left) and sameTree(p.right,q.right)

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

# Cosntructing Tree 1 
#                  / \
#                 2   3   

tree0=TreeNode(1,TreeNode(2),TreeNode(3))
tree1=TreeNode(1,TreeNode(2),TreeNode(3))
print(sameTree(tree0,tree1))    

# Cosntructing Tree 1 
#                  / \
#                 2   4
tree2=TreeNode(1,TreeNode(2),TreeNode(4))
print(sameTree(tree0,tree2))    

#BT Using Adj list
from collections import defaultdict
class Binary_Tree_Node:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.left=None
        self.right=None
        self.adj=defaultdict(list)

    def add_node(self,parent,child):
        #(parent) ->  (child)
        self.adj[parent].append(child)

tree=Binary_Tree_Node("X")
tree.add_node("X","Y")
tree.add_node("X","Z")
tree.add_node("Y","A")
tree.add_node("Y","B")
