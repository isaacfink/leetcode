from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareTrees(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
            if l is None and r is None:
                return True
            elif l is None or r is None:
                return False
            elif l.val != r.val:
                return False

            return compareTrees(l.left, r.left) and compareTrees(l.right, r.right)

        if root is None:
            return False

        return (
            compareTrees(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
