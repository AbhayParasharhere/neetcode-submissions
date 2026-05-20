class StockSpanner:

    def __init__(self):
        # using the montonic decreasing stack as we are interested in the previous element
        # greatest than the current to return the span
        self.prices = []
        self.stack = deque()

    def next(self, price: int) -> int:
        self.prices.append(price)
        any_pop = False
        cur = len(self.prices) - 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            any_pop = True
            self.stack.pop()
        prev = self.stack[-1] if self.stack else -1
        self.stack.append(cur)
        return cur - prev

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)