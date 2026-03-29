class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    match (top, ch):
                        case ("(", ")") | ("[", "]") | ("{", "}"):
                            pass
                        case _ :
                            return False  
        return len(stack) == 0

        