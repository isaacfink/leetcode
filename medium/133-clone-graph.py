class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    cache = {}

    def cloneGraph(self, node: Optional["Node"], isFirst=True) -> Optional["Node"]:
        if isFirst:
            self.cache = {}
        if node is None:
            return None
        new_node = self.cache.get(node.val) or Node(val=node.val)
        found = node.val in self.cache
        self.cache[node.val] = new_node
        if not found:
            print(len(node.neighbors))
            new_node.neighbors = [
                self.cloneGraph(x, isFirst=False) for x in node.neighbors
            ]
            print(len(new_node.neighbors))

        return new_node
