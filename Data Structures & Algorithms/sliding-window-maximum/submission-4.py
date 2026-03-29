class Solution:
    # Fixed window
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  
        result = []
        mono_stack = collections.deque()

        # Edge Case: Nothing to compare to
        if len(nums) < 2:
            return nums

        # Initialize the fixed window
        for i in range(k):
            if not mono_stack:
                mono_stack.append(i)

            # Purge the smallest against current
            while mono_stack and nums[i] > nums[mono_stack[-1]]:
                mono_stack.pop()
            mono_stack.append(i)
        result.append(nums[mono_stack[0]])

        for r in range(k, len(nums)):
            # Purge oldest indices
            while mono_stack and mono_stack[0] < (r - k + 1):
                mono_stack.popleft()
            
            if not mono_stack:
                mono_stack.append(r)

            # Purge smallest values against the cuurent
            while mono_stack and nums[r] > nums[mono_stack[-1]]:
                mono_stack.pop()
            mono_stack.append(r)
            result.append(nums[mono_stack[0]])

        return result

       