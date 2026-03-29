class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        set_nums = set(nums)

        return len_nums != len(set_nums)
        
