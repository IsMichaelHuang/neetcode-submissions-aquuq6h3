class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = [] 

        for i in tokens:
            if i in "+-*/":
                # LIFO
                right = stack.pop()
                left = stack.pop()
                opnd = i
                match (opnd):
                    case ("+"):
                        result = left + right
                    case ("-"):
                        result = left - right
                    case ("*"):
                        result = left * right
                    case ("/"):
                        result = int(left / right)
                    case _:
                        pass
                stack.append(result)
            else:
                stack.append(int(i))
        
        return stack[0]
    
    # Time: O(n) where n is the length of the given list
    # Space: O(m) where m is the # of operands
                    
        