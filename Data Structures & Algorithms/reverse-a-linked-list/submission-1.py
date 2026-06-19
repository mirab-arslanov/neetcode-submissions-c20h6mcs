# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head:
            return head
        rev_li = ListNode(val=head.val)
        curr = head.next
        while curr:
            rev_li = ListNode(val=curr.val, next=rev_li)
            curr = curr.next
        return rev_li
