# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            # Both nodes are None -> identical structural end
            if not r1 and not r2:
                return True
            # One node is None or values differ -> not identical
            if not r1 or not r2 or r1.val != r2.val:
                return False
            # Recursively check both left and right children
            return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)

        # Base cases
        if not subRoot:
            return True
        if not root:
            return False

        # If current trees match, return True; otherwise check left/right subtrees
        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)