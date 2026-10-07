class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # for i in range(n):                    # try every start
        #     gas_net = gas[i]                  # first fill at the start
        #     cur = i                           # station we're standing at
        #     completed = True

        #     for steps_taken in range(n):      # exactly n legs
        #         j = (cur + 1) % n             # station we drive to

        #         gas_cost_to_pay = cost[cur]   # pay to leave the current station
        #         gas_net -= gas_cost_to_pay
        #         if gas_net < 0:               # ran dry on the road, before reaching j
        #             completed = False
        #             break

        #         gas_received = gas[j]         # arrived at j, fill up
        #         gas_net += gas_received
        #         cur = j

        #     if completed:
        #         return i

        # return -1

        # optimal
        # now we dont need to cehck the circle we can complete the chain going froward ina poistive or 0 the previou would definely be completed as well
        if sum(gas) < sum(cost): return -1

        tank = res = 0

        # now we are guarteed a solution cos there exits 
        for at in range(n):
            tank += gas[at] - cost[at]
            if tank < 0:
                # this is not the result conutinue
                tank = 0
                res = at + 1
        return res


