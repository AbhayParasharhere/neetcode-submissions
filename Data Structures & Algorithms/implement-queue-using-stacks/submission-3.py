class MyQueue:

    def __init__(self):
        self.inbox = deque()
        self.outbox = deque()

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def pop(self) -> int:
        # Now logic is to get this val from outbox
        if self.outbox: return self.outbox.pop()
        else:
            # get everything from inbox into outbox
            while self.inbox:
                self.outbox.append(self.inbox.pop())
            return self.pop()
        

    def peek(self) -> int:
        # in peek we call pop then push it back to outbox
        tp = self.pop()
        self.outbox.append(tp)
        return tp

    def empty(self) -> bool:
        return len(self.inbox) == 0 and len(self.outbox) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()