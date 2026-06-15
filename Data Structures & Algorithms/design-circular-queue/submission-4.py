class LinkedList:
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        # we mainaitin a DLL linked list with a dummy front and back
        # we remove from the front and push from the back
        self.front = LinkedList(0)
        self.back = LinkedList(0)

        self.front.next = self.back
        self.back.prev = self.front
        self.capacity = k
        self.size = 0


    def enQueue(self, value: int) -> bool:
        if self.size >= self.capacity: return False

        # create a node
        node = LinkedList(value)
        # insert from the back before the last node
        prev = self.back.prev
        # attach to prev
        prev.next = node
        node.prev = prev

        # attach to next
        node.next = self.back
        self.back.prev = node
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.size <= 0: return False
        # we remove from the front - the node to remove is the self.front.next
        nxt = self.front.next.next
        self.front.next = nxt
        # reattach to the front the nxt node to maintain dll
        nxt.prev = self.front
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size <= 0: return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.size <= 0: return -1
        return self.back.prev.val     

    def isEmpty(self) -> bool:
        return self.front.next == self.back and self.back.prev == self.front

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()