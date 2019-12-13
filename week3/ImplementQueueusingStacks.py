class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.write = []
        self.read = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.write.append(x)
    
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.write ==[]:
            return None
        else:
            while self.write != []:
                self.read.append(self.write.pop())
            res = self.read.pop()
            while self.read != []:
                self.write.append(self.read.pop())
            return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.write ==[]:
            return None
        else:
            return self.write[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.write == []
