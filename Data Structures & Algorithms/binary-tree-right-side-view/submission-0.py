# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # [1], [2,3] [4,5]
        # remove layer from q
        # append the rightmost value in that layer

        if root is None:
            return []
        
        res = []

        q = deque([root])

        while q:
            lvl = []

            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(lvl[-1])


        return res
        


        
        