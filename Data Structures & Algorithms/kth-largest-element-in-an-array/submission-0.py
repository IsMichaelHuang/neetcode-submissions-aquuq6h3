class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        nlen = len(nums) - k

        res = 0
        for _ in range(nlen + 1): 
            res = heapq.heappop(nums)
        return res
        