class FreqStack:

    def __init__(self):
        # we maintain a hmap
        # and another fmap to stacks whihc stores the stacks of elemnts at those freq level
        # we keep track of larget freq and remove elments from largest freq stack first then go down
        self.hmap = {}
        self.maxf = 0
        self.fmap = {}

    def push(self, val: int) -> None:
        # update freq
        self.hmap[val] = self.hmap.get(val,0) + 1
        self.maxf = max(self.maxf, self.hmap[val])   
        freq = self.hmap[val] 

        if freq not in self.fmap: self.fmap[freq] = deque()

        self.fmap[freq].append(val) 

    def pop(self) -> int:
        # we remove from teh max f stack in fmap first
        elm = self.fmap[self.maxf].pop()
        # update hmap properly
        self.hmap[elm] -= 1
        if self.hmap[elm] <= 0: del self.hmap[elm]

        if len(self.fmap[self.maxf]) <= 0:
            del self.fmap[self.maxf]
            self.maxf -= 1 #since linear increase lower value is guaranteed
        
        return elm
        


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()