from typing import Optional


# Definition for singly-linked list.
# uncomment when submitting
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        node = self
        while node:
            res.append(str(node.val))
            node = node.next
        return " -> ".join(res)


def array_to_linked_list(arr: list[int]):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


class Solution:
    @staticmethod
    def node_to_int(node: ListNode):
        cur_node = node
        multiplier = 1
        res = 0
        while cur_node:
            res += cur_node.val * multiplier
            multiplier *= 10
            cur_node = cur_node.next
        return res

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        res = self.node_to_int(l1) + self.node_to_int(l2)
        arr = list(str(res))
        self.cur = ListNode(val=int(arr[0]))
        for i in arr[1::]:
            node = ListNode(val=int(i), next=self.cur)
            self.cur = node
        return self.cur


sol = Solution()
print(
    sol.addTwoNumbers(array_to_linked_list([2, 4, 3]), array_to_linked_list([5, 6, 4]))
)  # Expected: 7 -> 0 -> 8

print(sol.addTwoNumbers(ListNode(0), ListNode(0)))  # Expected: 0
print(
    sol.addTwoNumbers(
        array_to_linked_list([9, 9, 9, 9, 9, 9, 9]), array_to_linked_list([9, 9, 9, 9])
    )
)  # Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
