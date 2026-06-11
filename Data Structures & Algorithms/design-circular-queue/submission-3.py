class LinkedList:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def print_from_node(self, node):
        """Prints the linked list starting from the specified node."""
        current = node
        elements = []
        
        while current:
            elements.append(str(current.val))
            current = current.next
            
        print(" -> ".join(elements))

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.curSize = 0
        n = LinkedList(0)
        self.front = n
        self.back = n
        # front and back are trailing pointer their next pointer point to the actual front and back

    def enQueue(self, value: int) -> bool:
        if self.curSize >= self.size: return False
        # we are pushing an element to the linkedin list to the back

        if not self.front.next:
            # its the first element
            self.front.next = self.back.next = LinkedList(value)
        else:
            # we append to the back
            attach = LinkedList(value)
            # first advance back pointer then attach
            self.back = self.back.next
            self.back.next = attach

        self.curSize += 1
        return True

    def deQueue(self) -> bool:
        # we are popping from the front
        if self.curSize <= 0: return False

        self.front.next = self.front.next.next
        self.curSize -= 1

        if self.curSize == 0:
            self.front = self.back
            # so hat back is not left dangling
        return True

    def Front(self) -> int:
        return self.front.next.val if self.curSize > 0 else -1
        

    def Rear(self) -> int:
        return self.back.next.val if self.curSize > 0 else -1
        

    def isEmpty(self) -> bool:
        return self.curSize == 0
        

    def isFull(self) -> bool:
        return self.size == self.curSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()