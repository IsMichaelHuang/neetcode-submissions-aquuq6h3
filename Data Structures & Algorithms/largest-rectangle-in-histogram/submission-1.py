class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_h = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                p_w, p_h = stack.pop()
                max_h = max(max_h, ((i - p_w) * p_h))
                start = p_w
            stack.append((start, h))
        
        for i, h in stack:
            max_h = max(max_h, h * (len(heights) - i))

        return max_h

        