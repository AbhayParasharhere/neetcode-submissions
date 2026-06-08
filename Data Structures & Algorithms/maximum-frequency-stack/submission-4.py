class FreqStack:

    def __init__(self):
        self.hmap = {}
        self.fmap = {}
        self.maxF = 0

    def push(self, val: int) -> None:
        # update the hmap and max
        self.hmap[val] = self.hmap.get(val,0) + 1
        f = self.hmap[val]
        self.maxF = max(self.maxF, f)

        # Now push it to the appropriate fmap stack
        if f not in self.fmap:
            self.fmap[f] = deque()
        self.fmap[f].append(val)


    def pop(self) -> int:
        # we just need to pop from the maxF freq stack
        freq = self.fmap[self.maxF].pop()
        # remove from the hmap as well
        self.hmap[freq] -= 1
        if self.hmap[freq] <= 0: self.hmap.pop(freq)


        # in case we reach the end of that max freq stack, move to the prev
        if not self.fmap[self.maxF]:
            self.fmap.pop(self.maxF)
            # update max
            self.maxF -= 1
        return freq
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()