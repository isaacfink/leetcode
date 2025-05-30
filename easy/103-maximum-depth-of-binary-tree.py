from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], cur: int = 0) -> int:
        if root is None:
            return cur

        return max(
            self.maxDepth(root.left, cur=cur + 1),
            self.maxDepth(root.right, cur=cur + 1),
        )
