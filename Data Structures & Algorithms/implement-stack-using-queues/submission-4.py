class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        # follow pop push

        # pop and push all ements except the end at teh temp
        for r in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
                
        return self.q.popleft()

    def top(self) -> int:
        popped = self.pop()
        self.push(popped)
        return popped
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()