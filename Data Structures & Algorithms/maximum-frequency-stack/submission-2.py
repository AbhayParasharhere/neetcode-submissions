class FreqStack:

    def __init__(self):
        self.hmap = {}
        self.fmap = {}
        self.maxF = 0

    def push(self, val: int) -> None:
        if val not in self.hmap: 
            self.hmap[val] = 1
            if self.maxF == 0: self.maxF = 1
            if self.hmap[val] not in self.fmap:
                self.fmap[self.hmap[val]] = deque()
            self.fmap[self.hmap[val]].append(val)
        else:
            self.hmap[val] += 1
            # calculate teh current max frequency
            self.maxF = max(self.maxF, self.hmap[val])
            if self.hmap[val] not in self.fmap:
                self.fmap[self.hmap[val]] = deque()
            self.fmap[self.hmap[val]].append(val)



    def pop(self) -> int:
        # we get the poppe delement from our current max freq stack in fmap
        if self.maxF in self.fmap and self.fmap[self.maxF]:
            popped = self.fmap[self.maxF].pop()
            # need to reduce teh appriate frequency from hmap as well
            self.hmap[popped] -= 1
            if self.hmap[popped] <= 0: self.hmap.pop(popped)
            # print('hmap',self.hmap)
            # print(self.fmap,"--",self.maxF,"popped",popped)
            if len(self.fmap[self.maxF]) == 0:
                self.fmap.pop(self.maxF)
                # next max frqq is 1 -it guaranteed
                self.maxF -= 1
            return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()