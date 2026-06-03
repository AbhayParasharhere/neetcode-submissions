class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        # stack stroes teh price and teh span at that point
        # we are intrested in the montonic decreasing stack
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price,span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)