class MyQueue:

    def __init__(self):
        # using inbox and outbox for maintaing first leemnt to pop
        # and beahve as queue
        # whenever our inbox is empty - we empty all the content of outbox in it
        # that way last element becomes first for corretc ppop behavoiour
        self.inbox = deque()
        self.outbox = deque()

    def push(self, x: int) -> None:
        self.outbox.append(x)
        

    def pop(self) -> int:
        if self.inbox: return self.inbox.pop()
        else:
            while self.outbox:
                self.inbox.append(self.outbox.pop())
            return self.inbox.pop()
        

    def peek(self) -> int:
        popped = self.pop()
        self.inbox.append(popped)
        return popped
        

    def empty(self) -> bool:
        return not self.inbox and not self.outbox
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()