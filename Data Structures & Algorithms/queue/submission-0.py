class Deque:
    
    def __init__(self):
        self.d = deque()

    def isEmpty(self) -> bool:
        return not self.d

    def append(self, value: int) -> None:
        self.d.append(value)

    def appendleft(self, value: int) -> None:
        self.d.appendleft(value)        

    def pop(self) -> int:
        if self.d:
            return self.d.pop()
        return -1

    def popleft(self) -> int:
        if self.d:
            return self.d.popleft()
        return -1
