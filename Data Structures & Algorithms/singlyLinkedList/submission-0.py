class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # Dummy Node
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next
        return output
        
