class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        for i in range(len(self.stack) - 1):
            temp.append(self.stack.pop())
        res = self.stack.pop()
        # now fill the stack back in reverse
        for i in range(len(temp)):
            self.stack.append(temp[len(temp) - 1 - i])
        return res


    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()