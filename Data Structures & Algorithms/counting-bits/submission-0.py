class Solution:
    def countBits(self, nums: int) -> List[int]:
        dp = [0] * (nums + 1) 
        offset = 1

        for n in range(1, nums + 1):
            if offset * 2 == n:
                offset = n
            
            dp[n] = 1 + dp[n - offset]
        return dp

        