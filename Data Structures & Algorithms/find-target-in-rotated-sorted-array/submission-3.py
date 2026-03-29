class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Like a sliding window we need to check the range from mid and either the left and right
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # Left sorted portion
            if nums[l] <= nums[mid]:
                # Target has a stronger chance of being to the right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sorted portion
            else:
                # Target has a stronger chance of being to the left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1
        