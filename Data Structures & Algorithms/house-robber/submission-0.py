class Solution:
    def rob(self, nums: List[int]) -> int:
        nskip = skip = 0
        for num in nums:
            temp = max(skip + num, nskip)
            skip = nskip
            nskip = temp
        return nskip

