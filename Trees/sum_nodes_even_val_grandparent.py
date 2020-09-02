'''
Problem number: 1315 - refer the example for tree there.
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes = []
        def dfs(r,nodes):
            if not r:
                return
            if not r.val&1:
                if r.left:
                    if r.left.left:
                        nodes.append(r.left.left.val)
                    if r.left.right:
                        nodes.append(r.left.right.val)
                if r.right:
                    if r.right.left:
                        nodes.append(r.right.left.val)
                    if r.right.right:
                        nodes.append(r.right.right.val)
            dfs(r.left,nodes)
            dfs(r.right,nodes)
        
        dfs(root,nodes)
        return sum(nodes)