class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we calculate the time it takes for each car to reach the destination
        # we sort the car by position
        # if the time for the car in back is more than car in front - then it will never reach
        # the ahead car and form a fleet on its own
        # so the real limit is time of car before mroe than time ahead
        # so we are interested in monotic decreasing stack as interested in greater time
        # if time is less than car in front - then it will reach and merge with the ahead car 
        # the time ahed will remain its just that the before car will merge to the fleet

        stack = []
        ps = list(zip(position,speed))
        # sort by 1st apram position by default, so pairs are now sorted
        ps.sort()

        for p,s in ps:
            t = (target - p) / s
            # even if time before is equal to ahead that means they will mett at target
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
