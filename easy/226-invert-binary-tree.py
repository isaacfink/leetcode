from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root: Optional[TreeNode]):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            invert(root.left)
            invert(root.right)

        invert(root)
        return root
