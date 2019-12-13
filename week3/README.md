# Stack&Queue
## Stack
* Stack的功能
  * Push : 把data放進Stack
  * Pop : 移除Stack最上面的資料
  * Top : 回傳最上面的資料
  * IsEmpty : 確認Stack是否有資料
  * getSize : 回傳Stack裡的資料個數
```python
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
```
## Queue
* Queue的功能
  * Push(data) : 把資料從Queue的「後面」放進Queue，並更新成新的back
    * 在Queue中新增資料又稱為enqueue
  * Pop : 把front所指向的資料從Queue中移除，並更新front
    * 從Queue刪除資料又稱為dequeue
  * getFront : 回傳front所指向的資料
  * getBack : 回傳back所指向的資料
  * IsEmpty : 確認Queue裡是否有資料
  * getSize : 回傳Queue裡的資料個數
```python
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
```
