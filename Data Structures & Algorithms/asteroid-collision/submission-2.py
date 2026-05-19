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

        for ast in asteroids:
            if len(stack) > 0:
                top = stack[-1]
                # collision condition is top must be moving right or positive and ast coming must be -ve or left
                if top > 0 and ast < 0:
                    # print(ast,top,stack)
                    # collision condition
                    # see who survives
                    if abs(top) > abs(ast):
                        # top survives
                        # dont put anything on the stack
                        continue
                    elif abs(top) == abs(ast):
                        # destroy both top and dont put ast
                        stack.pop()
                    else:
                        # top of stack doesnt survive
                        stack.pop()
                        # get the next top element and keep trying until top of stack 
                        # survives or the stack becomes empty if yes
                        # put the ast then
                        while len(stack) > 0:
                            top = stack[-1]
                            if top > 0 and ast < 0:
                                # collison condition
                                if abs(top) < abs(ast):
                                    stack.pop()
                                elif abs(top) == abs(ast):
                                    # destroy both top and dont put ast
                                    stack.pop()
                                    break
                                else:
                                    # continue dont put this new ast on the stack
                                    break
                            else:
                                # just put the ast in stack
                                stack.append(ast)
                                break
                        if len(stack) == 0:
                            # everything destroyed by teh new incomer so at last only it survives
                            stack.append(ast)
                else:
                    # same direction jyst put it in the stack
                    stack.append(ast)
            else:
                # put the first element
                stack.append(ast)

        return list(stack)