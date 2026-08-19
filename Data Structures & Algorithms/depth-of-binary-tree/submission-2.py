# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


        # Time Complexity: $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited exactly once.
        
        # Space Complexity: $O(H)$, where $H$ is the height of the tree, representing the recursion stack depth. In the worst case (unbalanced tree), $H = O(N)$; in the best/balanced case, $H = O(\log N)$.