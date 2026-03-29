# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        def helper(tree):
            if not tree:
                return 0
            
            left = helper(tree.left)
            right = helper(tree.right)
            
            # The sub left || right branch is not balance or the current iteration is not balance
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # Return the height of the tree
            return 1 + max(left, right)
        
        return helper(root) != -1

