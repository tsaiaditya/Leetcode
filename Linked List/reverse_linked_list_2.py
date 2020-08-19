'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        m=m-1
        n=n-1
        while(m<=n):
            l[m],l[n]=l[n],l[m]
            m+=1
            n-=1
        temp=head
        for i in l:
            temp.val=i
            temp=temp.next
        return head