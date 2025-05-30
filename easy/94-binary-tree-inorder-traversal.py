from typing import Optional


# Definition for a binary tree node.
# uncomment before submitting
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res: list[int] = [root.val]
        return (
            self.inorderTraversal(root.left) + res + self.inorderTraversal(root.right)
        )
