class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash the difference between value and target
        remainder = {} 
        for i in range(0, len(nums)):
            if nums[i] in remainder:
                return [remainder[nums[i]], i]
            else:
                delta = target - nums[i]
                remainder[delta] = i
        return [None, None]