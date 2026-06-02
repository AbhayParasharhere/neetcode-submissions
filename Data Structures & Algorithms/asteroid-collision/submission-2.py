class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = deque()
        inc = 0
        incDestroyed = False

        while inc < n:
            if not stack: stack.append(asteroids[inc])
            else:
                # only collision when one is moving rt and other left
                # no collison when stack top is moving right and other is left or right
                while stack and stack[-1] > 0 and asteroids[inc] < 0:
                    # Collision conditon
                    if abs(asteroids[inc]) > abs(stack[-1]):
                        stack.pop() #last asteroid is destroyed on top of stack
                    else:
                        if abs(asteroids[inc]) == abs(stack[-1]): stack.pop()
                        # incoming is destoryed
                        incDestroyed = True
                        break
                if not incDestroyed: stack.append(asteroids[inc])
            incDestroyed = False
            inc += 1
        return list(stack)
            
