class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or idx >= len(nums):
                return
            
            cur.append(nums[idx])

            # Take it
            helper(idx, cur, total + nums[idx])

            # Over shot
            cur.pop()

            # Leave it
            helper(idx + 1, cur, total)
        
        helper(0, [], 0)
        return res
            

        