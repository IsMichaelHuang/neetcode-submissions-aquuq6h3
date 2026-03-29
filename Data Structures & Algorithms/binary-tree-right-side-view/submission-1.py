# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        