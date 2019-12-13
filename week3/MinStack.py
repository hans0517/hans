class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)
        self.len+=1

    def pop(self) -> None:
        self.list.pop(self.len-1)
        self.len-=1

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)
