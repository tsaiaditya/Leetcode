'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        arr = self.sub_sum(temp)
        curr = dummy= ListNode(-1)        
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        
    def sub_sum(self, arr):
        summ = 0
        d = {}
        d[0] = -1
        
        for i in range(len(arr)):
            summ += arr[i]
            if summ in d:
                t = d[summ]
                return self.sub_sum(arr[:t+1] + arr[i+1:])
            
            d[summ] = i
        return arr