class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        # here limit is again teh prev price who is greater as before
        # so again intrested in decreasing montonic stack
        # evry greater price down the stack knows its own span
        # as every greater pirce has already absorbed span before it for less price
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price,span))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)