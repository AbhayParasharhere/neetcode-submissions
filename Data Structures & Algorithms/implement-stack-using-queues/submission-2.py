class MyStack:

    def __init__(self):
        self.st = deque()

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        # pop and push n- 1 times
        for i in range(len(self.st) - 1):
            self.push(self.st.popleft())
        # the last pop remove sthe last element from teh que 
        # which is simulating stack
        return self.st.popleft()


    def top(self) -> int:
        # call pop and then reinsert in teh end through push
        tp = self.pop()
        self.push(tp)
        return tp

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()