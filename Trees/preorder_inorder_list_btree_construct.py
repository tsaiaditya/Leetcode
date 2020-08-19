'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        def preAndInorder(preorder,inorder):
            if len(preorder)==0 and len(inorder)==0:
                return None
            elif len(preorder)==1 and len(inorder)==1:
                return TreeNode(preorder[0])
            else: 
                root=TreeNode(preorder[0])
                inorderLeftTreeList=inorder[0:inorder.index(root.val)]
                inorderRightTreeList=inorder[inorder.index(root.val)+1:]
                preorderLeftTreeList=preorder[1:1+len(inorderLeftTreeList)]
                preorderRightTreeList=preorder[1+len(inorderLeftTreeList):]
                root.left=preAndInorder(preorderLeftTreeList,inorderLeftTreeList)
                root.right=preAndInorder(preorderRightTreeList,inorderRightTreeList)
                return root
        return preAndInorder(preorder,inorder)