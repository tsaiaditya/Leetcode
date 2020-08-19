'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        visited = list()
        while head:
            if head.val not in visited:
                visited.append(head.val)
            head = head.next
        fin = ListNode(0)
        cur = fin
        for i in visited:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return fin.next