# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = 0
        self.kth = 0
        def dfs(node):
            if not node:
                return
            
            if self.kth:
                return self.kth
            
            dfs(node.left)
            self.k += 1
            if self.k == k: 
                self.kth = node.val
            
            dfs(node.right)
        
        dfs(root)
        return self.kth

        