'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pa = pb = head
        i=0
        while pa:
            if i > n: 
                pb = pb.next
            pa = pa.next
            i+=1
        if i == n:
            return head.next
        if pb.next:
            pb.next = pb.next.next
        else:
            pb.next = None
        return head