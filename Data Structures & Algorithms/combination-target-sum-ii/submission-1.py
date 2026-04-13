class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates, key=lambda x: x)

        def dfs(idx, cur, total):
            # Good
            if total == target:
                res.append(cur.copy())
                return

            # Bad
            if total > target or idx >= len(nums):
                return

            # Take
            cur.append(nums[idx])
            dfs(idx + 1, cur, total + nums[idx])

            # Clean
            cur.pop()

            # Elimate dups
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            
            # Pass
            dfs(idx + 1, cur, total)
        
        dfs(0, [], 0)
        return res
            

        