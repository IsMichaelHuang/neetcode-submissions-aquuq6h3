# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(tree):
            if not tree:
                return 0

            left = helper(tree.left) 
            right = helper(tree.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        helper(root)
        return self.res

        