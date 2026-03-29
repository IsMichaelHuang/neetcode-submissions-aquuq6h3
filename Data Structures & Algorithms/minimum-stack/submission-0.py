class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if val < self.min_val:
            self.min_val = val
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

        self.min_val = float('inf')
        for i in self.stack:
            if i < self.min_val:
                self.min_val = i
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val
        
