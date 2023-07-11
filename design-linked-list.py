class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None
        
class MyLinkedList:
    def __init__(self):
        self.dum = Node()

    def get(self, indx: int) -> int:
        temp = self.dum
        for _ in range(indx + 1):
            if temp:
                temp = temp.next
        if temp:
            return temp.data
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        old_head = self.dum.next
        new_head.next = old_head
        if old_head:
            old_head.prev = new_head
        self.dum.next = new_head
        new_head.prev = self.dum
        

    def addAtTail(self, val: int) -> None:
        old_tail = self.dum
        while old_tail and old_tail.next:
            old_tail = old_tail.next
        new_tail = Node(val)
        if old_tail:
            old_tail.next = new_tail
        new_tail.prev = old_tail
        
        
    def addAtIndex(self, indx: int, val: int) -> None:
        prv = self.dum
        for _ in range(indx):
            if prv:
                prv = prv.next
        if prv and prv.next:
            new_node = Node(val)
            new_node.next = prv.next
            new_node.next.prev = new_node
            prv.next = new_node
            new_node.prev = prv
        if prv and not prv.next:
            self.addAtTail(val)  
        
        

    def deleteAtIndex(self, indx: int) -> None:
        temp = self.dum
        for _ in range(indx):
            if temp:
                temp = temp.next
        
        if temp and temp.next:
            temp.next = temp.next.next
        
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)