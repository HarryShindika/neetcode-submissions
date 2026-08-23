# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS, using a queue

        # while queue, 

        res = []

        q = deque([root])

        while q:
            num = len(q)
            lvl = []

            while num > 0:
                
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                num -= 1

            if lvl:
                res.append(lvl)

        return res




