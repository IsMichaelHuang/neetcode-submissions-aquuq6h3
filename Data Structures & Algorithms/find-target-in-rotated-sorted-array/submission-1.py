class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Like a sliding window we need to check the range from mid and either the left and right
        l, r = 0, len(nums) - 1
        pivot = r
        smallest = nums[-1]

        # We need to find the pivot
        while l <= r:
            if nums[l] < nums[r]:
                pivot = l
                smallest = nums[l]
                break
            
            mid = (l + r) // 2 
            if smallest > nums[mid]:
                pivot = mid
                smallest = nums[mid] 

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        # Found the pivot
        if nums[pivot] <= target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            r = pivot
            l = 0
        
        if nums[pivot] == target:
            return pivot

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        print(pivot)  
            
        return -1
        