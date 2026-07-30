class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr != self.tail and index == 0:
            return curr.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        first, second, new = self.head, self.head.next, Node(val)
        new.next = second
        new.prev = first
        first.next = new
        second.prev = new
        
    def addAtTail(self, val: int) -> None:
        new, tail, last = Node(val), self.tail, self.tail.prev
        new.next = tail
        new.prev = tail.prev
        last.next = new
        tail.prev = new 

    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new.next = curr
            new.prev = curr.prev
            curr.prev.next = new
            curr.prev = new

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)