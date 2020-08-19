'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        stk = [[root]]
        ans = []
        while stk:
            currentlvl = stk.pop()
            nodes = []
            nextlvl = []
            for i in currentlvl:
                if i:
                    nodes.append(i.val)
                    nextlvl.extend([i.left,i.right])
            if nextlvl:
                stk.append(nextlvl)
                ans.append(nodes)
            elif nodes:
                ans.append(nodes)
                
        for i,j in enumerate(ans):
            if i&1:
                ans[i] = j[::-1]
            else:
                continue
                
        return ans