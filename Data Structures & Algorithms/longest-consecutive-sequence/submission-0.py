class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for n in set_nums:
            if (n - 1) not in set_nums:
                length = 0
                while (n + length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest


