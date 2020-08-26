'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum1: int) -> List[List[int]]:
        self.ans = []
        def helper(root,sum1,arr):
            if not root:
                return []
            if not root.left and not root.right and sum1-root.val==0:
                self.ans.append(arr+[root.val])
            l = helper(root.left,sum1-root.val,arr+[root.val])
            r = helper(root.right,sum1-root.val,arr+[root.val])
            return l and r
        helper(root,sum1,[])
        return self.ans