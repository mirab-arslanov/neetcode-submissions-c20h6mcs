# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        first, second = head, head
        counter = 0
        while first:
            counter += 1
            first = first.next
        if counter < 2:
            return
        counter = counter - n
        if counter == 0:
            return second.next
        while counter > 1:
            second = second.next
            counter -= 1
        if second.next and second.next.next:
            second.next = second.next.next
            return head
        if n == 1:
            second.next = None
            return head

        