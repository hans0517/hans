class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0
        """
        Initialize your data structure here.
        """
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.len:
            return -1
        else:
            H = self.head
            for _ in range(index):
                H = H.next
            return H

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.len+=1
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        H = self.head
        for _ in range(self.len):
            if H.next == None:
                break
            else:
                H = H.next
            H.next = new_node
            self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        H = self.head
        if index > self.len:
            pass
        elif index == self.len:
            self.addAtTail(index)
        else:
            for i in range(self.len):
                if i==(index-1):
                    new_node.next = H.next 
                    H.next = new_node     
                else:
                    H = H.next 
            self.len+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.len or self.len==0 or index < 0:
            return -1
        elif self.len==1:
            self.head=None
            self.len=0
        elif index==0:
            value = self.head
            self.head = value.next
            self.len-=1
        else:
            value = self.head
            for i in range(index):
                if i==(index-1):
                    delete_item = value.next 
                    value.next = delete_item.next
                else:
                    value = value.next
                    self.len-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
