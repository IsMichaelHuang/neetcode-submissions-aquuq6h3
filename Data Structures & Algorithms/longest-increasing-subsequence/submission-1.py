from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for n in nums[1:]:
            if dp[-1] < n:
                dp.append(n)
                continue
            
            idx = bisect_left(dp, n)
            dp[idx] = n
        return len(dp)


        