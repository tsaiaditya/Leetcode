'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

As of 11 - 09 - 2020:
Runtime: 20 ms, faster than 99.62% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 20.84% of Python3 online submissions for Binary Tree Paths.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        arr,num = list(),""
        def dfs(r,arr,num):
            if not r:
                return
            if not num:
                num = str(r.val)
            else:
                num+='->'+str(r.val)
            if not r.left and not r.right:
                arr.append(num)
            dfs(r.left,arr,num)
            dfs(r.right,arr,num)
        dfs(root,arr,num)
        return arr

