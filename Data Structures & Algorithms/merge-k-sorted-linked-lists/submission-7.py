# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                li1 = lists[i]
                li2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(li1, li2))
            lists = merged_lists
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        dummy = new_li = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                new_li.next = list1
                list1 = list1.next
            else:
                new_li.next = list2
                list2 = list2.next
            new_li = new_li.next
        new_li.next = list1 or list2
        return dummy.next