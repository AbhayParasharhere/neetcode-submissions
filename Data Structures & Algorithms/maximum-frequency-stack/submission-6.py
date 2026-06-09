class FreqStack:

    def __init__(self):
        # using a hmap, maxf, and a freq stack map which maps to stacks at that freq
        self.hmap = {}
        self.fmap = {}
        self.maxf = 0

    def push(self, val: int) -> None:
        # update the hmap freq
        self.hmap[val] = self.hmap.get(val,0) + 1
        self.maxf = max(self.maxf,self.hmap[val])

        # put it in the correct fmap stack
        if not self.hmap[val] in self.fmap:
            self.fmap[self.hmap[val]] = deque()
            # need to push as well
        self.fmap[self.hmap[val]].append(val)
        

    def pop(self) -> int:
        # we pop from the freq stack with the max f
        # print(self.hmap,self.maxf,self.fmap,len(self.fmap[self.maxf]))
        popped = self.fmap[self.maxf].pop()
        # remove from the hmap its freq
        self.hmap[popped] -= 1
        if self.hmap[popped] <= 0: self.hmap.pop(popped)


        # recalculate the maxf in case teh whole stack is now empty
        if len(self.fmap[self.maxf]) <= 0:
            # print('removed')
            self.fmap.pop(self.maxf)
            self.maxf -= 1
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()