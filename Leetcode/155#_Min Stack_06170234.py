class MinStack:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> None:
        self.list.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)
