class Solution:
    # Non-negative integer values
    # Min of length of 1
    # Min integer value of 0
    def trap(self, height: List[int]) -> int:
        result = 0
        max_left_height = 0
        max_right_height = 0

        l, r = 0, len(height) - 1
        while l < r:
            # Calculate how much water we can trap    
            if height[l] < height[r]:
                result += max(0, (max_left_height - height[l]))

                # update the left value
                max_left_height = max(max_left_height, height[l])

                # Update pointer
                l += 1
            else:
                result += max(0, (max_right_height - height[r]))

                # Update the right value
                max_right_height = max(max_right_height, height[r])

                r -= 1
        
        return result


