class MyQueue:

    def __init__(self):
        # uses an inbox stack and outbox stack
        # wheneevr tehre is anything in box stack, pop and push in outward stack
        # that reverses teh order and now last element is at front so it beahves like Q
        # to remove element we look to outbox always
        # we push elements in inbox
        self.inbox = []
        self.outbox = []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        # clear out inbox first only if outbox is empty
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        # now outbox contains the first element from inbox as outbox
        # bahaves like a Q
        return self.outbox.pop()
        
    def peek(self) -> int:
        elem = self.pop()
        # must put it back at teh outbox
        self.outbox.append(elem)
        return elem

    def empty(self) -> bool:
        if not self.outbox and not self.inbox:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()