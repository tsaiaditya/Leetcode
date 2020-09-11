'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        if not root:
            return 0
        def traverse(r,arr):
            if not r:
                return
            traverse(r.left,arr)
            arr.append(r.val)
            traverse(r.right,arr)
        traverse(root,arr)
        diff = 10**20
        for i in range(len(arr)-1): 
            if arr[i+1] - arr[i] < diff: 
                diff = arr[i+1] - arr[i] 
        return diff 