class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]

        # Find the intersection
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the entry
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return tortoise

        