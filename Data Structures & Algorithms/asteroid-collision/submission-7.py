class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        incDestroyed = False

        for inc in asteroids:
            # collide when inc is - and stack top is +
            while not incDestroyed and stack and stack[-1] > 0 and inc < 0:
                if abs(inc) > abs(stack[-1]):
                    stack.pop()
                elif abs(inc) == abs(stack[-1]):
                    stack.pop()
                    incDestroyed = True
                else:
                    # inc is less so its destoyed
                    incDestroyed = True
            if not incDestroyed: stack.append(inc)
            # reset flag for later inc
            incDestroyed = False
        return list(stack)