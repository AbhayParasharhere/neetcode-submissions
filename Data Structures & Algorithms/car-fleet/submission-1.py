class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first get the time array
        n = len(position)
        cars = list(zip(position,speed))
        stack = deque()
        cars.sort()

        for p,v in cars:
            t = (target - p) / v
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
        