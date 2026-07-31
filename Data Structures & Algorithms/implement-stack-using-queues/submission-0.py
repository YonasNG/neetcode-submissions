class MyStack:

    def __init__(self):
        self.d = deque()
        
    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        for i in range(len(self.d) - 1):
            self.d.append(self.d.popleft())
        return self.d.popleft()

    def top(self) -> int:
        for i in range(len(self.d) - 1):
            self.d.append(self.d.popleft())
        ans = self.d.popleft()
        self.d.append(ans)
        return ans

    def empty(self) -> bool:
        return not self.d
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()