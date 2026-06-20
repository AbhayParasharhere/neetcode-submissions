class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # an incoming asteroid keeps destroying when the collsion condirions ar e et
        # collsion condirion is that in our stack top is positive which incoing is negative
        # incoming destroyed when it encounetrs a greater size asteriod or replaces eveything in satck
        stack = []
        incDestroyed = False
        for astr in asteroids:
            while not incDestroyed and stack and stack[-1] > 0 and astr < 0:
                # collision condition
                if abs(stack[-1]) > abs(astr):
                    incDestroyed = True
                elif abs(stack[-1]) < abs(astr):
                    stack.pop()
                else:
                    incDestroyed = True
                    stack.pop()
            if not incDestroyed: stack.append(astr)
            incDestroyed = False
        
        return stack
