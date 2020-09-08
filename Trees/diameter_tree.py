'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Approach:
The first solution comes from here which helps to get the intuition easier. 
You need to return one of the tree cases: 
    1) if the left subtree has the longest path 
    2) if the right subtree has the longest path
    3) if the longest path goes through root.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.diameter(root)
        return self.res
    
    def diameter(self, root):
        if root is None:
            return 0
        
        left_path = self.diameter(root.left)
        right_path = self.diameter(root.right)
        self.res = max(self.res, left_path + right_path)
        
        return max(left_path, right_path)+1