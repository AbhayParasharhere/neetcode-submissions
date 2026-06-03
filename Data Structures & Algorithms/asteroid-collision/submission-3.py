class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = deque()
        incDone = False

        for inc in asteroids:
            while stack and stack[-1] > 0 and inc < 0:
                # This is the collision condition
                # Nowe we see how the collsion resulted

                if abs(inc) > abs(stack[-1]):
                    stack.pop()
                    continue
                else:
                    if abs(stack[-1]) == abs(inc):
                        stack.pop()
                    incDone = True
                    break
            if not incDone: stack.append(inc)
            incDone = False
        return list(stack)