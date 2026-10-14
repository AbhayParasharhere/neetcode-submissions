class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # cretae 2 q's of r and d memebers as each meebrs just pops off the first enrty in teh q
        # or logically it means the closest entry to them aftwrwards
        # the greed crietria here. is that each menebr just locally takes care of tehir closest emebr and that reuslts in oevrall best

        at = 0
        popped = set()
        r = deque()
        d = deque()

        for i,mem in enumerate(senate):
            if mem == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r or d:
            while at in popped:
                at = (at + 1) % len(senate)
            
            cur = senate[at]
            # print(at,cur,r,d)
            if cur == "R":
                # he pops the d q
                if not d:
                    return "Radiant"
                popped.add(d.popleft())
                # since i have banned im on teh lowest rpiorty of the enemy i will move to the end
                r.append(r.popleft())
            else:
                # he pops the r q
                if not r:
                    return "Dire"
                popped.add(r.popleft())
                d.append(d.popleft())
            at = (at + 1) % len(senate)
