from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:

            return True

        def compareSubTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False
            return compareSubTree(p.left, q.right) and compareSubTree(p.right, q.left)

        return compareSubTree(root.left, root.right)
