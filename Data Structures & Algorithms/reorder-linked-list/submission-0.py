# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        h2 = slow.next
        slow.next = None
        prev = None
        while h2:
            nxt = h2.next
            h2.next = prev
            prev = h2
            h2 = nxt
        h1, h2 = head, prev
        while h2:
            tmp1, tmp2 = h1.next, h2.next
            h1.next = h2
            h2.next = tmp1
            h1, h2 = tmp1, tmp2
        
