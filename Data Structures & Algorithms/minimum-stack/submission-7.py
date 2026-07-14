class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        # push to main stack
        self.st.append(val)
        if not self.min_st or self.min_st[-1] >= val:
            # push in case of start fresh with min stack or
            # we get a smaller value or minm
            self.min_st.append(val)

    def pop(self) -> None:
        elm = self.st.pop()
        if elm == self.min_st[-1]:
            # in case its the min being ejected
            self.min_st.pop()
        return elm
        

    def top(self) -> int:
        return self.st[-1] if self.st else None
        

    def getMin(self) -> int:
        return self.min_st[-1] if self.min_st else None
        
