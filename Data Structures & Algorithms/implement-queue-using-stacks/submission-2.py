class MyQueue:

    def __init__(self):
        self.inbox = deque()
        self.outbox = deque()

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        # pop operations needs eveything from inbox popped to outbox, 
        # then pop off the last elemnt from outbox
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def peek(self) -> int:
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]
        
        

    def empty(self) -> bool:
        return (not self.inbox and not self.outbox)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()