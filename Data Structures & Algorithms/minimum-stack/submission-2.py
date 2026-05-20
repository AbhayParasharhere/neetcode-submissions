class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        # push to normal stack
        self.stack.append(val)
        if self.minStack and self.minStack[-1] >= val:
            # push the new min to keep track of the minimums
            self.minStack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        

    def pop(self) -> None:
        removed = self.stack.pop()
        # if this is the top of min stack then pop it off the minstack as well
        if self.minStack and self.minStack[-1] == removed:
            # just avoiding this condition will help us maintain correct stacks in both cases
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print(self.stack,self.minStack)
        return self.minStack[-1]
       