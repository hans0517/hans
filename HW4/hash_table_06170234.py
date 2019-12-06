class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def ghash(self, key):
        from Crypto.Hash import MD5
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        x = int(h.hexdigest(), 16)
        index = x % self.capacity
        return index
    
    def add(self, key):
        index = self.ghash(key)
        if self.data[index] == None:
            self.data[index] = ListNode(key)
            return
        if self.data[index] == key:
            return
        else:
            cur_node = self.data[index]
            while cur_node != None:
                if cur_node == key:
                    return
                if cur_node.next == None:
                    cur_node.next = ListNode(key)
                    return
                if cur_node.next != None:
                    cur_node = cur_node.next
            return
    
    def remove(self, key):
        index = self.ghash(key)
        cur_node = self.data[index]
        if not self.contains(key):
            return
        elif key == self.data[index].val:
            self.data[index] = self.data[index].next
            return
        elif cur_node.next != None:
            while cur_node.next:
                if cur_node.next.val == key:
                    cur_node.next = cur_node.next.next
                else:
                    cur_node = cur_node.next
            return
        
    def contains(self, key):
        index = self.ghash(key)
        cur_node = self.data[index]
        try:
            if cur_node.val == None:
                return False
            elif cur_node.val != key:
                cur_node = cur_node.next
        except:
            pass
        else:
            pass
        finally:
            pass
        
        if not cur_node:
            return False
        if cur_node.val is key:
            return True
