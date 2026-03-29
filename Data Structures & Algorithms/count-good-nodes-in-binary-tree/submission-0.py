# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        self.res = 1
        def dfs(node, cur_max): 
            # Base Case
            if not node:
                return -101
            
            cur_max = max(node.val, cur_max)

            left = dfs(node.left, cur_max)
            if left and cur_max <= left:
                self.res += 1
 
            right = dfs(node.right, cur_max)
            if right and cur_max <= right:
                self.res += 1

            print(left, right)
            return node.val
        
        dfs(root, -101)
        return self.res

        