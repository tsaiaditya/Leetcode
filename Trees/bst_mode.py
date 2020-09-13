'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        seen = dict()
        if not root:
            return []
        def traverse(r,seen):
            if not r:
                return
            if r.val not in seen:
                seen[r.val] = 1
            else:
                seen[r.val] += 1
            traverse(r.left,seen)
            traverse(r.right,seen)
        traverse(root,seen)
        maxval,arr = sorted(seen.items(),key = lambda x:x[1], reverse = True)[0][1],list()
        for i,j in seen.items():
            if j == maxval:
                arr.append(i)
        return arr