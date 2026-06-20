class StockSpanner:

    def __init__(self):
        # in this porblem th elimiting factor is th eprice greater that is before us
        # this price beofre us - absorbs al the less prices span before it as well
        # if we encounter a price beofre us that is less than us we absorb its span
        self.stack = []

    def next(self, price: int) -> int:
        # before appending to the stack, we must miantain monoonic decreasing stack
        # wher anything less than it we absorb into our span
        # the greater ones keep their span 
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            # abosrb smaller popped span into us
            span += self.stack.pop()[1]
        self.stack.append((price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)