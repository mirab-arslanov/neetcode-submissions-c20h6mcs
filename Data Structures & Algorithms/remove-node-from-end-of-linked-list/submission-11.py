# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(next=head)
        left, right = dummy, head
        counter = 0
        while right:
            right = right.next
            counter += 1
        counter = counter - n
        while counter != 0:
            left = left.next
            counter -= 1
            # right = right.next
        left.next = left.next.next
        return dummy.next

        