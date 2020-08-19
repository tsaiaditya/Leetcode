'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        h = head
        while h:
            arr.append(h.val)
            h = h.next
        arr1,arr2=collections.deque(),collections.deque()
        for i in range(0,len(arr)//2):
            arr1.append(arr[i])
        for i in range(len(arr)//2,len(arr)):
            arr2.append(arr[i])
        if len(arr2) != 1 and len(arr1):
            arr1.popleft()
            cur = head
            i=2
            while arr1 or arr2:
                if i&1 and arr1:
                    node = ListNode(arr1.popleft())
                    cur.next = node
                    cur = cur.next
                    i+=1
                else:
                    node = ListNode(arr2.pop())
                    cur.next = node
                    cur = cur.next
                    i+=1

        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        
        print('Answer : ')
        print(*ans,sep = '->')

s = Solution()
root = ListNode()
cur = root
arr = [1,2,3,4,5]
for i in arr:
    node = ListNode(i)
    cur.next = node
    cur = cur.next
s.reorderList(root.next)