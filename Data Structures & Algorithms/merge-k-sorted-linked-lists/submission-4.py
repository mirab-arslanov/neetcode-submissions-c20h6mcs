# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        dummy = new_li = ListNode()
        while any(lists):
            min_node = (ListNode(val=1001), 1488)
            for i, curr_node in enumerate(lists):
                if not curr_node:
                    continue
                min_node = (curr_node, i) if curr_node.val < min_node[0].val else min_node
            new_li.next = min_node[0]
            lists[min_node[1]] = lists[min_node[1]].next
            new_li = new_li.next

        return dummy.next