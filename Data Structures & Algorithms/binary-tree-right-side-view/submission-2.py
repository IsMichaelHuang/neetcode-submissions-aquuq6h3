# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        if not root:
            return []

        self.right = []
        def helper(node, level):
            if not node:
                return
            
            if level == len(self.right):
                self.right.append(node.val)
            
            helper(node.right, 1 + level)
            helper(node.left, 1 + level)

        helper(root, 0)
        return self.right
        """
        res = []
        queue = collections.deque([root])

        while queue:
            right_side = None
            q_len = len(queue)

            for _ in range(q_len):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res
        