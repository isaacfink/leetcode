from typing import Optional


# Definition for singly-linked list.
# uncomment locally for the correct types, leave it commented o ut for leetcode
class ListNode:
    val: int
    next: Optional["ListNode"]

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        return create_nodes(sorted(nodes_to_list(list1) + nodes_to_list(list2)))


def create_nodes(s: list[int]):
    if len(s) == 0:
        return None
    rev = list(reversed(s))
    last_node = ListNode(rev[0])
    if len(rev) == 1:
        return last_node
    for i in rev[1::]:
        node = ListNode(i, next=last_node)
        last_node = node
    return node


def nodes_to_list(node: Optional[ListNode]):
    res: list[int] = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res


def run(s1: list[int], s2: list[int], expected: list[int]):
    sol = Solution()
    node1 = create_nodes(s1)
    node2 = create_nodes(s2)
    final = sol.mergeTwoLists(node1, node2)
    print(f"{nodes_to_list(final)}, expected: {expected}")


run([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
run([], [], [])
run([], [0], [0])
