from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        found = set()
        while node is not None:
            if node in found:
                return True
            found.add(node)
            node = node.next
        return False
