'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

Your input:
[1,2,5,3,4,null,6]
Output:
[1,null,2,null,3,null,4,null,5,null,6]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = collections.deque()
    def preOrder(self,temp):
            if not temp:
                return
            self.pre.append(temp.val)
            self.preOrder(temp.left)
            self.preOrder(temp.right)
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = root
        self.preOrder(temp)
        while self.pre:
            a = self.pre.popleft()
            if temp :
                temp.val = a
                temp.left = None
                if not temp.right and self.pre:
                    temp.right = TreeNode()
            
            temp = temp.right