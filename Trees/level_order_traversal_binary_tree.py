'''
Binary Tree Level Order Traversal:
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        queue = [[root]]
        ans = []
        while queue:
            currentlvl = queue.pop()
            nodes = []
            nextlvl = []
            for i in currentlvl:
                if i:
                    nodes.append(i.val)
                    nextlvl.extend([i.left,i.right])
            if nextlvl:
                queue.append(nextlvl)
                ans.append(nodes)
            elif nodes:
                ans.append(nodes)
                
        return ans