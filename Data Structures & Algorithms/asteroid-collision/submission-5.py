class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l = 0
        stack = deque()
        incDestroyed = False

        for inc in asteroids:
            # collission condition keeps happening until one of 2 things happen
            # inc destroys the full stack, inc is stopped and some elements may be destroyed
            while stack and inc < 0 and stack[-1] > 0:
                against = stack[-1]
                if abs(inc) > abs(against): stack.pop()
                elif abs(inc) == abs(against):
                    stack.pop()
                    incDestroyed = True
                    break
                else:
                    incDestroyed = True
                    break
                    # break stops the collision otherwise loop will reoccur
                    # with same incoming
            if not incDestroyed: stack.append(inc)
            incDestroyed = False
        
        return list(stack)
