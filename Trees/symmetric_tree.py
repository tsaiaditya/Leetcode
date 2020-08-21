'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(r1,r2):
            if r1 is None and r2 is None:
                return True
            if r1 is not None and r2 is not None:
                if r1.val == r2.val:
                    return (mirror(r1.right,r2.left) and mirror(r1.left,r2.right))
        return mirror(root,root)