class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(d,s) for d,s in zip(position,speed)]

        pair.sort()
        stack = deque()

        # Now we go through the end of the list to maintain our stack
        # this stack keeps track of the car fellet which is the least time taken surving pairs
        # as any other pairs is first compared to the stack if their time taken is less
        # then they are just merging and not put on the stack

        for d,s in pair[::-1]:
            time2reach = (target - d) / s
            if stack and stack[-1] < time2reach:
                # As this car cant reach the next car in line ever
                # put it in the fleet
                stack.append(time2reach)
            if not stack: stack.append(time2reach)

        return len(stack)
