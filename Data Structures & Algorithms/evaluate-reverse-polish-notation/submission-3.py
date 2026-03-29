class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Edge case: If it only contains one element
        if len(tokens) < 2:
            return int(tokens[0])
        
        stack = [] 
        result = 0

        for i in tokens:
            # TODO
            print(stack)
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
                # TODO
                print(result)
                stack.append(result)
            else:
                stack.append(int(i))
        
        return result
                    
        