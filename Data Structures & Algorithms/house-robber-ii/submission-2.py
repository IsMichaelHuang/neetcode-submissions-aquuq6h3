class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0] if not nums else nums[0]

        rob1 = rob2 = 0
        # [ rob1, rob2, n, n+1, ...]
        for n in nums[:len(nums) - 1]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        first = rob2

        rob1 = rob2 = 0
        for n in nums[1:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        second = rob2

        return first if first > second else second
    
        

        