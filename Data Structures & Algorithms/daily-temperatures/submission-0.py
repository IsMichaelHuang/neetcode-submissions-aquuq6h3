class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # Do Work
            while stack and temp > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                output[stack_i] = i - stack_i
            stack.append([i, temp])
        
        return output 
            
        