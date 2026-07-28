class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minimumStack[-1] if self.minimumStack else val)
        self.minimumStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimumStack[-1]
        
