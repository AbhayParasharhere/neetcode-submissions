class MinStack:

    def __init__(self):
        self.st = deque()
        self.q = deque()

    def push(self, val: int) -> None:
        # when we push we cehck teh monotonicty of the q
        self.st.append(val)

        if not self.q or self.q[-1] >= val:
            # now only i can push to keep track of the min
            self.q.append(val)

    def pop(self) -> None:
        check = self.st.pop()
        if self.q[-1] == check:
            self.q.pop()
        
    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.q[-1]
        
