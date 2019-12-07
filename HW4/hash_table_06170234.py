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
        h = MD5.new()
        h.update(key.encode('utf-8'))
        key = int(h.hexdigest(), 16)
        index = key % self.capacity
        cur_node = self.data[index]
        if cur_node==None:
            return
        if self.data[index].val == key:
            self.data[index] = self.data[index].next
            return
        head = self.data[index]
        while head.next.val != key:
            head = head.next
        
        
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
