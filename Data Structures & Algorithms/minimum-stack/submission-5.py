class MinStack:

    def __init__(self):
        # use a second stack for maintaing mimimum
        # its top always contain the oevrall min in stack
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
             self.minStack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.minStack and pop == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
