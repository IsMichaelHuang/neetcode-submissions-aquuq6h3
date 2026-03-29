class Solution:
    # No duplicate triplets
    # May return output and the triplets in any order
    # Min length 3
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            # Protect against dups and off-by-one error...
            if i > 0 and num == nums[i - 1]:
                continue
            
            # TwoSumII
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Does it equal to 0??
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    # Avoids dups with conjunction with the sorted list
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
        
        