'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        h1 = ListNode(0)
        t = h1
        x = Counter(arr)
        fin = [i for i,j in x.items() if j == 1]
        for i in fin:
            t.next = ListNode(i)
            t = t.next
        return h1.next