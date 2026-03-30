class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = res = nums[0]
        for i in nums[1:]:
            max_ending = max(max_ending + i, i)
            res = max(max_ending, res)
        return res
        