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
                        stack.append(left + right)
                    case ("-"):
                        stack.append(left - right)
                    case ("*"):
                        stack.append(left * right)
                    case ("/"):
                        # int() truncates towards 0
                        stack.append(int(left / right))
                    case _:
                        pass
            else:
                stack.append(int(i))
        
        return stack.pop()
    
    # Time: O(n) where n is the length of the given list
    # Space: O(m) where m is the # of operands
                    
        