# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        self.res = 0
        def dfs(node, cur_max): 
            # Base Case
            if not node:
                return
            
            if node.val >= cur_max:
                self.res += 1
            
            new_max = max(cur_max, node.val)

            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        dfs(root, -101)
        return self.res

        