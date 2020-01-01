## Hash Table 與 Hash function 原理
HashTable是一種資料結構，把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來，把key值依照hash後得到的index值，放入在各個table中，比如說我今天hash時是%10，那麼key:1006的index就是6，那麼我的table也要有0~9，10個去存放我的資料，假使現在有一個key值為2006，index與剛剛的1006一樣，那麼就把第二個進來的2006接在1006後面，將每個table裡的資料形成linkedlist接下去。HashFunction是將key值轉換成index值，例如現在我有8個table，那我可以把hash設定成取key%8的值為index，這樣經過%8後的值會有0,1,2,3,4,5,6,7，接著編好index後再使用hashset來add、remove、contains。因為此次作業有規定要用MD5去加密，所以在hash時要先將文字轉換成數字，才能去hash值得到index值

![image](https://github.com/hans0517/hans/blob/master/week11/HashTable.png)

## Hash Table code
```python
from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        h = MD5.new()
        h.update(key.encode('utf-8'))
        key = int(h.hexdigest(), 16)
        index = key % self.capacity
        cur_node = self.data[index]
        if self.data[index] == None:
            self.data[index] = ListNode(key)
            return
        if self.data[index] == key:
            return
        else:
            if cur_node.val == key:
                return
            if cur_node.val != key:
                cur_node.next = ListNode(key)
            while cur_node.next != None:
                cur_node = cur_node.next


    def remove(self, key):
        if self.contains(key) == True:
            h = MD5.new()
            h.update(key.encode('utf-8'))
            key = int(h.hexdigest(), 16)
            index = key % self.capacity
            cur_node = self.data[index]
            if cur_node==None:
                pass
            if self.data[index].val == key:
                self.data[index] = self.data[index].next
                return
            elif cur_node.next != None:
                while cur_node.next:
                    if cur_node.next.val == key:
                        cur_node.next = cur_node.next.next
                    else:
                        cur_node = cur_node.next
                return
        else:
            pass
        
        
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode('utf-8'))
        key = int(h.hexdigest(), 16)
        index = key % self.capacity
        cur_node = self.data[index]
        try:
            if cur_node.val == None:
                return False
            elif cur_node.val != key:
                cur_node = cur_node.next
            while cur_node.val != key:
                cur_node = cur_node.next
        except:
            pass
        else:
            pass
        finally:
            pass
        
        if not cur_node:
            return False
        if cur_node.val == key:
            return True
```
