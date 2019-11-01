class MyLinkedList:
    def __init__(self): #初始化數據結構
        self.head = None
        self.len = 0
        
    def get(self, index: int) -> int:
        if index>=self.len-1 or index==0:
            return -1
        else:
            i = 1
            while i<=index:
                cur_node = self.head
                cur_node = cur_node.next
                i+=1
                return cur_node.val
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)
        cur_node = self.head
        new_node.next = cur_node
        new_node = self.head
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)
        cur_node = self.head
        if self.head == None:
            return
        else:
            for _ in range(self.len):
                if cur_node.next == None:
                    break
                else:
                    cur_node.next = cur_node
                    cur_node.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = ListNode(val)
        cur_node = self.head
        if index > self.len:
                return -1
        elif index <= 0 or self.len == 0:
            self.addAtTail(val)
        else:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
                return cur_node.val
        

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
