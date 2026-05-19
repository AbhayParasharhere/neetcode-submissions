class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        count = 1 # default value even if stack is empty
        temp = deque()
        while self.stack and self.stack[-1] <= price:
            temp.append(self.stack.pop())
            count += 1
        # in the end we want to preseve thes epopped value so rattach
        while temp:
            self.stack.append(temp.popleft())
        # reagrdless after popping and calculating we 
        # must send the temp into the self.stack
        self.stack.append(price)
        return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)