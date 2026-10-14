class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if we have a guarantted gas > = cost tehn we dont need to rechedk teh roudned portion
        # we just need to ensure from a point we can go to the end

        if sum(gas) < sum(cost): return -1

        # guaranteed yes atleast we can complete the trip, just the starting point is left to be found

        res = 0
        at = 0
        gas_left = 0
        while at < len(gas):
            # assume res is res
            # but for it to be valid at must reach the end
            gas_left +=  gas[at] - cost[at]
            if gas_left < 0:
                # reset gas as we now consider a new start point at + 1
                gas_left = 0
                res = at + 1
            at += 1
        return res
        