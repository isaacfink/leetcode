from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(lst: list[int]):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(node: Optional[ListNode]):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur_node, next_node = head, head.next
        head.next = None
        while next_node is not None:
            cur_temp = cur_node
            cur_node, next_node = next_node, next_node.next
            cur_node.next = cur_temp

        return cur_node


sol = Solution()

l = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(sol.reverseList(l))  # Expected: [5,4,3,2,1]
