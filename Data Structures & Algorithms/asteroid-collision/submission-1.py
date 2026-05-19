class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # collision only happens in the next asteriod in line
        # so ideal for stack 
        # the case for collison is always between the top of stack and
        # the asteriod we are trying to put next
        # collsion happens due to sign diff
        # either at teh end of collison - asteroid at top of stack survives
        # or the asteriod we are trying put next doesnt survive

        stack = deque()
        done = False

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                top = stack[-1]
                # collsion condition on teh stack from teh incoming
                if abs(top) > abs(ast):
                    # top survives and incoming ast is destroyed
                    done = True
                    break
                elif abs(top) == abs(ast):
                    done = True
                    stack.pop()
                    break
                else:
                    stack.pop()
                    done = False

            if not done:
                stack.append(ast)
            done = False

        return list(stack)