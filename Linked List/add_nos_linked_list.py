'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        while(l1):
            s1 += str(l1.val)
            l1 = l1.next
        s1 = s1[::-1]
        s2 = ""
        while(l2):
            s2 += str(l2.val)
            l2 = l2.next
        s2 = s2[::-1]
        res = str(eval(s1+"+"+s2))
        res = list(map(int,res[::-1]))
        # print(res)
        fin = ListNode(0)
        fin_tail = fin
        for i in res:
            fin_tail.next = ListNode(i)
            fin_tail = fin_tail.next
            
        return fin.next